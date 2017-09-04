#include "python_wrapper.h"

using namespace std;
using namespace op;

int openPoseDemo()
{
	cout << "It works! " << endl;
	return 0;
}

int start(string image_dir, string video, int camera, string camera_resolution, double camera_fps, bool no_display, bool no_gui_verbose) {
	// Initializing google logging (Caffe uses it for logging)
	google::InitGoogleLogging("openPoseDemo");

	op::log("Starting pose estimation demo.", op::Priority::High);
	const auto timerBegin = std::chrono::high_resolution_clock::now();

	// Applying user defined configuration - Google flags to program variables
	const auto producerSharedPtr = op::flagsToProducer(image_dir, video, camera, camera_resolution, camera_fps);
	op::log("", op::Priority::Low, __LINE__, __FUNCTION__, __FILE__);

	// OpenPose wrapper
	op::log("Configuring OpenPose wrapper.", op::Priority::Low, __LINE__, __FUNCTION__, __FILE__);
	op::Wrapper<std::vector<op::Datum>> opWrapper;
	// Pose configuration (use WrapperStructPose{} for default and recommended configuration)
	op::WrapperStructPose wrapperStructPose{};
	wrapperStructPose.renderMode = op::RenderMode::Gpu;
	// Producer (use default to disable any input)
	const op::WrapperStructInput wrapperStructInput{ producerSharedPtr };
	// Consumer (comment or use default argument to disable any output)
	const op::WrapperStructOutput wrapperStructOutput{ !no_display, !no_gui_verbose };
	// Configure wrapper
	opWrapper.configure(wrapperStructPose, wrapperStructInput, wrapperStructOutput);
	// Set to single-thread running (e.g. for debugging purposes)
	// opWrapper.disableMultiThreading();

	// Start processing
	// Two different ways of running the program on multithread environment
	op::log("Starting thread(s)", op::Priority::High);
	opWrapper.exec();  // It blocks this thread until all threads have finished

					   // Measuring total time
	const auto now = std::chrono::high_resolution_clock::now();
	const auto totalTimeSec = (double)std::chrono::duration_cast<std::chrono::nanoseconds>(now - timerBegin).count() * 1e-9;
	const auto message = "Real-time pose estimation demo successfully finished. Total time: " + std::to_string(totalTimeSec) + " seconds.";
	op::log(message, op::Priority::High);

	return 0;
}

int main(int argc, char *argv[])
{
	// Running openPoseDemo
	cout << to_string(argc) << " " << argv[0] << endl;
	return openPoseDemo();
}
