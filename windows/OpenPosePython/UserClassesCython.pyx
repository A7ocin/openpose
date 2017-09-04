import glob
import os
import OpenPosePython as opp
import cv2 as cv
import numpy as np
import ast
import io

cimport numpy as np

cdef class UserInputClass:
    cdef int mCounter
    cdef bint mClosed
    cdef list mImageFiles

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
        # Close program when empty frame
        if (self.mClosed or len(self.mImageFiles) <= self.mCounter):
            print "Last frame read and added to queue. Closing program after it is processed."
		    # This funtion stops this worker, which will eventually stop the whole thread system once all the frames have been processed
            self.mClosed = True
            return None
        else: # if (!mClosed)
		    # Create new datum
            opp.emplaceBack(datumsPtr)
            #self.datum = opp.datum_frompointer(opp.datumsPtr_at(datumsPtr)).__getitem__(0)
            # Fill datum
            self.setImage(datumsPtr, "1280x720", image)
            #if not self.datum.cvInputData:
            #    print "Empty frame detected on path: " + self.mImageFiles[self.mCounter - 1] + ". Closing program."
            #    self.mClosed = True
            #    datumsPtr = None
                
            return datumsPtr

    def setImage(UserInputClass self, datumsPtr, str resolution, np.ndarray np_image):
        cdef int width, height, myWidth, myHeight, w, h, c
        
        width = int(resolution.split('x')[0])
        height = int(resolution.split('x')[1])
        myWidth = len(np_image[0])
        myHeight = len(np_image)
        if (myHeight*float(width)/float(myWidth))>(height):
                factor = float(height)/float(myHeight)
        else:
                factor = float(width)/float(myWidth)
        np_image_temp = cv.resize(np_image, (int(myWidth*factor), int(myHeight*factor)))
        np_image= cv.copyMakeBorder(np_image_temp,0,height-myHeight,0,width-myWidth,cv.BORDER_CONSTANT,value=[0,0,0])
        channels = 3
        for w in range(width):
            for h in range(height):
                for c in range(channels):
                    opp.setElement(h, w, c, datumsPtr, int(np_image[h][w][c]))

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