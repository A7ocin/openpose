import glob
import os
import OpenPosePython as opp
import cv2 as cv
import numpy as np
import ast
import io
import weave

from cython.parallel import parallel, prange

cimport numpy as np
from libc.string cimport memcpy
from cpython.ref cimport PyObject
from libcpp.vector cimport vector
from libcpp.memory cimport shared_ptr

cdef extern from "../../3rdparty/windows/opencv/include/opencv2/core/core.hpp" namespace "cv":
  cdef cppclass Mat:
    Mat() except +
    void create(int, int, int)
    void* data
    int rows
    int cols
    int channels()

cdef Mat np2Mat3D(np.ndarray ary):
    assert ary.ndim==3 and ary.shape[2]==3, "ASSERT::3channel RGB only!!"
    ary = np.dstack((ary[...,2], ary[...,1], ary[...,0])) #RGB -> BGR

    cdef np.ndarray[np.uint8_t, ndim=3, mode ='c'] np_buff = np.ascontiguousarray(ary, dtype=np.uint8)
    cdef unsigned int* im_buff = <unsigned int*> np_buff.data
    cdef int r = ary.shape[0]
    cdef int c = ary.shape[1]
    cdef Mat m
    m.create(r, c, cv.CV_8UC3)
    memcpy(m.data, im_buff, r*c*3)
    return m

cdef class UserInputClass:
    cdef int mCounter
    cdef bint mClosed
    cdef list mImageFiles
    cdef int numberOfImages

    def __init__(UserInputClass self, str directoryPath):
        cdef str cwd
        cwd = os.getcwd()
        os.chdir(directoryPath)
        self.mImageFiles = []
        self.mCounter = 0
        self.mClosed = False
        for file in glob.glob("*.jpg"):
            self.mImageFiles.append(directoryPath+file+"")
        if not self.mImageFiles:
            print "No images found on: " + directoryPath
        os.chdir(cwd)

    def createDatum(UserInputClass self, datumsPtr, np.ndarray image, str resolution):
        numberOfImages = len(self.mImageFiles)
        # Close program when empty frame
        if (self.mClosed or numberOfImages <= self.mCounter):
            print "Last frame read and added to queue. Closing program after it is processed."
		    # This funtion stops this worker, which will eventually stop the whole thread system once all the frames have been processed
            self.mClosed = True
            return None
        else: # if (!mClosed)
		    # Create new datum
            opp.emplaceBack(datumsPtr)
            #self.datum = opp.datum_frompointer(opp.datumsPtr_at(datumsPtr)).__getitem__(0)
            # Fill datum
            
            self.setImage(datumsPtr, resolution, image)

            
            #opp.setInput(datumsPtr, image.tolist(), resolution)

            #if not self.datum.cvInputData:
            #    print "Empty frame detected on path: " + self.mImageFiles[self.mCounter - 1] + ". Closing program."
            #    self.mClosed = True
            #    datumsPtr = None
                
            return datumsPtr

    cdef setImage(UserInputClass self, datumsPtr, str resolution, np.ndarray np_image):
        cdef int width, height, myWidth, myHeight, w, h, c
        cdef float factor
        cdef Mat mat
        cdef bint condition
        
        width = int(resolution.split('x')[0])
        height = int(resolution.split('x')[1])
        myWidth = len(np_image[0])
        myHeight = len(np_image)

        condition = (float(width)/float(myWidth))>(float(height)/float(myHeight))

        if (condition):
                factor = float(height)/float(myHeight)
        else:
                factor = float(width)/float(myWidth)
        np_image_temp = cv.resize(np_image, (int(myWidth*factor), int(myHeight*factor)))
        np_image= cv.copyMakeBorder(np_image_temp, 0, abs(height-len(np_image_temp)), 0, abs(width-len(np_image_temp[0])), cv.BORDER_CONSTANT, value=[0,0,0])
        channels = 3

        #list_temp = [item for sublist in np_image.tolist() for item in sublist]
        #list = [item for sublist in list_temp for item in sublist]

        list = np_image.flatten().reshape(height*width*channels).tolist()  # <--- THIS WORKS

        #list1 = np_image[:, :, 0].flatten().reshape(1,height*width).tolist()
        #list2 = np_image[:, :, 1].flatten().reshape(1,height*width).tolist()
        #list3 = np_image[:, :, 2].flatten().reshape(1,height*width).tolist()
        
        opp.setInputMat(datumsPtr, list, resolution);
        #mat = np2Mat3D(np_image)
        
        #myCy = PyAdditionalCython();

        ##list4 = np.array([[[1, 2], [2, 3], [3, 4]], [[4, 5], [5, 6], [6, 7]]])
        #myCy.setElement(np_image)
        
        #cy.printNumpy(np_image)
       
        #opp.setMat(datumsPtr, <object><void*>mat.data)

        #for h in range(height):              #TODO ----> Move loops to C++
        #    for w in range(width):
        #        for c in range(channels):
        #            opp.setElement(h, w, c, datumsPtr, int(np_image[h][w][c]), width, height)

    def nextImage(UserInputClass self):
        returnImage = self.mImageFiles[self.mCounter]
        self.mCounter +=1
        return returnImage

    def isFinished(UserInputClass self):
        return self.mClosed


cdef class UserOutputClass:
    def init(UserOutputClass self):
        return opp.UserOutputClass()

    def getProcessedImage(UserOutputClass self, datumsPtr, str resolution):
        cdef int width, height, channels, w, h, c
        if (datumsPtr and not opp.datumsPtr_empty(datumsPtr)):
            width = int(resolution.split('x')[0])
            height = int(resolution.split('x')[1])
            channels = 3
            np_array = np.ndarray((height,width,channels), dtype=np.uint8)
            for w in range(width):
                for h in range(height):
                    for c in range(channels):
                        np_array[h][w][c] = opp.getElement(h,w,c,datumsPtr)
            return np_array
        else:
            print "Nullptr or empty datumsPtr found."

def getDatum(datumsPtr):
    return opp.datum_frompointer(opp.datumsPtr_at(datumsPtr)).__getitem__(0)


def openPoseInit(FLAGS):
    
    # User processing
    userInputClass = UserInputClass(FLAGS.image_dir)
    userOutputClass =   UserOutputClass()

    opp.configure()
    print "OpenPose configuration done."

    return userInputClass, userOutputClass