#pragma once

// ------------------------- OpenPose Library Tutorial - Thread - Example 1 - Asynchronous -------------------------
// C++ std library dependencies
#include <chrono> // `std::chrono::` functions and classes, e.g. std::chrono::milliseconds
#include <thread> // std::this_thread
// Other 3rdparty dependencies
#include <gflags/gflags.h> // DEFINE_bool, DEFINE_int32, DEFINE_int64, DEFINE_uint64, DEFINE_double, DEFINE_string
#include <glog/logging.h> // google::InitGoogleLogging

// OpenPose dependencies
#include <openpose/headers.hpp>


//class UserInputClass
//{
//public:
//	UserInputClass(const std::string& directoryPath);
//
//	std::shared_ptr<std::vector<op::Datum>> UserInputClass::createDatum(std::shared_ptr<std::vector<op::Datum>> datumsPtr);
//
//	bool isFinished() const;
//
//	std::shared_ptr<std::vector<op::Datum>> datumsPtr;
//
//private:
//	const std::vector<std::string> mImageFiles;
//	unsigned long long mCounter;
//	bool mClosed;
//};

//class UserOutputClass
//{
//public:
//	void display(const std::shared_ptr<std::vector<op::Datum>>& datumsPtr);
//};

bool openPosePython(std::shared_ptr<std::vector<op::Datum>> datumToProcess);
void configure();
void stop();

void setMat(std::shared_ptr<std::vector<op::Datum>> dptr, uchar* matData);

std::shared_ptr<std::vector<op::Datum>> new_datumsPtr();

int get(std::shared_ptr<std::vector<op::Datum>> dptr);
op::Datum datumsPtr_at(std::shared_ptr<std::vector<op::Datum>> dptr);
std::vector<uchar> mat_at(std::shared_ptr<std::vector<op::Datum>> dptr);
bool datumsPtr_empty(std::shared_ptr<std::vector<op::Datum>> dptr);
float* get_pose_keypoints(std::shared_ptr<std::vector<op::Datum>> dptr);
void emplaceBack(std::shared_ptr<std::vector<op::Datum>> dptr);
void setCvInputData(std::shared_ptr<std::vector<op::Datum>> dptr, std::string image);
void setInput(std::shared_ptr<std::vector<op::Datum>> dptr, std::vector<std::vector<int>> np_image, std::string resolution);
std::string matToNumpyString(std::shared_ptr<std::vector<op::Datum>> dptr);
int getElement(int w, int h, int c, std::shared_ptr<std::vector<op::Datum>> dptr);
void setElement(int h, int w, int c, std::shared_ptr<std::vector<op::Datum>> dptr, int value, int width, int height);
void initInput(std::shared_ptr<std::vector<op::Datum>> dptr);
void show(std::string name, std::shared_ptr<std::vector<op::Datum>> dptr);
std::vector<float> matToArray(cv::Mat mat);

void test();
void setCppInput(std::shared_ptr<std::vector<op::Datum>> dptr, std::vector<std::vector<int>> np_image1, std::vector<std::vector<int>> np_image2, std::vector<std::vector<int>> np_image3, std::string resolution);
void setInputMat(std::shared_ptr<std::vector<op::Datum>> dptr, std::vector<int> np_image, std::string resolution);