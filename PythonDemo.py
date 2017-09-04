from gflags import *
from glog import *
from google.apputils import app
import sys
import cv2 as cv

sys.path.insert(0, 'windows/OpenPosePython')

import UserClasses
import OpenPosePython as opp

DEFINE_string("image_dir",                "examples/media/",      "Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).");


def main(argv):
    # User processing
    userInputClass = UserClasses.UserInputClass(FLAGS.image_dir)
    userOutputClass = UserClasses.UserOutputClass()

    while not userInputClass.isFinished():
        datumsPtr = opp.new_datumsPtr()
        datumToProcess = userInputClass.createDatum(datumsPtr)          #TODO: write createDatum in Python
        if not datumToProcess:
                break
        #datumProcessed = None
        datum = opp.datumsPtr_at(datumsPtr)
        realDatum = opp.datum_frompointer(datum)
        #realDatum = opp.datum_frompointer(opp.datumsPtr_at(datumsPtr)).__getitem__(0)
        value = opp.openPoseTutorialWrapper1(datumsPtr)
        if value == 0:
            #np_image = opp.datum_frompointer(opp.datumsPtr_at(datumsPtr)).__getitem__(0).cvOutputData;
            #mat_image = cv.fromarray(np_image)
            #cv.imshow("User worker GUI", mat_image)
            userOutputClass.display(datumsPtr)
        else:
            print "Wrapper Error"
        
        

    opp.test()

if __name__ == '__main__':
    app.run()