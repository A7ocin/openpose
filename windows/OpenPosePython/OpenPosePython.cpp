#include "OpenPosePython.h"

using namespace std;
using namespace op;

// See all the available parameter options withe the `--help` flag. E.g. `./build/examples/openpose/openpose.bin --help`.
// Note: This command will show you flags for other unnecessary 3rdparty files. Check only the flags for the OpenPose
// executable. E.g. for `openpose.bin`, look for `Flags from examples/openpose/openpose.cpp:`.
// Producer
DEFINE_string(image_dir, "examples/media/", "Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).");

// The W-classes can be implemented either as a template or as simple classes given
// that the user usually knows which kind of data he will move between the queues,
// in this case we assume a std::shared_ptr of a std::vector of op::Datum

// This worker will just read and return all the jpg files in a directory
//UserInputClass::UserInputClass(const std::string& directoryPath) :
//	mImageFiles{ op::getFilesOnDirectory(directoryPath, "jpg") },
//	// mImageFiles{op::getFilesOnDirectory(directoryPath, std::vector<std::string>{"jpg", "png"})}, // If we want "jpg" + "png" images
//	mCounter{ 0 },
//	mClosed{ false }
//{
//	if (mImageFiles.empty())
//		op::error("No images found on: " + directoryPath, __LINE__, __FUNCTION__, __FILE__);
//}
//
//std::shared_ptr<std::vector<op::Datum>> UserInputClass::createDatum(std::shared_ptr<std::vector<op::Datum>> datumsPtr)
//{
//	// Close program when empty frame
//	if (mClosed || mImageFiles.size() <= mCounter)
//	{
//		op::log("Last frame read and added to queue. Closing program after it is processed.", op::Priority::High);
//		// This funtion stops this worker, which will eventually stop the whole thread system once all the frames have been processed
//		mClosed = true;
//		return nullptr;
//	}
//	else // if (!mClosed)
//	{
//		// Create new datum
//		//datumsPtr = std::make_shared<std::vector<op::Datum>>();
//		datumsPtr->emplace_back();
//		auto& datum = datumsPtr->at(0);
//
//		// Fill datum
//		datum.cvInputData = cv::imread(mImageFiles.at(mCounter++));
//
//		// If empty frame -> return nullptr
//		if (datum.cvInputData.empty())
//		{
//			op::log("Empty frame detected on path: " + mImageFiles.at(mCounter - 1) + ". Closing program.", op::Priority::High);
//			mClosed = true;
//			datumsPtr = nullptr;
//		}
//
//		return datumsPtr;
//	}
//}
//
//bool UserInputClass::isFinished() const
//{
//	return mClosed;
//}

//void UserOutputClass::display(const std::shared_ptr<std::vector<op::Datum>>& datumsPtr)
//{
//	// User's displaying/saving/other processing here
//	// datum.cvOutputData: rendered frame with pose or heatmaps
//	// datum.poseKeypoints: Array<float> with the estimated pose
//	if (datumsPtr != nullptr && !datumsPtr->empty())
//	{
//		cv::imshow("User worker GUI", datumsPtr->at(0).cvOutputData);
//		cv::waitKey(1); // It displays the image and sleeps at least 1 ms (it usually sleeps ~5-10 msec to display the image)
//	}
//	else
//		op::log("Nullptr or empty datumsPtr found.", op::Priority::High, __LINE__, __FUNCTION__, __FILE__);
//}

void test() {
	cout << "Working" << endl;
}

int openPoseTutorialWrapper1(std::shared_ptr<std::vector<op::Datum>> datumToProcess)
{
	int value = 0;
	op::log("Starting pose estimation demo.", op::Priority::High);
	const auto timerBegin = std::chrono::high_resolution_clock::now();
	// Configure OpenPose
	op::Wrapper<std::vector<op::Datum>> opWrapper{ op::ThreadManagerMode::Asynchronous };
	// Pose configuration (use WrapperStructPose{} for default and recommended configuration)
	op::WrapperStructPose wrapperStructPose{};
	wrapperStructPose.renderMode = op::RenderMode::Gpu;
	// Configure wrapper
	opWrapper.configure(wrapperStructPose);

	op::log("Starting thread(s)", op::Priority::High);
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
				value = 0;
			}
			else {
				op::log("Processed datum could not be emplaced.", op::Priority::High, __LINE__, __FUNCTION__, __FILE__);
				value = 1;
			}
		}
	//}

	op::log("Stopping thread(s)", op::Priority::High);
	opWrapper.stop();

	// Measuring total time
	const auto now = std::chrono::high_resolution_clock::now();
	const auto totalTimeSec = (double)std::chrono::duration_cast<std::chrono::nanoseconds>(now - timerBegin).count() * 1e-9;
	const auto message = "Real-time pose estimation demo successfully finished. Total time: " + std::to_string(totalTimeSec) + " seconds.";
	op::log(message, op::Priority::High);

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

int getElement(int w, int h, int c, std::shared_ptr<std::vector<op::Datum>> dptr) {
	return dptr->at(0).cvOutputData.at<int>(w,h,c);
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