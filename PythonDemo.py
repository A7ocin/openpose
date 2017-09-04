from gflags import *
from glog import *
from google.apputils import app
import sys
import cv2 as cv
import time

sys.path.insert(0, 'windows/OpenPosePython')

import UserClasses
import OpenPosePython as opp

DEFINE_string("image_dir",                "examples/media/",      "Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).")
DEFINE_string("resolution",               "1280x720",     "The image resolution (display and output). Use \"-1x-1\" to force the program to use the default images resolution.")

def main(argv):
    # User processing
    userInputClass = UserClasses.UserInputClass(FLAGS.image_dir)
    userOutputClass = UserClasses.UserOutputClass()

    start = time.time()
    print "Starting pose estimation demo."

    while not userInputClass.isFinished():
        datumsPtr = opp.new_datumsPtr()
        inputImage = cv.imread(userInputClass.nextImage())
        
        if not userInputClass.createDatum(datumsPtr, inputImage, FLAGS.resolution):
                break
        if not opp.openPosePython(datumsPtr):
            print "Wrapper Error"
        
        outputImage = userOutputClass.getProcessedImage(datumsPtr, str(FLAGS.resolution))
        cv.imshow("User worker GUI", outputImage)  
        cv.waitKey(1) # It displays the image and sleeps at least 1 ms (it usually sleeps ~5-10 msec to display the image)
    
    end = time.time()
    print "Real-time pose estimation demo successfully finished. Total time: " + str(end - start) + "seconds."

if __name__ == '__main__':
    app.run()