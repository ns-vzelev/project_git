#include <stdio.h>
#include <math.h>
int parties(int n, int N,int sum, int * a[100000])
{
    int sum1 = sum - n*N;
    if(sum1<0)
      return -1;
    int i = 0;
    int diff[N];
    for(;i<N;++i)
    {
      diff[i] = a[i][1] - n;
     /* printf("%d\n", diff[i]); */
    }
    i = 0;
    
    for (i = 0;i<N;i++)
    {
    int left = i;
    int right = i;
      while(diff[i]<0)
      {
       if(i <= 0)
       left = -1;
       if(left > -1)
        while(diff[left]<=0)
        {
          left -= 1;
          if(left == 0)
            if(diff[0]<=0)
            {
              left = -1;
              break;
            }
        }
         if(right >= N-1)
         right = -1;
        if(right > 0)
        while(diff[right]<=0)
        {
         right += 1;
         if(right == N-1)
           if(diff[right]<=0)
           {
             right = -1;
             break;
           }
        }
        if(left <= -1 && right <= -1)
         return -1;
        int c;
        if(left <= -1 || left == i)
           c = right;
        else if(right <= 0 || right == i)
           c = left;
        else
        {
         if((int)fabs((int)a[i][0] - (int)a[left][0])<(int)fabs((int)a[i][0] - (int)a[right][0]))
          c = left;
          else
          c = right;
        }
      
        int dist;
        dist = (int)fabs(a[i][0]- a[c][0]);
        if(diff[c]<=dist)
        { 
           if(c == left)
           left -= 1;
           else
           right += 1;
           continue;
        }
        sum1 -= dist;
        diff[c] -= dist;
        if(sum1<0)
          return -1;
        if(diff[c]<-diff[i])
          {
          diff[i] += diff[c];
          diff[c] = 0;
          if(c == N-1 || c == 0)
          return -1;
          if(c == left)
           left -= 1;
           else
           right += 1;
          }
          else
          {
           diff[c] += diff[i];
           diff[i] = 0;
           if(c == left)
           left -= 1;
           else
           right += 1;
           break;
          }             
      }
    }
   return sum1;
}
int main()
{
int * a[100000];
long long int sum = 0;
int N;
scanf("%d", &N);
if(N>100000)
{
printf("1\n");
return 0;
}
int i = 0;
for (;i<N;i++)
{
    a[i] =(int *) malloc(sizeof(int)*2);
    if(!a[i])
        return 0; 
    scanf("%d %d", &a[i][0], &a[i][1]);
    sum += a[i][1];
}
if(N==1)
{
printf("%d\n", a[0][1]);
return 0;
}
i = 0;
int isSorted = 0;
while(!isSorted)
{
  int j = 1;
  isSorted = 1;
    for(;j<N;j++)
    {
        if(a[j-1][0] > a[j][0])
                {
                int * temp = a[j];
                a[j] = a[j-1];
                a[j-1] = temp;
                isSorted = 0;
                }
    }
}
i = 0;
int left = 0, right = sum/N, mid, mod;
i = 0;
for(;i<sum/N;i++)
{
 
         mod = parties(i, N, sum, a); 
         int mod1 = parties(i+1, N,sum,a);             
         if(mod>=0 && mod < N || mod>=0 && mod1<=0)
         {
                  printf("%d ", i);
                  system("pause");
                  return 0;
         }
   
}
system("pause");
return 0;
}
