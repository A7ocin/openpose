#include "OpenPosePython.h"
#include <typeinfo>
#include <chrono>
#include <thread>

using namespace std;
using namespace op;

// See all the available parameter options withe the `--help` flag. E.g. `./build/examples/openpose/openpose.bin --help`.
// Note: This command will show you flags for other unnecessary 3rdparty files. Check only the flags for the OpenPose
// executable. E.g. for `openpose.bin`, look for `Flags from examples/openpose/openpose.cpp:`.
// Producer
DEFINE_string(image_dir, "examples/media/", "Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).");


// Configure OpenPose
op::Wrapper<std::vector<op::Datum>> opWrapper{ op::ThreadManagerMode::Asynchronous };
std::shared_ptr<std::vector<op::Datum>> datumsPtr;

bool openPosePython(std::shared_ptr<std::vector<op::Datum>> datumToProcess)
{
	bool value = false;

	if (datumToProcess != nullptr)
	{
		auto successfullyEmplaced = opWrapper.waitAndEmplace(datumToProcess);
		// Pop frame
		std::shared_ptr<std::vector<op::Datum>> datumProcessed;
		if (successfullyEmplaced && opWrapper.waitAndPop(datumProcessed)) {
			value = true;
		}
		else {
			value = false;
		}
	}

	return value;
}

void configure() {
	// Pose configuration (use WrapperStructPose{} for default and recommended configuration)
	op::WrapperStructPose wrapperStructPose{};
	wrapperStructPose.renderMode = op::RenderMode::Gpu;
	// Configure wrapper
	opWrapper.configure(wrapperStructPose);

	opWrapper.start();
}

void stop() {
	opWrapper.stop();
}

std::shared_ptr<std::vector<op::Datum>> new_datumsPtr() {
	datumsPtr = std::make_shared<std::vector<op::Datum>>();
	return datumsPtr;
}

op::Datum datumsPtr_at(std::shared_ptr<std::vector<op::Datum>> dptr) {
	return dptr->at(0);
}

std::vector<uchar> mat_at(std::shared_ptr<std::vector<op::Datum>> dptr) {
	cv::Mat mat = dptr->at(0).cvOutputData;
	std::vector<uchar> array;
	if (mat.isContinuous()) {
		array.assign(mat.datastart, mat.dataend);
	}
	else {
		for (int i = 0; i < mat.rows; ++i) {
			array.insert(array.end(), mat.ptr(i), mat.ptr(i) + mat.cols);
		}
	}
	cout << mat.size << endl;
	return array;
}

bool datumsPtr_empty(std::shared_ptr<std::vector<op::Datum>> dptr) {
	return dptr->empty();
}

void emplaceBack(std::shared_ptr<std::vector<op::Datum>> dptr) {
	dptr->emplace_back();
}

int getElement(int h, int w, int c, std::shared_ptr<std::vector<op::Datum>> dptr) {
	//std::cout << "Size: " << dptr->at(0).cvOutputData.size() << std::endl;
	return dptr->at(0).cvOutputData.at<cv::Vec3b>(h,w)[c];
}

void setElement(int h, int w, int c, std::shared_ptr<std::vector<op::Datum>> dptr, int value, int width, int height) {
	if (dptr->at(0).cvInputData.empty()) {
		dptr->at(0).cvInputData = cv::Mat(height, width, CV_8UC3, double(0));
	}
	dptr->at(0).cvInputData.at<cv::Vec3b>(h, w)[c] = (unsigned char)value;
}

void setInputMat(std::shared_ptr<std::vector<op::Datum>> dptr, std::vector<int> np_image, std::string resolution) {
	// How to access np_image? --> [height][width][channel]

	size_t pos = 0;

	std::string delimiter = "x";
	pos = resolution.find(delimiter);
	int width = stoi(resolution.substr(0, pos));
	resolution.erase(0, resolution.find(delimiter) + delimiter.length());
	pos = resolution.find(delimiter);
	int height = stoi(resolution.substr(0, pos));

	const int channels = 3;
	const int totalSize = width * height;

	uchar* rawData = new uchar[921600 * 3];

	for (int i = 0; i < np_image.size(); i++) {
		rawData[i] = (uchar)np_image[i];
	}

	cv::Mat* out = new cv::Mat(height, width, CV_8UC3, rawData);

	datumsPtr->at(0).cvInputData = *out;
}