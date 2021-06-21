while True:
    from random import randint
    unknow = randint(1, 100)
    while True:
        guess=input("請輸入數字")
        guess=int(guess)
        if (guess > unknow):
            print("小於",guess)
            continue
        else:
            if (guess < unknow):
                print("大於",guess)
                continue
            else:
                print("bingo")
                break
    print("是否重新?1=Yes 2=No")  
    a=1
    c=input("請輸入1or2: ")
    c=int(c)
    if (c > 2 or c < 1):
        print("輸入錯誤，強制結束。")
        break
    elif(c > a):
        break
    else:
        continue