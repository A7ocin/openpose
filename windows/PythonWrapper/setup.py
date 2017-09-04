#!/usr/bin/env python

"""
setup.py file for SWIG OpenPose Python Wrapper
"""

from distutils.core import setup, Extension


python_wrapper = Extension('_python_wrapper',
							sources=['python_wrapper_wrap.cxx', 'python_wrapper.cpp'],
							swig_opts=['-I..\..\include python_wrapper.i'],
							include_dirs=[
											"../../include", 
											"../../3rdparty/windows/opencv/include",
											"../../3rdparty/windows/caffe/include",
											"../../3rdparty/windows/caffe/include2",
											"../../3rdparty/windows/caffe3rdparty/include",
											"../../3rdparty/windows/caffe3rdparty/include/boost-1_61",
											"C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v8.0/include"
										],
							define_macros=[
											('_CRT_SECURE_NO_WARNINGS',None),
											('BOOST_ALL_NO_LIB',None),
											('CAFFE_VERSION', '1.0.0'),
											('CMAKE_WINDOWS_BUILD',None),
											('GLOG_NO_ABBREVIATED_SEVERITIES',None),
											('GOOGLE_GLOG_DLL_DECL','__declspec(dllimport)'),
											('GOOGLE_GLOG_DLL_DECL_FOR_UNITTESTS','__declspec(dllimport)'),
											('H5_BUILT_AS_DYNAMIC_LIB','1'),
											('USE_CAFFE',None),
											('USE_CUDNN',None),
											('USE_OPENCV',None),
											('USE_LEVELDB',None),
											('USE_LMDB',None),
											('CMAKE_INTDIR',"Release"),
											('NDEBUG',None)
										]
                           )

setup (name = 'python_wrapper',
       version = '0.1',
       author      = "Nicola Garau",
       description = """OpenPose Python wrapper""",
       ext_modules = [python_wrapper],
       py_modules = ["python_wrapper"],
       )