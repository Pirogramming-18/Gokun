num = 1
a=input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능):')
a=float(a)
a=int(a)

while a < 0:
        print ("정수를 입력하세요")
while a > 3:
        print ("1,2,3 중 하나를 입력하세요")
else:
    for _ in range(a):
        print ('playerA:',num)
        num += 1

b=input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능):')
b=float(b)
b=int(b)

if b < 0:
    print ("정수를 입력하세요")
elif b > 3:
    print ("1,2,3 중 하나를 입력하세요")
else:
    for _ in range(b):
        print ('playerB:',num)
        num += 1


    
