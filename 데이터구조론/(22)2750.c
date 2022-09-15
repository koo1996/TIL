#include<stdio.h>

int main() {
	int N, arr[1000] = { 0 };
	int temp;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	} //버블정렬 
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N - 1; j++) { //데이터교환
			if (arr[j + 1] < arr[j]) { //비교 연산
				temp = arr[j + 1];
				arr[j + 1] = arr[j];
				arr[j] = temp;
			}
		}
	}
	for (int i = 0; i < N; i++) {
		printf("%d\n", arr[i]);
	}
	return 0;
}