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

bool openPosePython(std::shared_ptr<std::vector<op::Datum>> datumToProcess);
void configure();
void stop();
std::shared_ptr<std::vector<op::Datum>> new_datumsPtr();
op::Datum datumsPtr_at(std::shared_ptr<std::vector<op::Datum>> dptr);
std::vector<uchar> mat_at(std::shared_ptr<std::vector<op::Datum>> dptr);
bool datumsPtr_empty(std::shared_ptr<std::vector<op::Datum>> dptr);
void emplaceBack(std::shared_ptr<std::vector<op::Datum>> dptr);
int getElement(int w, int h, int c, std::shared_ptr<std::vector<op::Datum>> dptr);
void setElement(int h, int w, int c, std::shared_ptr<std::vector<op::Datum>> dptr, int value, int width, int height);
void setInputMat(std::shared_ptr<std::vector<op::Datum>> dptr, std::vector<int> np_image, std::string resolution);