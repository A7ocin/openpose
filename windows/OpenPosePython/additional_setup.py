# Cython compile instructions

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

# Use python setup.py build_ext --inplace
# to compile

setup(
  name = "additionalcython",
  ext_modules = cythonize(Extension('cy_additional',
									sources=['cy_additional.pyx'],
									include_dirs=[
												".",
												"../../include",
												"../../3rdparty/windows/opencv/include",
												"../../3rdparty/windows/caffe/include",
												"../../3rdparty/windows/caffe/include2",
												"../../3rdparty/windows/caffe3rdparty/include",
												"../../3rdparty/windows/caffe3rdparty/include/boost-1_61",
												"$(CUDA_PATH_V8_0)\include"
												],
									library_dirs=[
													"../../3rdparty/windows/opencv/x64/vc14/lib",
													"../x64/Release"
													],
									libraries=["opencv_world310", "OpenPose"]
									)
						)
)