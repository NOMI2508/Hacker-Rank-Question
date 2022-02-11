#include<iostream>
using namespace std;

void fun(int a)
{
	for (int i = 1; i <= 4; i++)
	{
		for (int j = 0; j < a - i; j++)
		{
			cout << " ";
		}

		for (int k = 0; k < i; k++)
		{
			cout << "*";
		}
		cout << endl;
	}


}


int main()
{
	int n = 4;
	fun(n);
	
    	system("pause");
	return 0;
}


