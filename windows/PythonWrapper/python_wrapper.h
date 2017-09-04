#pragma once

#include <chrono> // `std::chrono::` functions and classes, e.g. std::chrono::milliseconds
#include <string>
#include <thread> // std::this_thread
#include <vector>
#include <iostream>

#include <openpose\headers.hpp>

int openPoseDemo();
int start(std::string image_dir, std::string video, int camera, std::string camera_resolution, double camera_fps, bool no_display, bool no_gui_verbose);
int main(int argc, char *argv[]);

