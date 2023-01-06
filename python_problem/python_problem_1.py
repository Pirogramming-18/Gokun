import random as R
def brGame():
    num=0
    pc=1
    #0: com 1: player

    while True:
        if pc == 0:
            count=R.randint(1,3)
        elif pc == 1:
            try:
                count=int(input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능):'))
                if not 1<=count<=3:
                    raise Exception('1,2,3 중 하나를 입력하세요')
            except ValueError:
                    print ('정수를 입력하세요')
                    continue
            except Exception as e:
                    print (e)
                    continue
                    #입력 끝
                        
        if pc==0:
            pc=1
            count_all=count+num
            while num<count_all:
                num+=1
                print ('computer:',num)
                if num>=31:
                    return pc
                    #컴퓨터 끝
                
        elif pc==1:
            pc=0
            count_all=count+num
            while num<count_all:
                num+=1
                print ('player:',num)
                if num>=31:
                    return pc
                    #사람일때 끝
         
br=brGame()
if br==0:
    print ('computer win!')
elif br==1:
    print ('player win!')
                    


