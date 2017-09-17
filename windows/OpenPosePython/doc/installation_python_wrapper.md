Instructions: 
0) Install SWIG as described here http://www.swig.org/Doc1.3/Windows.html#Windows_installation
1) Build OpenPose
2) Remove OP_API in datum.hpp and save the file
3) Compile the project OpenPosePython in VS, then restore OP_API
4) Add these dlls to the OpenPosePython folder (see dlls.png)
5a) If you don't have Cython --> in PythonDemo.py replace import UserClassesCython as UserClasses with import UserClasses
5b) If you have Cython, execute setup.py as follows: python setup.py build_ext --inplace
6) Navigate to the OpenPose root folder and from cmd: �python PythonDemo.py�
