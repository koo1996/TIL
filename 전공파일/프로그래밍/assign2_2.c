#include <stdio.h>

int main(void)
{
	int n,x,y;  //변수 선언
	printf("정수를 입력하시오: ");  
	scanf_s("%d", &x);  //x입력

	

	for (y = 1; y <= x; y++)  //y가 x보다 작거나 같을 때 y는 1씩 커진다.
	{
			for (n = 1; n <= y; n++)  //n이 y보다 작거나 같을 때 n은 1씩 커진다.
			printf("%d", n);  //n을 순서대로 나열한다.
			printf("\n");  //n을 줄바꿈한다.
		}
return 0; 
}