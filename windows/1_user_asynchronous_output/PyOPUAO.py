# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_PyOPUAO')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_PyOPUAO')
    _PyOPUAO = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_PyOPUAO', [dirname(__file__)])
        except ImportError:
            import _PyOPUAO
            return _PyOPUAO
        try:
            _mod = imp.load_module('_PyOPUAO', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _PyOPUAO = swig_import_helper()
    del swig_import_helper
else:
    import _PyOPUAO
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _PyOPUAO.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _PyOPUAO.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _PyOPUAO.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _PyOPUAO.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _PyOPUAO.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _PyOPUAO.SwigPyIterator_equal(self, x)

    def copy(self):
        return _PyOPUAO.SwigPyIterator_copy(self)

    def next(self):
        return _PyOPUAO.SwigPyIterator_next(self)

    def __next__(self):
        return _PyOPUAO.SwigPyIterator___next__(self)

    def previous(self):
        return _PyOPUAO.SwigPyIterator_previous(self)

    def advance(self, n):
        return _PyOPUAO.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _PyOPUAO.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _PyOPUAO.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _PyOPUAO.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _PyOPUAO.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _PyOPUAO.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _PyOPUAO.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _PyOPUAO.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _PyOPUAO.SHARED_PTR_DISOWN
class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _PyOPUAO.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _PyOPUAO.IntVector___nonzero__(self)

    def __bool__(self):
        return _PyOPUAO.IntVector___bool__(self)

    def __len__(self):
        return _PyOPUAO.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _PyOPUAO.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _PyOPUAO.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _PyOPUAO.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _PyOPUAO.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _PyOPUAO.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _PyOPUAO.IntVector___setitem__(self, *args)

    def pop(self):
        return _PyOPUAO.IntVector_pop(self)

    def append(self, x):
        return _PyOPUAO.IntVector_append(self, x)

    def empty(self):
        return _PyOPUAO.IntVector_empty(self)

    def size(self):
        return _PyOPUAO.IntVector_size(self)

    def swap(self, v):
        return _PyOPUAO.IntVector_swap(self, v)

    def begin(self):
        return _PyOPUAO.IntVector_begin(self)

    def end(self):
        return _PyOPUAO.IntVector_end(self)

    def rbegin(self):
        return _PyOPUAO.IntVector_rbegin(self)

    def rend(self):
        return _PyOPUAO.IntVector_rend(self)

    def clear(self):
        return _PyOPUAO.IntVector_clear(self)

    def get_allocator(self):
        return _PyOPUAO.IntVector_get_allocator(self)

    def pop_back(self):
        return _PyOPUAO.IntVector_pop_back(self)

    def erase(self, *args):
        return _PyOPUAO.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _PyOPUAO.new_IntVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _PyOPUAO.IntVector_push_back(self, x)

    def front(self):
        return _PyOPUAO.IntVector_front(self)

    def back(self):
        return _PyOPUAO.IntVector_back(self)

    def assign(self, n, x):
        return _PyOPUAO.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _PyOPUAO.IntVector_resize(self, *args)

    def insert(self, *args):
        return _PyOPUAO.IntVector_insert(self, *args)

    def reserve(self, n):
        return _PyOPUAO.IntVector_reserve(self, n)

    def capacity(self):
        return _PyOPUAO.IntVector_capacity(self)
    __swig_destroy__ = _PyOPUAO.delete_IntVector
    __del__ = lambda self: None
IntVector_swigregister = _PyOPUAO.IntVector_swigregister
IntVector_swigregister(IntVector)

class IntVectorVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVectorVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVectorVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _PyOPUAO.IntVectorVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _PyOPUAO.IntVectorVector___nonzero__(self)

    def __bool__(self):
        return _PyOPUAO.IntVectorVector___bool__(self)

    def __len__(self):
        return _PyOPUAO.IntVectorVector___len__(self)

    def __getslice__(self, i, j):
        return _PyOPUAO.IntVectorVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _PyOPUAO.IntVectorVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _PyOPUAO.IntVectorVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _PyOPUAO.IntVectorVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _PyOPUAO.IntVectorVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _PyOPUAO.IntVectorVector___setitem__(self, *args)

    def pop(self):
        return _PyOPUAO.IntVectorVector_pop(self)

    def append(self, x):
        return _PyOPUAO.IntVectorVector_append(self, x)

    def empty(self):
        return _PyOPUAO.IntVectorVector_empty(self)

    def size(self):
        return _PyOPUAO.IntVectorVector_size(self)

    def swap(self, v):
        return _PyOPUAO.IntVectorVector_swap(self, v)

    def begin(self):
        return _PyOPUAO.IntVectorVector_begin(self)

    def end(self):
        return _PyOPUAO.IntVectorVector_end(self)

    def rbegin(self):
        return _PyOPUAO.IntVectorVector_rbegin(self)

    def rend(self):
        return _PyOPUAO.IntVectorVector_rend(self)

    def clear(self):
        return _PyOPUAO.IntVectorVector_clear(self)

    def get_allocator(self):
        return _PyOPUAO.IntVectorVector_get_allocator(self)

    def pop_back(self):
        return _PyOPUAO.IntVectorVector_pop_back(self)

    def erase(self, *args):
        return _PyOPUAO.IntVectorVector_erase(self, *args)

    def __init__(self, *args):
        this = _PyOPUAO.new_IntVectorVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _PyOPUAO.IntVectorVector_push_back(self, x)

    def front(self):
        return _PyOPUAO.IntVectorVector_front(self)

    def back(self):
        return _PyOPUAO.IntVectorVector_back(self)

    def assign(self, n, x):
        return _PyOPUAO.IntVectorVector_assign(self, n, x)

    def resize(self, *args):
        return _PyOPUAO.IntVectorVector_resize(self, *args)

    def insert(self, *args):
        return _PyOPUAO.IntVectorVector_insert(self, *args)

    def reserve(self, n):
        return _PyOPUAO.IntVectorVector_reserve(self, n)

    def capacity(self):
        return _PyOPUAO.IntVectorVector_capacity(self)
    __swig_destroy__ = _PyOPUAO.delete_IntVectorVector
    __del__ = lambda self: None
IntVectorVector_swigregister = _PyOPUAO.IntVectorVector_swigregister
IntVectorVector_swigregister(IntVectorVector)

class IntVectorVectorVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVectorVectorVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVectorVectorVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _PyOPUAO.IntVectorVectorVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _PyOPUAO.IntVectorVectorVector___nonzero__(self)

    def __bool__(self):
        return _PyOPUAO.IntVectorVectorVector___bool__(self)

    def __len__(self):
        return _PyOPUAO.IntVectorVectorVector___len__(self)

    def __getslice__(self, i, j):
        return _PyOPUAO.IntVectorVectorVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _PyOPUAO.IntVectorVectorVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _PyOPUAO.IntVectorVectorVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _PyOPUAO.IntVectorVectorVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _PyOPUAO.IntVectorVectorVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _PyOPUAO.IntVectorVectorVector___setitem__(self, *args)

    def pop(self):
        return _PyOPUAO.IntVectorVectorVector_pop(self)

    def append(self, x):
        return _PyOPUAO.IntVectorVectorVector_append(self, x)

    def empty(self):
        return _PyOPUAO.IntVectorVectorVector_empty(self)

    def size(self):
        return _PyOPUAO.IntVectorVectorVector_size(self)

    def swap(self, v):
        return _PyOPUAO.IntVectorVectorVector_swap(self, v)

    def begin(self):
        return _PyOPUAO.IntVectorVectorVector_begin(self)

    def end(self):
        return _PyOPUAO.IntVectorVectorVector_end(self)

    def rbegin(self):
        return _PyOPUAO.IntVectorVectorVector_rbegin(self)

    def rend(self):
        return _PyOPUAO.IntVectorVectorVector_rend(self)

    def clear(self):
        return _PyOPUAO.IntVectorVectorVector_clear(self)

    def get_allocator(self):
        return _PyOPUAO.IntVectorVectorVector_get_allocator(self)

    def pop_back(self):
        return _PyOPUAO.IntVectorVectorVector_pop_back(self)

    def erase(self, *args):
        return _PyOPUAO.IntVectorVectorVector_erase(self, *args)

    def __init__(self, *args):
        this = _PyOPUAO.new_IntVectorVectorVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _PyOPUAO.IntVectorVectorVector_push_back(self, x)

    def front(self):
        return _PyOPUAO.IntVectorVectorVector_front(self)

    def back(self):
        return _PyOPUAO.IntVectorVectorVector_back(self)

    def assign(self, n, x):
        return _PyOPUAO.IntVectorVectorVector_assign(self, n, x)

    def resize(self, *args):
        return _PyOPUAO.IntVectorVectorVector_resize(self, *args)

    def insert(self, *args):
        return _PyOPUAO.IntVectorVectorVector_insert(self, *args)

    def reserve(self, n):
        return _PyOPUAO.IntVectorVectorVector_reserve(self, n)

    def capacity(self):
        return _PyOPUAO.IntVectorVectorVector_capacity(self)
    __swig_destroy__ = _PyOPUAO.delete_IntVectorVectorVector
    __del__ = lambda self: None
IntVectorVectorVector_swigregister = _PyOPUAO.IntVectorVectorVector_swigregister
IntVectorVectorVector_swigregister(IntVectorVectorVector)

class NumpyMatrix(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NumpyMatrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NumpyMatrix, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _PyOPUAO.NumpyMatrix_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _PyOPUAO.NumpyMatrix___nonzero__(self)

    def __bool__(self):
        return _PyOPUAO.NumpyMatrix___bool__(self)

    def __len__(self):
        return _PyOPUAO.NumpyMatrix___len__(self)

    def __getslice__(self, i, j):
        return _PyOPUAO.NumpyMatrix___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _PyOPUAO.NumpyMatrix___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _PyOPUAO.NumpyMatrix___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _PyOPUAO.NumpyMatrix___delitem__(self, *args)

    def __getitem__(self, *args):
        return _PyOPUAO.NumpyMatrix___getitem__(self, *args)

    def __setitem__(self, *args):
        return _PyOPUAO.NumpyMatrix___setitem__(self, *args)

    def pop(self):
        return _PyOPUAO.NumpyMatrix_pop(self)

    def append(self, x):
        return _PyOPUAO.NumpyMatrix_append(self, x)

    def empty(self):
        return _PyOPUAO.NumpyMatrix_empty(self)

    def size(self):
        return _PyOPUAO.NumpyMatrix_size(self)

    def swap(self, v):
        return _PyOPUAO.NumpyMatrix_swap(self, v)

    def begin(self):
        return _PyOPUAO.NumpyMatrix_begin(self)

    def end(self):
        return _PyOPUAO.NumpyMatrix_end(self)

    def rbegin(self):
        return _PyOPUAO.NumpyMatrix_rbegin(self)

    def rend(self):
        return _PyOPUAO.NumpyMatrix_rend(self)

    def clear(self):
        return _PyOPUAO.NumpyMatrix_clear(self)

    def get_allocator(self):
        return _PyOPUAO.NumpyMatrix_get_allocator(self)

    def pop_back(self):
        return _PyOPUAO.NumpyMatrix_pop_back(self)

    def erase(self, *args):
        return _PyOPUAO.NumpyMatrix_erase(self, *args)

    def __init__(self, *args):
        this = _PyOPUAO.new_NumpyMatrix(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _PyOPUAO.NumpyMatrix_push_back(self, x)

    def front(self):
        return _PyOPUAO.NumpyMatrix_front(self)

    def back(self):
        return _PyOPUAO.NumpyMatrix_back(self)

    def assign(self, n, x):
        return _PyOPUAO.NumpyMatrix_assign(self, n, x)

    def resize(self, *args):
        return _PyOPUAO.NumpyMatrix_resize(self, *args)

    def insert(self, *args):
        return _PyOPUAO.NumpyMatrix_insert(self, *args)

    def reserve(self, n):
        return _PyOPUAO.NumpyMatrix_reserve(self, n)

    def capacity(self):
        return _PyOPUAO.NumpyMatrix_capacity(self)
    __swig_destroy__ = _PyOPUAO.delete_NumpyMatrix
    __del__ = lambda self: None
NumpyMatrix_swigregister = _PyOPUAO.NumpyMatrix_swigregister
NumpyMatrix_swigregister(NumpyMatrix)

class Datum(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Datum, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Datum, name)
    __repr__ = _swig_repr
    __swig_setmethods__["id"] = _PyOPUAO.Datum_id_set
    __swig_getmethods__["id"] = _PyOPUAO.Datum_id_get
    if _newclass:
        id = _swig_property(_PyOPUAO.Datum_id_get, _PyOPUAO.Datum_id_set)
    __swig_setmethods__["name"] = _PyOPUAO.Datum_name_set
    __swig_getmethods__["name"] = _PyOPUAO.Datum_name_get
    if _newclass:
        name = _swig_property(_PyOPUAO.Datum_name_get, _PyOPUAO.Datum_name_set)
    __swig_setmethods__["cvInputData"] = _PyOPUAO.Datum_cvInputData_set
    __swig_getmethods__["cvInputData"] = _PyOPUAO.Datum_cvInputData_get
    if _newclass:
        cvInputData = _swig_property(_PyOPUAO.Datum_cvInputData_get, _PyOPUAO.Datum_cvInputData_set)
    __swig_setmethods__["inputNetData"] = _PyOPUAO.Datum_inputNetData_set
    __swig_getmethods__["inputNetData"] = _PyOPUAO.Datum_inputNetData_get
    if _newclass:
        inputNetData = _swig_property(_PyOPUAO.Datum_inputNetData_get, _PyOPUAO.Datum_inputNetData_set)
    __swig_setmethods__["outputData"] = _PyOPUAO.Datum_outputData_set
    __swig_getmethods__["outputData"] = _PyOPUAO.Datum_outputData_get
    if _newclass:
        outputData = _swig_property(_PyOPUAO.Datum_outputData_get, _PyOPUAO.Datum_outputData_set)
    __swig_setmethods__["cvOutputData"] = _PyOPUAO.Datum_cvOutputData_set
    __swig_getmethods__["cvOutputData"] = _PyOPUAO.Datum_cvOutputData_get
    if _newclass:
        cvOutputData = _swig_property(_PyOPUAO.Datum_cvOutputData_get, _PyOPUAO.Datum_cvOutputData_set)
    __swig_setmethods__["poseKeypoints"] = _PyOPUAO.Datum_poseKeypoints_set
    __swig_getmethods__["poseKeypoints"] = _PyOPUAO.Datum_poseKeypoints_get
    if _newclass:
        poseKeypoints = _swig_property(_PyOPUAO.Datum_poseKeypoints_get, _PyOPUAO.Datum_poseKeypoints_set)
    __swig_setmethods__["poseHeatMaps"] = _PyOPUAO.Datum_poseHeatMaps_set
    __swig_getmethods__["poseHeatMaps"] = _PyOPUAO.Datum_poseHeatMaps_get
    if _newclass:
        poseHeatMaps = _swig_property(_PyOPUAO.Datum_poseHeatMaps_get, _PyOPUAO.Datum_poseHeatMaps_set)
    __swig_setmethods__["faceRectangles"] = _PyOPUAO.Datum_faceRectangles_set
    __swig_getmethods__["faceRectangles"] = _PyOPUAO.Datum_faceRectangles_get
    if _newclass:
        faceRectangles = _swig_property(_PyOPUAO.Datum_faceRectangles_get, _PyOPUAO.Datum_faceRectangles_set)
    __swig_setmethods__["faceKeypoints"] = _PyOPUAO.Datum_faceKeypoints_set
    __swig_getmethods__["faceKeypoints"] = _PyOPUAO.Datum_faceKeypoints_get
    if _newclass:
        faceKeypoints = _swig_property(_PyOPUAO.Datum_faceKeypoints_get, _PyOPUAO.Datum_faceKeypoints_set)
    __swig_setmethods__["faceHeatMaps"] = _PyOPUAO.Datum_faceHeatMaps_set
    __swig_getmethods__["faceHeatMaps"] = _PyOPUAO.Datum_faceHeatMaps_get
    if _newclass:
        faceHeatMaps = _swig_property(_PyOPUAO.Datum_faceHeatMaps_get, _PyOPUAO.Datum_faceHeatMaps_set)
    __swig_setmethods__["handRectangles"] = _PyOPUAO.Datum_handRectangles_set
    __swig_getmethods__["handRectangles"] = _PyOPUAO.Datum_handRectangles_get
    if _newclass:
        handRectangles = _swig_property(_PyOPUAO.Datum_handRectangles_get, _PyOPUAO.Datum_handRectangles_set)
    __swig_setmethods__["handKeypoints"] = _PyOPUAO.Datum_handKeypoints_set
    __swig_getmethods__["handKeypoints"] = _PyOPUAO.Datum_handKeypoints_get
    if _newclass:
        handKeypoints = _swig_property(_PyOPUAO.Datum_handKeypoints_get, _PyOPUAO.Datum_handKeypoints_set)
    __swig_setmethods__["handHeatMaps"] = _PyOPUAO.Datum_handHeatMaps_set
    __swig_getmethods__["handHeatMaps"] = _PyOPUAO.Datum_handHeatMaps_get
    if _newclass:
        handHeatMaps = _swig_property(_PyOPUAO.Datum_handHeatMaps_get, _PyOPUAO.Datum_handHeatMaps_set)
    __swig_setmethods__["scaleInputToNetInputs"] = _PyOPUAO.Datum_scaleInputToNetInputs_set
    __swig_getmethods__["scaleInputToNetInputs"] = _PyOPUAO.Datum_scaleInputToNetInputs_get
    if _newclass:
        scaleInputToNetInputs = _swig_property(_PyOPUAO.Datum_scaleInputToNetInputs_get, _PyOPUAO.Datum_scaleInputToNetInputs_set)
    __swig_setmethods__["netInputSizes"] = _PyOPUAO.Datum_netInputSizes_set
    __swig_getmethods__["netInputSizes"] = _PyOPUAO.Datum_netInputSizes_get
    if _newclass:
        netInputSizes = _swig_property(_PyOPUAO.Datum_netInputSizes_get, _PyOPUAO.Datum_netInputSizes_set)
    __swig_setmethods__["scaleInputToOutput"] = _PyOPUAO.Datum_scaleInputToOutput_set
    __swig_getmethods__["scaleInputToOutput"] = _PyOPUAO.Datum_scaleInputToOutput_get
    if _newclass:
        scaleInputToOutput = _swig_property(_PyOPUAO.Datum_scaleInputToOutput_get, _PyOPUAO.Datum_scaleInputToOutput_set)
    __swig_setmethods__["netOutputSize"] = _PyOPUAO.Datum_netOutputSize_set
    __swig_getmethods__["netOutputSize"] = _PyOPUAO.Datum_netOutputSize_get
    if _newclass:
        netOutputSize = _swig_property(_PyOPUAO.Datum_netOutputSize_get, _PyOPUAO.Datum_netOutputSize_set)
    __swig_setmethods__["scaleNetToOutput"] = _PyOPUAO.Datum_scaleNetToOutput_set
    __swig_getmethods__["scaleNetToOutput"] = _PyOPUAO.Datum_scaleNetToOutput_get
    if _newclass:
        scaleNetToOutput = _swig_property(_PyOPUAO.Datum_scaleNetToOutput_get, _PyOPUAO.Datum_scaleNetToOutput_set)
    __swig_setmethods__["elementRendered"] = _PyOPUAO.Datum_elementRendered_set
    __swig_getmethods__["elementRendered"] = _PyOPUAO.Datum_elementRendered_get
    if _newclass:
        elementRendered = _swig_property(_PyOPUAO.Datum_elementRendered_get, _PyOPUAO.Datum_elementRendered_set)

    def __init__(self, *args):
        this = _PyOPUAO.new_Datum(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _PyOPUAO.delete_Datum
    __del__ = lambda self: None

    def clone(self):
        return _PyOPUAO.Datum_clone(self)

    def __lt__(self, datum):
        return _PyOPUAO.Datum___lt__(self, datum)

    def __gt__(self, datum):
        return _PyOPUAO.Datum___gt__(self, datum)

    def __le__(self, datum):
        return _PyOPUAO.Datum___le__(self, datum)

    def __ge__(self, datum):
        return _PyOPUAO.Datum___ge__(self, datum)

    def __eq__(self, datum):
        return _PyOPUAO.Datum___eq__(self, datum)

    def __ne__(self, datum):
        return _PyOPUAO.Datum___ne__(self, datum)
Datum_swigregister = _PyOPUAO.Datum_swigregister
Datum_swigregister(Datum)

class datum(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, datum, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, datum, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _PyOPUAO.new_datum(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _PyOPUAO.delete_datum
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _PyOPUAO.datum___getitem__(self, index)

    def __setitem__(self, index, value):
        return _PyOPUAO.datum___setitem__(self, index, value)

    def cast(self):
        return _PyOPUAO.datum_cast(self)
    if _newclass:
        frompointer = staticmethod(_PyOPUAO.datum_frompointer)
    else:
        frompointer = _PyOPUAO.datum_frompointer
datum_swigregister = _PyOPUAO.datum_swigregister
datum_swigregister(datum)

def datum_frompointer(t):
    return _PyOPUAO.datum_frompointer(t)
datum_frompointer = _PyOPUAO.datum_frompointer

class mat(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mat, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _PyOPUAO.new_mat(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _PyOPUAO.delete_mat
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _PyOPUAO.mat___getitem__(self, index)

    def __setitem__(self, index, value):
        return _PyOPUAO.mat___setitem__(self, index, value)

    def cast(self):
        return _PyOPUAO.mat_cast(self)
    if _newclass:
        frompointer = staticmethod(_PyOPUAO.mat_frompointer)
    else:
        frompointer = _PyOPUAO.mat_frompointer
mat_swigregister = _PyOPUAO.mat_swigregister
mat_swigregister(mat)

def mat_frompointer(t):
    return _PyOPUAO.mat_frompointer(t)
mat_frompointer = _PyOPUAO.mat_frompointer

class ucharMat(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ucharMat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ucharMat, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _PyOPUAO.new_ucharMat(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _PyOPUAO.delete_ucharMat
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _PyOPUAO.ucharMat___getitem__(self, index)

    def __setitem__(self, index, value):
        return _PyOPUAO.ucharMat___setitem__(self, index, value)

    def cast(self):
        return _PyOPUAO.ucharMat_cast(self)
    if _newclass:
        frompointer = staticmethod(_PyOPUAO.ucharMat_frompointer)
    else:
        frompointer = _PyOPUAO.ucharMat_frompointer
ucharMat_swigregister = _PyOPUAO.ucharMat_swigregister
ucharMat_swigregister(ucharMat)

def ucharMat_frompointer(t):
    return _PyOPUAO.ucharMat_frompointer(t)
ucharMat_frompointer = _PyOPUAO.ucharMat_frompointer

class DatumsPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DatumsPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DatumsPtr, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _PyOPUAO.new_DatumsPtr()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _PyOPUAO.delete_DatumsPtr
    __del__ = lambda self: None
DatumsPtr_swigregister = _PyOPUAO.DatumsPtr_swigregister
DatumsPtr_swigregister(DatumsPtr)

class oparrayf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, oparrayf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, oparrayf, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _PyOPUAO.new_oparrayf(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def clone(self):
        return _PyOPUAO.oparrayf_clone(self)

    def reset(self, *args):
        return _PyOPUAO.oparrayf_reset(self, *args)

    def setFrom(self, cvMat):
        return _PyOPUAO.oparrayf_setFrom(self, cvMat)

    def setTo(self, value):
        return _PyOPUAO.oparrayf_setTo(self, value)

    def empty(self):
        return _PyOPUAO.oparrayf_empty(self)

    def getSize(self, *args):
        return _PyOPUAO.oparrayf_getSize(self, *args)

    def getNumberDimensions(self):
        return _PyOPUAO.oparrayf_getNumberDimensions(self)

    def getVolume(self, *args):
        return _PyOPUAO.oparrayf_getVolume(self, *args)

    def getPtr(self):
        return _PyOPUAO.oparrayf_getPtr(self)

    def getConstPtr(self):
        return _PyOPUAO.oparrayf_getConstPtr(self)

    def getConstCvMat(self):
        return _PyOPUAO.oparrayf_getConstCvMat(self)

    def getCvMat(self):
        return _PyOPUAO.oparrayf_getCvMat(self)

    def at(self, *args):
        return _PyOPUAO.oparrayf_at(self, *args)

    def toString(self):
        return _PyOPUAO.oparrayf_toString(self)
    __swig_destroy__ = _PyOPUAO.delete_oparrayf
    __del__ = lambda self: None
oparrayf_swigregister = _PyOPUAO.oparrayf_swigregister
oparrayf_swigregister(oparrayf)

class Mat(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Mat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Mat, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _PyOPUAO.new_Mat(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _PyOPUAO.delete_Mat
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _PyOPUAO.Mat___getitem__(self, index)

    def __setitem__(self, index, value):
        return _PyOPUAO.Mat___setitem__(self, index, value)

    def cast(self):
        return _PyOPUAO.Mat_cast(self)
    if _newclass:
        frompointer = staticmethod(_PyOPUAO.Mat_frompointer)
    else:
        frompointer = _PyOPUAO.Mat_frompointer
Mat_swigregister = _PyOPUAO.Mat_swigregister
Mat_swigregister(Mat)

def Mat_frompointer(t):
    return _PyOPUAO.Mat_frompointer(t)
Mat_frompointer = _PyOPUAO.Mat_frompointer


def PyOP():
    return _PyOPUAO.PyOP()
PyOP = _PyOPUAO.PyOP

def initialize(FLAGS_logging_level, FLAGS_output_resolution, FLAGS_net_resolution, FLAGS_face_net_resolution, FLAGS_hand_net_resolution, FLAGS_image_dir, FLAGS_video, FLAGS_ip_camera, FLAGS_camera, FLAGS_camera_resolution, FLAGS_camera_fps, FLAGS_model_pose, FLAGS_keypoint_scale, FLAGS_heatmaps_add_parts, FLAGS_heatmaps_add_bkg, FLAGS_heatmaps_add_PAFs, FLAGS_heatmaps_scale):
    return _PyOPUAO.initialize(FLAGS_logging_level, FLAGS_output_resolution, FLAGS_net_resolution, FLAGS_face_net_resolution, FLAGS_hand_net_resolution, FLAGS_image_dir, FLAGS_video, FLAGS_ip_camera, FLAGS_camera, FLAGS_camera_resolution, FLAGS_camera_fps, FLAGS_model_pose, FLAGS_keypoint_scale, FLAGS_heatmaps_add_parts, FLAGS_heatmaps_add_bkg, FLAGS_heatmaps_add_PAFs, FLAGS_heatmaps_scale)
initialize = _PyOPUAO.initialize

def getDatum():
    return _PyOPUAO.getDatum()
getDatum = _PyOPUAO.getDatum

def stop():
    return _PyOPUAO.stop()
stop = _PyOPUAO.stop
# This file is compatible with both classic and new-style classes.

