import glob, os
import OpenPosePython as opp
import cv2 as cv
import numpy as np
import ast
import io

class UserInputClass:
    def __init__(self, directoryPath): 
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

    def createDatum(self, datumsPtr):
        # Close program when empty frame
	    if (self.mClosed or len(self.mImageFiles) <= self.mCounter):
		    print "Last frame read and added to queue. Closing program after it is processed."
		    # This funtion stops this worker, which will eventually stop the whole thread system once all the frames have been processed
		    mClosed = True;
		    return None;
	    else: # if (!mClosed)
		    # Create new datum
		    opp.emplaceBack(datumsPtr)
            self.datum = opp.datum_frompointer(opp.datumsPtr_at(datumsPtr)).__getitem__(0)
		    # Fill datum
            #np_image = cv.imread(self.mImageFiles[self.mCounter])
            #list_image = np_image.tolist()
            #print type(list_image)
            #print list_image
            #opp.setInput(datumsPtr, list_image)
            opp.setCvInputData(datumsPtr, self.mImageFiles[self.mCounter])     #TODO --> in Python
            self.mCounter+=1

		    # If empty frame -> return nullptr
            if not self.datum.cvInputData:
                print "Empty frame detected on path: " + self.mImageFiles[mCounter - 1] + ". Closing program."
                self.mClosed = True
                datumsPtr = None

            return datumsPtr

    def isFinished(self):
        return self.mClosed


class UserOutputClass:
    def init(self):
        return opp.UserOutputClass()

    def display(self, datumsPtr, width, height):
        # User's displaying/saving/other processing here
	    # datum.cvOutputData: rendered frame with pose or heatmaps
	    # datum.poseKeypoints: Array<float> with the estimated pose
        print "Inside Display"
        if (datumsPtr and not opp.datumsPtr_empty(datumsPtr)):
            print "Datum OK"
            #uchar_vec = opp.mat_at(datumsPtr)
            #print uchar_vec

            mat_array = opp.mat_frompointer(getDatum(datumsPtr).cvOutputData)
            print "mat_array: " + str(getDatum(datumsPtr).cvOutputData)

            #np_string = opp.matToNumpyString(datumsPtr)     # <--- Fine, it works!
            #list_arr = ast.literal_eval(np_string)
            #np_array = np.array(list_arr, dtype=np.uint8)
            
            channels = 3
            np_array = np.ndarray((width,height,channels), dtype=np.uint8)
            for w in width:
                    for h in height:
                        for c in channels:
                            np_array[w][h][c] = opp.getElement(w,h,c,datumsPtr)

            cv.imshow("User worker GUI", np_array)  
            cv.waitKey(1) # It displays the image and sleeps at least 1 ms (it usually sleeps ~5-10 msec to display the image)
        else:
            print "Nullptr or empty datumsPtr found."

def getDatum(datumsPtr):
    return opp.datum_frompointer(opp.datumsPtr_at(datumsPtr)).__getitem__(0)

def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]