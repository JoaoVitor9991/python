num = int(input('Digite o termo: '))

t1 = 0 
t2 = 1
print(t1,',',t2,end='')
for i in range(num-2):
    t3 = t1 + t2
    print(',',t3,end="")
    t1 = t2
    t2 = t3
