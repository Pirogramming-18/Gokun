num=0

try:
   while True:
    a=int(input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능):'))
    if a<0:
            print ('정수를 입력하세요')
    elif a>3:
            print ('1,2,3 중 하나를 입력하세요')
    else:
            break
except:
      print ('정수를 입력하세요')
      