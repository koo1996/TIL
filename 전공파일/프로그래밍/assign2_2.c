#include <stdio.h>

int main(void)
{
	int n,x,y;  //���� ����
	printf("������ �Է��Ͻÿ�: ");  
	scanf_s("%d", &x);  //x�Է�

	

	for (y = 1; y <= x; y++)  //y�� x���� �۰ų� ���� �� y�� 1�� Ŀ����.
	{
			for (n = 1; n <= y; n++)  //n�� y���� �۰ų� ���� �� n�� 1�� Ŀ����.
			printf("%d", n);  //n�� ������� �����Ѵ�.
			printf("\n");  //n�� �ٹٲ��Ѵ�.
		}
return 0; 
}