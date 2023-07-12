array = list(map(int,input().strip().split()))
b = int(input())
count = 0
for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if array[i] + array[j] == b:
            count+=1
print(count)