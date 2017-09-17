//OpenPosePython.i
 
%module OpenPosePython
%include <std_string.i>
%include <std_vector.i>
%include <std_shared_ptr.i>
%include <carrays.i>
%include "cpointer.i"

namespace std{
	%template(IntVector) vector<int>;
	%template(IntVectorVector) vector<vector<int>>;
	%template(IntVectorVectorVector) vector<vector<vector<int>>>;

	%template(NumpyMatrix) vector<vector<vector<int,allocator<int >>,allocator<vector<int,allocator<int>>>>,allocator<vector<vector<int,allocator<int>>, allocator<vector<int, allocator<int>>>>>>;
}

%shared_ptr(std::vector<op::Datum>)
 
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

#include "OpenPosePython.h"
#include "..\..\include\openpose\headers.hpp"
#include "..\..\include\openpose\core\datum.hpp"
#include "..\..\3rdparty\windows\opencv\include\opencv2\core\mat.hpp"
using namespace std;
using namespace op;

extern bool openPosePython(std::shared_ptr<std::vector<op::Datum>> datumToProcess);
extern void configure();
extern void stop();
extern void setMat(std::shared_ptr<std::vector<op::Datum>> dptr, uchar* matData);

extern std::shared_ptr<std::vector<op::Datum>> new_datumsPtr();
extern int get(std::shared_ptr<std::vector<op::Datum>> dptr);
extern op::Datum datumsPtr_at(std::shared_ptr<std::vector<op::Datum>> dptr);
extern std::vector<uchar> mat_at(std::shared_ptr<std::vector<op::Datum>> dptr);
extern bool datumsPtr_empty(std::shared_ptr<std::vector<op::Datum>> dptr);
extern float* get_pose_keypoints(std::shared_ptr<std::vector<op::Datum>> dptr);
extern void emplaceBack(std::shared_ptr<std::vector<op::Datum>> dptr);
extern void setCvInputData(std::shared_ptr<std::vector<op::Datum>> dptr, std::string image);
extern void setInput(std::shared_ptr<std::vector<op::Datum>> dptr, std::vector<std::vector<int>> np_image, std::string resolution);
extern std::string matToNumpyString(std::shared_ptr<std::vector<op::Datum>> dptr);
extern int getElement(int w, int h, int c, std::shared_ptr<std::vector<op::Datum>> dptr);
extern void setElement(int h, int w, int c, std::shared_ptr<std::vector<op::Datum>> dptr, int value, int width, int height);
extern void initInput(std::shared_ptr<std::vector<op::Datum>> dptr);
extern void show(std::string name, std::shared_ptr<std::vector<op::Datum>> dptr);
extern std::vector<float> matToArray(cv::Mat mat);

extern void test();
%}
 
%include "OpenPosePython.h"
%include "..\..\include\openpose\headers.hpp"
%include "..\..\include\openpose\core\datum.hpp"

%array_class(op::Datum, datum);
%array_class(cv::Mat, mat);
%array_class(std::vector<uchar>, ucharMat);

namespacec std{
	%template(DatumVec) vector<op::Datum>;
}

%template(DatumsPtr) std::shared_ptr<std::vector<op::Datum>>;

%array_class(cv::Mat, Mat);

extern bool openPosePython(std::shared_ptr<std::vector<op::Datum>> datumToProcess);
extern void configure();
extern void stop();
extern void setMat(std::shared_ptr<std::vector<op::Datum>> dptr, uchar* matData);

extern std::shared_ptr<std::vector<op::Datum>> new_datumsPtr();
extern int get(std::shared_ptr<std::vector<op::Datum>> dptr);
extern op::Datum datumsPtr_at(std::shared_ptr<std::vector<op::Datum>> dptr);
extern std::vector<uchar> mat_at(std::shared_ptr<std::vector<op::Datum>> dptr);
extern bool datumsPtr_empty(std::shared_ptr<std::vector<op::Datum>> dptr);
extern float* get_pose_keypoints(std::shared_ptr<std::vector<op::Datum>> dptr);
extern void emplaceBack(std::shared_ptr<std::vector<op::Datum>> dptr);
extern void setCvInputData(std::shared_ptr<std::vector<op::Datum>> dptr, std::string image);
extern void setInput(std::shared_ptr<std::vector<op::Datum>> dptr, std::vector<std::vector<int>> np_image, std::string resolution);
extern std::string matToNumpyString(std::shared_ptr<std::vector<op::Datum>> dptr);
extern int getElement(int w, int h, int c, std::shared_ptr<std::vector<op::Datum>> dptr);
extern void setElement(int h, int w, int c, std::shared_ptr<std::vector<op::Datum>> dptr, int value, int width, int height);
extern void initInput(std::shared_ptr<std::vector<op::Datum>> dptr);
extern void show(std::string name, std::shared_ptr<std::vector<op::Datum>> dptr);
extern std::vector<float> matToArray(cv::Mat mat);

extern void test();