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

	//// Configure OpenPose
	//op::Wrapper<std::vector<op::Datum>> opWrapper{ op::ThreadManagerMode::Asynchronous };
	//// Pose configuration (use WrapperStructPose{} for default and recommended configuration)
	//op::WrapperStructPose wrapperStructPose{};
	//wrapperStructPose.renderMode = op::RenderMode::Gpu;
	//// Configure wrapper
	//opWrapper.configure(wrapperStructPose);

	//opWrapper.start();

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

	//opWrapper.stop();

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

void setMat(std::shared_ptr<std::vector<op::Datum>> dptr, uchar* matData) {
	std::cout << matData << std::endl;
	dptr->at(0).cvInputData.data = matData;
}

std::shared_ptr<std::vector<op::Datum>> new_datumsPtr() {
	datumsPtr = std::make_shared<std::vector<op::Datum>>();
	return datumsPtr;
	//return std::make_shared<std::vector<op::Datum>>();
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

void setInput(std::shared_ptr<std::vector<op::Datum>> dptr, std::vector<std::vector<int>> np_image, std::string resolution) {
	int width, height, w, h, c;
	size_t pos = 0;

	std::string delimiter = "x";
	pos = resolution.find(delimiter);
	width = stoi(resolution.substr(0, pos));
	resolution.erase(0, resolution.find(delimiter) + delimiter.length());
	pos = resolution.find(delimiter);
	height = stoi(resolution.substr(0, pos));
	
	int channels = 3;

	std::cout << "-----------------------------------------------------------------" << std::endl;
	
	//std::memcpy(A.data, x, 280 * 280 * sizeof(uchar));
	/*cv::Mat test = cv::Mat(cv::Size(1280, 720), CV_8UC3, (void*)np_image.data());
	std::cout << test.rows << std::endl;
	std::cout << test.cols << std::endl;*/
	/*cv::imshow("Test", A);
	cv::waitKey(1);*/

	/*dptr->at(0).cvInputData.convertTo(dptr->at(0).cvInputData, CV_8UC3);*/
	//memcpy(dptr->at(0).cvInputData.data, np_image.data(), np_image.size() * sizeof(int));

	std::cout << "-----------------------------IT WORKS------------------------------------" << std::endl;
	std::cout << dptr->at(0).cvInputData.rows << std::endl;
	std::cout << dptr->at(0).cvInputData.cols << std::endl;
	std::cout << np_image.data() << std::endl;
	std::cout << dptr->at(0).cvInputData.data << std::endl;

	/*if (dptr->at(0).cvInputData.empty()) {	
		dptr->at(0).cvInputData = cv::Mat(height, width, CV_8UC3, double(0));
	}

	for (h = 0; h < height; h++) {
		for (w = 0; w < width; w++) {
			for (c = 0; c < channels; c++) {
				dptr->at(0).cvInputData.at<cv::Vec3b>(h, w)[c] = (unsigned char)np_image[h][w][c];
			}
		}
	}*/
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

void setElement(int h, int w, int c, std::shared_ptr<std::vector<op::Datum>> dptr, int value, int width, int height) {
	if (dptr->at(0).cvInputData.empty()) {
		dptr->at(0).cvInputData = cv::Mat(height, width, CV_8UC3, double(0));
	}
	dptr->at(0).cvInputData.at<cv::Vec3b>(h, w)[c] = (unsigned char)value;
}

void setCvInputValue(int h, int w, int c, int value) {
	datumsPtr->at(0).cvInputData.at<cv::Vec3b>(h, w)[c] = value;
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

void test() {
	std::cout << "Starting..." << std::endl;
	//int x[1000000] = { 0 };
	//std::vector<std::vector<int>> x = std::vector<std::vector<int>>();
	/*for (int i = 0; i < 1000000; i++) {
		x[i] = 0;
		std::cout << i << std::endl;
	}*/
	/*cv::Size size = cv::Size(1280, 1280);
	std::this_thread::sleep_for(std::chrono::milliseconds(5000));*/

	//cv::Mat A(1280, 1280, CV_8UC3, double(0));
	
	////1 channel
	//std::array<uchar, 921600> test1 = { 0 };
	////3 channel
	//std::array<uchar, 2764800> test3 = { 0 };
	//std::cout << "DONE" << std::endl;
	//cv::Mat A = cv::Mat(720, 1280, CV_8UC1, test1.data());

	std::array<uchar, 921600> rawData = { 0 };
	cv::Mat rawMat = cv::Mat(720, 1280, CV_8UC1, rawData.data());
	cv::Mat chan[3] = {
		rawMat,
		rawMat,
		rawMat
	};

	/*for (cv::Mat& channel : chan)
		channel = channel.reshape(1280, 720);*/

	cv::Mat merged;
	cv::merge(chan, 3, merged);
	
	cv::imshow("Test", merged);
	cv::waitKey(1);
}

void setCppInput(std::shared_ptr<std::vector<op::Datum>> dptr, std::vector<std::vector<int>> np_image1, std::vector<std::vector<int>> np_image2, std::vector<std::vector<int>> np_image3, std::string resolution) {
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

	std::cout << "---------------------------SIZE----------------------------" << std::endl;
	std::cout << np_image1.size() << " x " << np_image1[0].size() << std::endl;
	std::cout << np_image2.size() << " x " << np_image2[0].size() << std::endl;
	std::cout << np_image3.size() << " x " << np_image3[0].size() << std::endl;

	//std::array<uchar, 921600> rawData1, rawData2, rawData3;
	uchar* rawData1 = new uchar[921600];
	uchar* rawData2 = new uchar[921600];
	uchar* rawData3 = new uchar[921600];
	//for (int i = 0; i < np_image1.size(); i++) {
		for (int j = 0; j < np_image1[0].size(); j++) {
			rawData1[j] = (uchar)np_image1[0][j];
			rawData2[j] = (uchar)np_image2[0][j];
			rawData3[j] = (uchar)np_image3[0][j];
			//rawData2[i * np_image2.size() + j] = (uchar)np_image2[i][j];
			//rawData3[i * np_image3.size() + j] = (uchar)np_image3[i][j];
		}
	//}

	uchar* my_array = new uchar[921600 * 3];
	memcpy(my_array, (rawData1), sizeof(uchar) * 921600);
	memcpy(my_array + (sizeof(uchar)*921600), (rawData2), sizeof(uchar) * 921600);
	memcpy(my_array + 2*(sizeof(uchar) * 921600), (rawData3), sizeof(uchar) * 921600);
	//cv::Mat* out = new cv::Mat(height, width, CV_8UC3, my_array);

	cv::Mat* chan = new cv::Mat[3];
	chan[0] = cv::Mat(height, width, CV_8UC1, my_array);
	chan[1] = cv::Mat(height, width, CV_8UC1, my_array + sizeof(uchar) * 921600);
	chan[2] = cv::Mat(height, width, CV_8UC1, my_array + sizeof(uchar) * 921600 * 2);

	cv::Mat* out = new cv::Mat(height, width, CV_8UC3);
	cv::merge(chan, 3, *out);

	//cv::Mat r = cv::Mat(height, width, CV_8UC1, rawData1.data());
	//cv::Mat g = cv::Mat(height, width, CV_8UC1, rawData2.data());
	////cv::Mat b = cv::Mat(height, width, CV_8UC1, rawData3.data());
	//
	//std::vector<cv::Mat> out{ r,g,r };

	//cv::Mat merged;
	//cv::merge(out, merged);

	/*cv::imshow("Test", r);
	cv::waitKey(1);*/

			//std::array<uchar, 3*921600> rawData;
			//for (int i = 0; i < np_image.size(); i++) {
			//	for (int j = 0; j < np_image[0].size(); j++) {
			//		for (int k = 0; k < np_image[0][0].size(); k++) {
			//			//[x + WIDTH * (y + DEPTH * z)]
			//			rawData[i + np_image.size() *( j + np_image[0].size() * k )] = (uchar)np_image[i][j][k];
			//		}
			//	}
			//}
			//cv::Mat out = cv::Mat(height, width, CV_8UC3, rawData.data());
			//cv::imshow("Test", out);
			//cv::waitKey(1);
	datumsPtr->at(0).cvInputData = *out;
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