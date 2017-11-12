#pragma once
// This file should only be used for the user to take specific examples.

// C++ std library dependencies
#include <chrono> // `std::chrono::` functions and classes, e.g. std::chrono::milliseconds
#include <thread> // std::this_thread
#include <iostream>
// Other 3rdparty dependencies
// GFlags: DEFINE_bool, _int32, _int64, _uint64, _double, _string
#include <gflags/gflags.h>
// Allow Google Flags in Ubuntu 14
//#ifndef GFLAGS_GFLAGS_H_
//namespace gflags = google;
//#endif
// OpenPose dependencies
#include <openpose/headers.hpp>

// ------------------------- OpenPose Library Tutorial - Thread - Example 3 - Asynchronous Output -------------------------
// Asynchronous output mode: ideal for fast prototyping when performance is not an issue and user wants to use the output OpenPose format. The user
// simply gets the processed frames from the OpenPose wrapper when he desires to.

// This example shows the user how to use the OpenPose wrapper class:
// 1. Read folder of images / video / webcam
// 2. Extract and render keypoint / heatmap / PAF of that image
// 3. Save the results on disk
// 4. User displays the rendered pose
// Everything in a multi-thread scenario
// In addition to the previous OpenPose modules, we also need to use:
// 1. `core` module:
// For the Array<float> class that the `pose` module needs
// For the Datum struct that the `thread` module sends between the queues
// 2. `utilities` module: for the error & logging functions, i.e. op::error & op::log respectively