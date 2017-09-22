# distutils: language = c++
# distutils: sources = AdditionalCython.cpp


from libcpp.vector cimport vector
from libcpp.memory cimport shared_ptr


cdef extern from "../../include/openpose/core/datum.hpp" namespace "op":
    struct Datum:
        pass

cdef extern from "AdditionalCython.h":
  ctypedef shared_ptr[vector[Datum]] DatumsPtr
  cdef cppclass AdditionalCython:
        AdditionalCython() except +
        void printMat(vector[vector[vector[int]]])
        void setElement(vector[vector[vector[int]]])


cdef class PyAdditionalCython:
    cdef AdditionalCython *thisptr
    def __cinit__(self):
        self.thisptr = new AdditionalCython()
    def __dealloc__(self):
        del self.thisptr
    def printMat(self, sv):
        return self.thisptr.printMat(sv)
    def setElement(self, sv):
        return self.thisptr.setElement(sv)