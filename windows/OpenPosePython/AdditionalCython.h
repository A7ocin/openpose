#include <vector>
#include <iostream>
#include "openpose\core\datum.hpp"

extern std::shared_ptr<std::vector<op::Datum>> datumsPtr;

class AdditionalCython {
public:
	AdditionalCython();
	~AdditionalCython();
	void printMat(std::vector< std::vector< std::vector<int> > > sv);
	void setElement(std::vector< std::vector< std::vector<int> > > sv);
};