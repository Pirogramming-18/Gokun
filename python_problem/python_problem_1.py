num = 0
a=input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능):')
a=float(a)
a=int(a)
if a < 0:
    print ("정수를 입력하세요")
elif a > 3:
    print ("1,2,3 중 하나를 입력하세요")