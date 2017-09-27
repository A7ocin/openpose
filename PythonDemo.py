from gflags import *
from glog import *
from google.apputils import app
import sys
import cv2 as cv
import time

sys.path.insert(0, 'windows/OpenPosePython')

import UserClassesCython as UserClasses
import OpenPosePython as opp

DEFINE_string("image_dir",                "examples/media/",      "Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).")
DEFINE_string("resolution",               "1280x720",     "The image resolution (display and output). Use \"-1x-1\" to force the program to use the default images resolution.")

def main(argv):
    """
    Create and initialize user input and output classes
    """
    userInputClass, userOutputClass = UserClasses.openPoseInit(FLAGS)
    numImages = 0

    start = time.time()
    print "Starting pose estimation demo."
    
    while not userInputClass.isFinished():
        datumsPtr = opp.new_datumsPtr()
        inputImage = cv.imread(userInputClass.nextImage())
        
        if not userInputClass.createDatum(datumsPtr, inputImage, FLAGS.resolution):
            break

        if not opp.openPosePython(datumsPtr):
            print "Wrapper Error"
            break
        
        outputImage = userOutputClass.getProcessedImage(datumsPtr, FLAGS.resolution)
        numImages += 1
        fps = "FPS: " + str(round((numImages/(time.time()-start)),2))
        print fps
        cv.putText(outputImage, fps,(10,60), cv.FONT_HERSHEY_DUPLEX, 2, (0,255,255), 4, cv.LINE_AA)
        cv.imshow("User worker GUI", outputImage)  
        cv.waitKey(1)
        
    print "Stopping OpenPose..."
    end = time.time()
    opp.stop()
    print "Real-time pose estimation demo successfully finished. Total time: " + str(end - start) + "seconds."

if __name__ == '__main__':
    app.run()
