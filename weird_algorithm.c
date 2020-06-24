#include<stdio.h>
int main(){
	int num;
	scanf("%d",&num);
	while (num!=1)
	{
		printf("%d ",num);
		if(num%2==0)
		num = num / 2;
		else
		num = (num*3)+1;			
	}
	printf("1");
}
