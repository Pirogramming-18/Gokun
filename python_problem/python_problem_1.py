num=0
player='B'
try:
   while True:
    a=int(input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능):'))
    player = ('B' if player=='A' else 'A')
    if a<=0:
            print ('정수를 입력하세요')
    elif a>3:
            print ('1,2,3 중 하나를 입력하세요')
            
    elif (0<a<4):
                for _ in range(a):                    
                        num += 1
                        print ('player{0}:{1}'.format(player, num))
except Exception:
      print ('정수를 입력하세요')

