num=0
end=False

a=input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능);')
try:
    a = int(a)
    if a<0<3:
        raise Exception('1,2,3중 하나를 입력하세요')
    else:
        print ('1,2,3중 하나를 입력하세요')
except Exception:
        print ('정수를 입력하세요')    
