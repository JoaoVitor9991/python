a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

if c>b and b>a:
    print(a,b,c)

if b>c and c>a:
    print(a,c,b)

if c>a and a>b:
    print(b,a,c)
    
if a>b and b>c:
    print(c,b,a)