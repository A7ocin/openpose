//python_wrapper.i
 
%module python_wrapper
 
%{
#define SWIG_PYTHON_INTERPRETER_NO_DEBUG
#if _DEBUG
  #define _DEBUG_IS_ENABLED
  #undef _DEBUG
#endif
#include "pyconfig.h"
#if defined(_DEBUG_IS_ENABLED)
  #define _DEBUG
#endif

#include "python_wrapper.h"
#include "..\..\include\openpose\headers.hpp"
using namespace std;
using namespace op;

extern int openPoseDemo();
extern int start(std::string image_dir, std::string video, int camera, std::string camera_resolution, double camera_fps, bool no_display, bool no_gui_verbose);
extern int main(int argc, char *argv[]);
%}

%typemap(in) (int argc, char *argv[]) {
  int i;
  if (!PyList_Check($input)) {
    PyErr_SetString(PyExc_ValueError, "Expecting a list");
    return NULL;
  }
  $1 = PyList_Size($input);
  $2 = (char **) malloc(($1+1)*sizeof(char *));
  for (i = 0; i < $1; i++) {
    PyObject *s = PyList_GetItem($input,i);
    if (!PyString_Check(s)) {
        free($2);
        PyErr_SetString(PyExc_ValueError, "List items must be strings");
        return NULL;
    }
    $2[i] = PyString_AsString(s);
  }
  $2[i] = 0;
}
 
%include <std_string.i>
%include "python_wrapper.h"
%include "..\..\include\openpose\headers.hpp"

extern int openPoseDemo();
extern int start(std::string image_dir, std::string video, int camera, std::string camera_resolution, double camera_fps, bool no_display, bool no_gui_verbose);
extern int main(int argc, char *argv[]);