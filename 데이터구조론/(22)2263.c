#include <stdio.h>

int n, tmp;
int InOr[100001], PostOr[100001];

void PreOr(int Pstart, int Pend, int Istart, int Iend) //���������Լ� 
{
    int root = PostOr[Pend];
    printf("%d ", root);

    int Istnd = InOr[root] - Istart - 1; //�ο����� ����
    if (InOr[root] != Istart) //���ǹ��� �̿��� ��ȸ
        PreOr(Pstart, Pstart + Istnd, Istart, InOr[root] - 1);
    if (InOr[root] != Iend) //���ǹ��� �̿��� ��ȸ
        PreOr(Pstart + Istnd + 1, Pend - 1, InOr[root] + 1, Iend);
}

int main()
{
    scanf_s("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf_s("%d", &tmp);
        InOr[tmp] = i;
    }
    for (int i = 0; i < n; i++)
        scanf_s("%d", &PostOr[i]);

    PreOr(0, n - 1, 0, n - 1);
}