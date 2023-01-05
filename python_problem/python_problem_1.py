turn = 'A' # 플레이어 출력 시 사용
num = 0
end = False # while문 종료조건
while not end:
    inp = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능):')
    try : 
        inp = int(inp) # 실수면 오류
        if inp < 0 : raise Exception() # 0보다 작아도 오류
        if (0 < inp < 4): # 1,2,3일때만
            while inp > 0:
                num += 1
                if num == 31:
                    end = True
                    inp = 0
                inp -= 1
                print("player{} : {}".format(turn, num))
            turn = ('B' if turn=='A' else 'A')
        else: # 0이거나 4 이상이면
            print("1,2,3 중 하나를 입력하세요")
    except:
        print("정수를 입력하세요")
        
