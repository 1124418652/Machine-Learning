#include <iostream>
#include <cstring>

#define _Matrix(ins) Matrix<int> ins(#ins)
#define _Matrix(ins, row, col) Matrix<int> ins(#ins, row, col)
#define _Matrix(ins, matrix, row, col) Matrix<int> ins(#ins, matrix, row, col)

using namespace std;
typedef unsigned int UINT;

template<class T>
class Matrix
{
	int col;
	int row;
	T *matrix;
	string *name;
	public:
		Matrix(char *n, T *m, int row1, int col1):row(row1), col(col1){
			strcpy(name, n);
			matrix = new T[row*col];
			for (int i=0; i<row*col; i++)
			{
				matrix[i] = m[i];
			}
		}
		Matrix(char *n, int row1, int col1):row(row1), col(col1)
		{
			strcpy(name, n);
			matrix = new T[row*col];
			cout<<"Have set the shape of the matrix, but should use create() to initialize the matrix!"<<endl;
		}
		Matrix(char *n)
		{
			strcpy(name, n);
			matrix = NULL;
		}
		~Matrix(){
			delete[] matrix;
		}
		void show();
		UINT create(T *m);
		UINT zeros(int size);
		UINT eye(int size);

		//friend Matrix operator+(const Matrix &a, const Matrix &b);
		Matrix operator+(const Matrix &);
		//friend Matrix operator-(const Matrix &a, const Matrix &b);
		Matrix operator-(const Matrix &);
		//friend Matrix operator*(const Matrix &a, const Matrix &b);
		Matrix operator*(const Matrix &);
		Matrix &operator=(const Matrix &);
		friend ostream &operator<<(ostream &output, const Matrix &a);
		Matrix matrix_T();              // transpose the matrix
		Matrix matrix_Inv();            // calculate matrix's inverse
		Matrix matrix_Adjoint();        // calculate the adjoint matrix
};


template<class T>
void Matrix<T>::show()
{
	if (col==0 || row ==0)
	{
		cout<<"The matrix is empty"<<endl;
		return;
	}
	cout<<"Show matrix ";
	for (int i=0; i<row; i++)
	{
		for (int j=0; j<col; j++)
		{
			cout<<setw(sizeof(T))<<matrix[i*col+j];
		}
		cout<<endl;
	}
	cout<<endl;
}


template<class T>
UINT Matrix<T>::create(T *m)
{
	for (int i=0; i<row; i++)
	{
		for (int j=0; j<col; j++)
		{
			matrix[i*col+j] = *m++;
		}
	}
	return 1;
}


template<class T>
UINT Matrix<T>::zeros(int size)
{
	col = size;
	row = size;
	if(NULL == (matrix=new T[row*col]))
	{
		cout<<"don't have enough memory!"<<endl;
		return 0;
	}
	for (int i=0; i<row; i++)
	{
		for (int j=0; j<col; j++)
		{
			matrix[i*col+j] = 0;
		}
	}
	return 1;
}


template<class T>
UINT Matrix<T>::eye(int size)
{
	col = size;
	row = size;
	if (NULL == (matrix=new T[row*size]))
	{
		cout<<"Don't have enough memory"<<endl;
		return 0;
	}
	for (int i=0; i<row; i++)
	{
		for (int j=0; j<col; j++)
		{
			if (i==j)
				matrix[i*col+j] = 1;
			else
				matrix[i*col+j] = 0;
		}
	}
	return 1;
}


template<class T>
Matrix<T> Matrix<T>::operator +(const Matrix<T> &m1)
{
	if (m1.col!=col || m1.row!=row)
	{
		cout<<"These two matrices can't be plused!"<<endl;
		exit(0);
	}
	T *tmp = new T[col*row];
	for (int i=0; i<row; i++)
	{
		for (int j=0; j<col; j++)
		{
			tmp[i*col+j] = m1.matrix[i*col+j] + matrix[i*col+j];
		}
	}
	return Matrix<T>(tmp, row, col);
}

template<class T>
Matrix<T> Matrix<T>::operator -(const Matrix<T> &m1)
{
	if (m1.col!=col || m1.row!=row)
	{
		cout<<"These two matrices can't be plused!"<<endl;
		exit(0);
	}
	T *tmp = new T[col*row];
	for (int i=0; i<row; i++)
	{
		for (int j=0; j<col; j++)
		{
			tmp[i*col+j] = m1.matrix[i*col+j] - matrix[i*col+j];
		}
	}
	return Matrix<T>(tmp, row, col);
}


template<class T>
Matrix<T> Matrix<T>::operator *(const Matrix &m1)
{
	if (col != m1.row)
	{
		cout<<"These two matrices can't be multiplied"<<endl;
		exit(0);
	}
	T *tmp = new T[row*m1.col];
	for (int i=0; i<row; i++)
	{
		for (int j=0; j<m1.col; j++)
		{
            T data = 0;
            for(int m_1=0; m_1<col; m_1++)
            {
                data = data + matrix[i*col+m_1] * m1.matrix[m_1*m1.col+j];
            }
            tmp[i*m1.col+j] = data;
		}
	}
	return Matrix<T>(tmp, row, m1.col);
}


template<class T>
Matrix<T>& Matrix<T>::operator =(const Matrix<T> &m)
{
	delete[] matrix;
	if (m.matrix)
	{
		row = m.row;
		col = m.col;
		matrix = new T[m.row*m.col];
		for (int i=0; i<row*col; i++)
		{
			matrix[i] = m.matrix[i];
		}
	}
	else
		matrix = NULL;
	return *this;
}

template<class T>
Matrix<T> Matrix<T>::matrix_T()
{
	T *tmp = new T[col*row];
	int k = 0;
	for (int j=0; j<col; j++)
	{
		for (int i=0; i<row; i++)
		{
			tmp[k] = matrix[i*col+j];
			k++;
		}
	}
	return Matrix<T>(tmp, col, row);
}


