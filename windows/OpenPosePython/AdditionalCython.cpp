#include "AdditionalCython.h"

extern std::shared_ptr<std::vector<op::Datum>> datumsPtr;

AdditionalCython::AdditionalCython()
{
	
}

AdditionalCython::~AdditionalCython()
{
}

void AdditionalCython::printMat(std::vector< std::vector< std::vector<int> > > sv)
{
	int rows = sv.size();
	int cols = sv[0].size();
	int dim = sv[0][0].size();
	std::cout << "vector length " << rows << " , " << cols << " , " << dim << std::endl;

	std::cout << "[";
	for (int i = 0; i<rows; i++)
	{
		std::cout << "[";
		for (int j = 0; j<cols; j++)
		{
			std::cout << "[";
			for (int k = 0; k<dim; k++)
			{
				if (k + 1 != dim) {
					std::cout << sv[i][j][k] << ", ";
				}
				else {
					std::cout << "]";
				}
			}
			if (j + 1 != cols) {
				std::cout << "], ";
			}
			else {
				std::cout << "]";
			}
		}
		if (i + 1 != rows) {
			std::cout << "];" << std::endl;
		}
		else {
			std::cout << "]";
		}
	}
	std::cout << "]";
}

void AdditionalCython::setElement(std::vector< std::vector< std::vector<int> > > sv) {
	int rows = sv.size();
	int cols = sv[0].size();
	int dim = sv[0][0].size();
	std::cout << "------------------INSIDE SET ELEMENT------------------" << std::endl;
	if (datumsPtr != nullptr) {
		std::cout << "Datum OK" << std::endl;
	}
	else {
		std::cout << "Datum NULL" << std::endl;
		datumsPtr = std::make_shared<std::vector<op::Datum>>();
	}
	if (datumsPtr->at(0).cvInputData.empty()) {
		std::cout << "------------------DATUM EMPTY------------------" << std::endl;
		datumsPtr->at(0).cvInputData = cv::Mat(cols, rows, CV_8UC3);
	}

	for (int i = 0; i<rows; i++)
	{
		std::cout << i << std::endl;
		for (int j = 0; j<cols; j++)
		{
			for (int k = 0; k<dim; k++)
			{
				datumsPtr->at(0).cvInputData.at<cv::Vec3b>(j, i)[k] = (unsigned char)sv[i][j][k];
				//setCvInputValue(j, i, k, sv[i][j][k]);
			}
		}
	}
}