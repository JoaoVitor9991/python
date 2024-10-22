a = 80000
b = 200000
cont = 0
while True:
    if a <= b:
        a = a + (a * 0.03)
        b = b + (b * 0.015)
        cont = cont + 1
    else:
        break
print('A:',a) 
print('B:',b)
print(f'Para A passar B levara {cont} anos')