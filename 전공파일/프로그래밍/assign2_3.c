#include <stdio.h>
int main(void)
{
	printf("*****************\n");
	printf("A---- Add \nS---- Subtract \nM---- Multiply \nD---- Divide \nQ---- Quit\n");
	printf("*****************\n");

	int x, y;  //���� ����
	char C;  //


	do
	{
		printf("������ �����Ͻÿ� :");  //A S M D Q �����Ѵ�.
		scanf_s("%c%*c", &C);  //�Է°��� ����Ѵ�.

		if (C == 'A')  //A(���ϱ�)�� ����������
		{
			printf("�μ��� �������� �и��Ͽ� �Է��Ͻÿ� :");  //x,y ���� �Է��Ѵ�.
			scanf_s("%d%d", &x, &y); //x+y ����Ѵ�
			printf("%d", x + y);
			break;
		}
		else if (C == 'S')  //S(����)�� ����������
		{
			printf("�μ��� �������� �и��Ͽ� �Է��Ͻÿ� :");  //x,y ���� �Է��Ѵ�.
			scanf_s("%d%d", &x, &y);  //x-y ����Ѵ�.
			printf("%d", x - y);
			break;
		}
		else if (C == 'M')  //M(���ϱ�)�� ����������
		{
			printf("�μ��� �������� �и��Ͽ� �Է��Ͻÿ� :");  //x,y ���� �Է��Ѵ�.
			scanf_s("%d%d", &x, &y);  //x*y ����Ѵ�.
			printf("%d", x * y);
			break;
		}
		else if (C == 'D')  //D(������)�� ����������  
		{
			printf("�μ��� �������� �и��Ͽ� �Է��Ͻÿ� :");  //x,y ���� �Է��Ѵ�.
			scanf_s("%d%d", &x, &y);  //x/y ����Ѵ�.
			printf("%d", x / y);
			break;
		}
		else if (C == 'Q')  //Q(����)�� ����������
		{
			break;
		}
	} while (C);
}