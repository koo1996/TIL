#include <stdio.h>
int main(void)
{
	printf("*****************\n");
	printf("A---- Add \nS---- Subtract \nM---- Multiply \nD---- Divide \nQ---- Quit\n");
	printf("*****************\n");

	int x, y;  //변수 선언
	char C;  //


	do
	{
		printf("연산을 선택하시오 :");  //A S M D Q 선택한다.
		scanf_s("%c%*c", &C);  //입력값을 출력한다.

		if (C == 'A')  //A(더하기)를 선택했을때
		{
			printf("두수를 공백으로 분리하여 입력하시오 :");  //x,y 값을 입력한다.
			scanf_s("%d%d", &x, &y); //x+y 출력한다
			printf("%d", x + y);
			break;
		}
		else if (C == 'S')  //S(빼기)를 선택했을때
		{
			printf("두수를 공백으로 분리하여 입력하시오 :");  //x,y 값을 입력한다.
			scanf_s("%d%d", &x, &y);  //x-y 출력한다.
			printf("%d", x - y);
			break;
		}
		else if (C == 'M')  //M(곱하기)를 선택했을때
		{
			printf("두수를 공백으로 분리하여 입력하시오 :");  //x,y 값을 입력한다.
			scanf_s("%d%d", &x, &y);  //x*y 출력한다.
			printf("%d", x * y);
			break;
		}
		else if (C == 'D')  //D(나누기)를 선택했을때  
		{
			printf("두수를 공백으로 분리하여 입력하시오 :");  //x,y 값을 입력한다.
			scanf_s("%d%d", &x, &y);  //x/y 출력한다.
			printf("%d", x / y);
			break;
		}
		else if (C == 'Q')  //Q(종료)를 선택했을때
		{
			break;
		}
	} while (C);
}