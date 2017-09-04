#include "OpenPosePython.h"

using namespace std;
using namespace op;

// See all the available parameter options withe the `--help` flag. E.g. `./build/examples/openpose/openpose.bin --help`.
// Note: This command will show you flags for other unnecessary 3rdparty files. Check only the flags for the OpenPose
// executable. E.g. for `openpose.bin`, look for `Flags from examples/openpose/openpose.cpp:`.
// Producer
DEFINE_string(image_dir, "examples/media/", "Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).");

bool openPosePython(std::shared_ptr<std::vector<op::Datum>> datumToProcess)
{
	bool value = false;

	// Configure OpenPose
	op::Wrapper<std::vector<op::Datum>> opWrapper{ op::ThreadManagerMode::Asynchronous };
	// Pose configuration (use WrapperStructPose{} for default and recommended configuration)
	op::WrapperStructPose wrapperStructPose{};
	wrapperStructPose.renderMode = op::RenderMode::Gpu;
	// Configure wrapper
	opWrapper.configure(wrapperStructPose);

	opWrapper.start();

	//while (!userInputClass.isFinished())
	//{
		// Push frame
		//auto datumToProcess = userInputClass.createDatum();
		if (datumToProcess != nullptr)
		{
			//cout << "---> " << datumToProcess->at(0).cvInputData << endl;
			auto successfullyEmplaced = opWrapper.waitAndEmplace(datumToProcess);
			// Pop frame
			std::shared_ptr<std::vector<op::Datum>> datumProcessed;
			if (successfullyEmplaced && opWrapper.waitAndPop(datumProcessed)) {
				//userOutputClass.display(datumProcessed);
				//show("User worker GUI", datumProcessed);
				value = true;
			}
			else {
				//op::log("Processed datum could not be emplaced.", op::Priority::High, __LINE__, __FUNCTION__, __FILE__);
				value = false;
			}
		}
	//}

	opWrapper.stop();

	return value;
}

std::shared_ptr<std::vector<op::Datum>> new_datumsPtr() {
	return std::make_shared<std::vector<op::Datum>>();
}

int get(std::shared_ptr<std::vector<op::Datum>> dptr) {
	return dptr->at(0).poseKeypoints[{0, 0, 0}];
}

op::Datum datumsPtr_at(std::shared_ptr<std::vector<op::Datum>> dptr) {
	return dptr->at(0);
}

std::vector<uchar> mat_at(std::shared_ptr<std::vector<op::Datum>> dptr) {
	/*cout << mat->size() << endl;
	return mat->data;*/

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

float* get_pose_keypoints(std::shared_ptr<std::vector<op::Datum>> dptr) {
	return dptr->at(0).poseKeypoints.getPtr();
}

void emplaceBack(std::shared_ptr<std::vector<op::Datum>> dptr) {
	dptr->emplace_back();
}

void setCvInputData(std::shared_ptr<std::vector<op::Datum>> dptr, std::string image) {
	dptr->at(0).cvInputData = cv::imread(image);
	//return dptr;
}

void setInput(std::shared_ptr<std::vector<op::Datum>> dptr, std::vector<std::vector<float>> image) {
	std::vector<std::vector<uchar>> newimage;
	for (unsigned int i = 0; i < image.size(); i++) {
		for (unsigned int j = 0; j < image[0].size(); i++) {
			newimage[i][j] = (uchar)image[i][j];
		}
	}
	cv::Size size = cv::Size(image.size(), image[0].size());
	cv::Mat out(size, CV_8UC1);
	memcpy(out.data, &newimage, image.size());
	dptr->at(0).cvInputData = out;
	//return dptr;
}

std::string matToNumpyString(std::shared_ptr<std::vector<op::Datum>> dptr) {
	/*cv::Formatter const * c_formatter(cv::Formatter::get("numpy"));
	c_formatter->write(std::cout, image)*/
	std::stringstream buffer;
	buffer << cv::format(dptr->at(0).cvOutputData, 4);
	std::string s = buffer.str();
	s.erase(s.length() - 16);
	s.erase(0, 6);
	return s;
}

int getElement(int h, int w, int c, std::shared_ptr<std::vector<op::Datum>> dptr) {
	//std::cout << "Size: " << dptr->at(0).cvOutputData.size() << std::endl;
	return dptr->at(0).cvOutputData.at<cv::Vec3b>(h,w)[c];
}

void setElement(int h, int w, int c, std::shared_ptr<std::vector<op::Datum>> dptr, int value) {
	if (dptr->at(0).cvInputData.empty()) {
		dptr->at(0).cvInputData = cv::Mat(720, 1280, CV_8UC3);
	}
	dptr->at(0).cvInputData.at<cv::Vec3b>(h, w)[c] = (unsigned char)value;
}

void initInput(std::shared_ptr<std::vector<op::Datum>> dptr) {
	if (dptr->at(0).cvInputData.empty()) {
		dptr->at(0).cvInputData = cv::Mat(720, 1280, CV_8UC3);
	}
}

void show(std::string name, std::shared_ptr<std::vector<op::Datum>> dptr) {
	if (dptr != nullptr && !dptr->empty())
	{
		ofstream outputFile("outputCpp.txt");
		outputFile << dptr->at(0).cvOutputData;
		//cv::imshow("User worker GUI", dptr->at(0).cvOutputData);
		//cv::waitKey(1); // It displays the image and sleeps at least 1 ms (it usually sleeps ~5-10 msec to display the image)
	}
	else
		op::log("Nullptr or empty datumsPtr found.", op::Priority::High, __LINE__, __FUNCTION__, __FILE__);
}

std::vector<float> matToArray(cv::Mat mat) {
	std::vector<float> array;
	if (mat.isContinuous()) {
		array.assign((float*)mat.datastart, (float*)mat.dataend);
	}
	else {
		for (int i = 0; i < mat.rows; ++i) {
			array.insert(array.end(), mat.ptr<float>(i), mat.ptr<float>(i) + mat.cols);
		}
	}
	return array;
}