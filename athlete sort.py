from operator import itemgetter
n,m=map(int,input().split())
A=[]
for i in range(n):
    A.append(list(map(int,input().split())))
k=int(input())
for i in sorted(A,key=itemgetter(k)):
    print(*i)
