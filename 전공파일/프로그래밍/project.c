#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define S_SIZE 30

typedef struct NODE {
	char title[S_SIZE];
	int year;
	int check;
	struct NODE *link;
}NODE;

int main(void) {
	NODE *list = NULL;
	NODE *prev, *p, *next;
	char buffer[S_SIZE];
	int year;
	int menu;


	int i;
		printf("연결형 리스트를 이용한 도서관리 프로그램\n");
		while (1)
		{
			printf("\n=====================\n");
			printf("0. 신규 등록\n");
			printf("1. 도서 대출\n");
			printf("2. 도서 반납\n");
			printf("3. 목록 출력\n");
			printf("4. 종료\n");
			printf("=====================\n");
			scanf("%d", &menu);
			getchar();

			if (menu == 0)
			{
				p = (NODE*)malloc(sizeof(NODE));
				printf("등록할 책의 제목을 입력하시오: ");
				gets(buffer);
				strcpy(p->title, buffer);

				printf("책의 출판 연도를 입력하시오: ");
				gets(buffer);
				year = atoi(buffer);
				p->year = year;
				p->check = 0;

				if (list == NULL)
					list = p;
				else
					prev->link = p;
				p->link = NULL;
				prev = p;

				printf("%s\n를 성공적으로 등록하였습니다.\n", p->title);

			}
			else if (menu == 1)
			{
				printf("대여할 책의 제목을 입력하시오: ");
				gets(buffer);
				p = list;
				while (p != NULL)
				{
					if (strcmp(p->title, buffer) == 0)
					{
						if (p->check == 0)
						{
							p->check = 1;
							printf("%s\n 를 대출에 성공하였습니다.\n", buffer);
						}
						else
						{
							printf("%s\n 가 이미 대출중입니다.\n", buffer);
						}
						break;
					}
					p = p->link;
				}
				if(p==NULL)
					printf("%s\n 가 존재하지 않습니다.\n", buffer);
			}
			else if (menu == 2)
			{
				printf("반납할 책의 제목을 입력하시오: ");
				gets(buffer);
				p = list;
				while (p != NULL)
				{
					if (strcmp(p->title, buffer) == 0)
					{
						if (p->check == 1)
						{
							p->check = 0;
							printf("%s\n 반납에 성공하였습니다.\n", buffer);
						}
						else
						{
							printf("%s\n 는 대출중인 책이 아닙니다.\n", buffer);
						}
						break;
					}
					p = p->link;
				}
				if(p==NULL)
					printf("%s\n 가 존재하지 않습니다.\n", buffer);
			}
			else if (menu == 3)
			{
				p = list;
				i = 0;
				while (p != NULL)
				{
					printf("순서 %d, 출판연도 %d, 대출여부 %d, 제목 %s\n\n", i, p->year, p->check, p->title);
					p = p->link;
					i++;
				}
			}
			else if (menu == 4)
			{
				p = list;
				while (p != NULL)
				{
					next = p->link;
					free(p);
					p = next;
				}

				printf("메모리를 모두 반납하였습니다.\n");
				break;
			}
			else
			{
				printf("잘못 입력하였습니다.\n");
			}
		}
}