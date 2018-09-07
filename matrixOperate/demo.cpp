#include <iomanip>
#include <iostream>
#include "matrixDefine.h"
using namespace std;

void main()
{
	int m[10] = {0,1,2,3,4,5,6,7,8,9};
	Matrix<int> matrix1(m, 5, 2);
	matrix1.show();
}