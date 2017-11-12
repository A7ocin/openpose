//1_user_asynchronous_output.i
 
%module PyOPUAO
%include <stl.i>
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

#include "1_user_asynchronous_output.h"
#include "..\..\include\openpose\headers.hpp"
#include "..\..\include\openpose\core\datum.hpp"
#include "..\..\include\openpose\core\array.hpp"
#include "..\..\3rdparty\windows\opencv\include\opencv2\core\mat.hpp"
using namespace std;
using namespace op;

extern int PyOP();

extern std::shared_ptr<std::vector<op::Datum>> initialize(int FLAGS_logging_level, std::string FLAGS_output_resolution,
	std::string FLAGS_net_resolution, std::string FLAGS_face_net_resolution, 
	std::string FLAGS_hand_net_resolution, std::string FLAGS_image_dir,
	std::string FLAGS_video, std::string FLAGS_ip_camera, int FLAGS_camera,
	std::string FLAGS_camera_resolution, double FLAGS_camera_fps, std::string FLAGS_model_pose,
	int FLAGS_keypoint_scale, bool FLAGS_heatmaps_add_parts, bool FLAGS_heatmaps_add_bkg,
	bool FLAGS_heatmaps_add_PAFs, int FLAGS_heatmaps_scale);

extern op::Datum getDatum();
extern void stop();

%}
 
%include "1_user_asynchronous_output.h"
%include "..\..\include\openpose\headers.hpp"
%include "..\..\include\openpose\core\datum.hpp"
%include "..\..\include\openpose\core\array.hpp"

%array_class(op::Datum, datum);
%array_class(cv::Mat, mat);
%array_class(std::vector<uchar>, ucharMat);


namespacec std{
	%template(DatumVec) vector<op::Datum>;
}

%template(DatumsPtr) std::shared_ptr<std::vector<op::Datum>>;
%template(oparrayf) op::Array<float>;

%array_class(cv::Mat, Mat);

extern int PyOP();

extern std::shared_ptr<std::vector<op::Datum>> initialize(int FLAGS_logging_level, std::string FLAGS_output_resolution,
	std::string FLAGS_net_resolution, std::string FLAGS_face_net_resolution, 
	std::string FLAGS_hand_net_resolution, std::string FLAGS_image_dir,
	std::string FLAGS_video, std::string FLAGS_ip_camera, int FLAGS_camera,
	std::string FLAGS_camera_resolution, double FLAGS_camera_fps, std::string FLAGS_model_pose,
	int FLAGS_keypoint_scale, bool FLAGS_heatmaps_add_parts, bool FLAGS_heatmaps_add_bkg,
	bool FLAGS_heatmaps_add_PAFs, int FLAGS_heatmaps_scale);

extern op::Datum getDatum();
extern void stop();

