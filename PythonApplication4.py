#Module Section
import random
import time

#Founction Section
def loading(): #Design
    time.sleep(1)
    print(". ")
    time.sleep(1)
    print(". ")
    time.sleep(1)
    print(". ")
    time.sleep(1)
def loading2():
    percent_list=[]
    while len(percent_list) != 6:
        per = random.randint(1, 100)
        if per not in percent_list:
            percent_list.append(per)
    for i in range(1, len(percent_list)): #Insertion Sort
        j = i - 1
        key = percent_list[i]
        while percent_list[j] > key and j >= 0:
            percent_list[j+1] = percent_list[j]
            j = j - 1
        percent_list[j+1] = key
    print("Loading... Please Wait")
    time.sleep(0.6)
    for k in percent_list:
        print(str(k)+'%..')
        time.sleep(k%3)
    print("100%..")    
def cal_coin(n): #Rewarding Founction
    global coin
    if n == 2:
        coin+=2
        print("Excellent! +2 coin :D")
    elif n == 1:
        coin+=1
        print("Not bad! +1 coin :P")
    elif n == 0:
        coin +=0
        print("That was so close~")
    elif n == -1:
        coin-=1
        print("Try one more time. -1 coin")
    elif n == -2:
        coin -=2
        print("You lose 2 coin.. :(")
def tgame():
    import turtle as t
    #Tracker = ts, player = t, point=te
    ts=t.Turtle()
    ts.shape("turtle")
    ts.color("red")
    ts.speed(9)
    ts.up()
    ts.goto(0,200)

    te=t.Turtle()
    te.shape("circle")
    te.color("green")
    te.speed(9)
    te.up()
    te.goto(0,-200)

    def turn_right():
        t.setheading(0)
    def turn_up():
        t.setheading(90)
    def turn_left():
        t.setheading(180)
    def turn_down():
        t.setheading(270)

    def start():
        global playing
        if playing == False:
            playing == True
            t.clear()
            play()

    def play():
        ts.goto(0,200)
        t.goto(0,0)
        global score
        global playing
        while(True):
            if random.randint(1,5) == 3:
                ang = ts.towards(t.pos())
                ts.setheading(ang)
            speed=score/2 +0.5
            t.forward(3+score/2)
            if speed > 15:
                speed =15
            ts. forward(speed)

            if t.distance(ts)<12:
                text = "Score:" +str(score)
                message("Game Over", text)
                playing = False
                score =0
                break
                t.exitonclick()
            if t.distance(te)<13:
                score = score + 1
                t.write(score,font=("Arial",10))      
                star_x = random.randint(-230,230)    
                star_y = random.randint(-230,230)
                te.goto(star_x,star_y)    
            if playing:
                t.ontimer(play,100)

    def message(m1,m2):
        t.clear()
        t.goto(0,100)
        t.write(m1,False,"center",font=('OCR A Extended',30))
        t.goto(0,-100)
        t.write(m2,False,"center",font=('Arial',25))
        t.home()

    t.title("Turtle Game")
    t.setup(600,700)
    t.bgcolor("gray")
    t.shape("turtle")
    t.speed(9)
    t.up()
    t.color("white")
    t.onkeypress(turn_right, "Right")
    t.onkeypress(turn_up, "Up")
    t.onkeypress(turn_left, "Left")
    t.onkeypress(turn_down, "Down")
    t.onkeypress(start, "space")

    t.listen()
    message("Turtle Game","[Press Space To Start]")

def baseball(): #Game_Founction 2
    time.sleep(1)
    print("==============================================================================")
    print("숫자 야구 게임 시작!")
    print("1~9까지 숫자로 구성된 4자리 숫자를 맞추세요.")
    print("Ex)2648 띄여쓰기 없이 입력해주세요.")
    time.sleep(1)
    print("\n     ---------------------------주의사항-----------------------------     \n")
    print("코인은 시도 횟수에 따라 차등 지급됩니다.")
    time.sleep(1)
    print("1~4회 : +2     5~9회 : +1     10회~14회 : 0    15~19회 : -1     20~ : -2")
    print("==============================================================================")
    # 랜덤으로 4자리 숫자 만들기
    number = list()

    while len(number) != 4:
        # randint(a, b) 함수는 a, b사이의 랜덤한 정수를 반환하는 함수
        new_number = random.randint(1, 9)
        if new_number not in number:
            number.append(new_number)

    # 변수 선언하기
    strike = 0
    count = 0

    while strike != 4:
        your_answer = input("서로 다른 숫자 4개를 입력하세요 : ")

        count += 1
        strike = 0
        ball = 0

        # strike, ball 검사하기(enumerate 함수는 인터넷 참고했습니다.)
        for index, value in enumerate(your_answer):
            # 숫자와 숫자의 위치가 동일할 때
            if int(value) == number[index]:
                strike += 1
            # 숫자만 동일하고 위치가 다를 때
            elif int(value) in number:
                ball += 1
        # 숫자 4개 모두 겹치지 않을 때
        if strike == 0 and ball == 0:
            print("아웃!")
        else:
            print(strike ,"스트라이크", ball, "볼입니다.")
        
    print(count,"번만에 정답을 맞추셨습니다!")
    if count<5:
        return 2
    elif count>4 and count<10:
        return 1
    elif count>9 and count<15:
        return 0
    elif count>14 and count<20:
        return -1
    elif count>19:
        return -2

#Main
print("=================================================================================================")
print("____    _      ____   _______    ___        ________.   _______    .___    ___.   ________. ")
print("＼ ＼  / ＼  /   /   |   ____|  |   |      /        |  /  ____ ＼  |   ＼/    |  |   _____|")
print(" ＼ ＼/   ＼/   /    |  |____   |   |      |   ,----'  |  |   | |  |  |＼  /  |  |   |__ ")
print("  ＼           /     |  _____|  |   |      |  |        |  |   | |  |  | ＼/|  |  |    __|")
print("   ＼   /＼   /      |  |_____  |   `---.  |  `----.   |  `--'  |  |  |    |  |  |   |____")
print("    ＼_/  ＼_/       |_______|  |_______|  ＼______|   ＼_______/  |__|    |__|  |________|")
print("=================================================================================================")
coin=int(input("Insert Coin: "))
print("\nPlease Wait")
#loading()

while (coin>0):
    print("\n1. Turtle(코드 문제로 1회만 이용 가능)     2. 숫자야구     3. Check My Coin     4. Quit")
    game_button=int(input("Choose The Game: "))
    if game_button==1:
        print("===================================================")
        print("방향키로 거북이의 방향을 바꿀 수 있습니다.")
        print("게임 종료 시 창을 닫아주세요.")
        print("===================================================")
        time.sleep(1)
        coin-=1
        loading2()
        score =0
        playing=False
        tgame() #Function position
        
    elif game_button==2:
        coin-=1
        loading2()
        r=baseball() #Function2 call
        cal_coin(r)
    elif game_button==3:
        print("\nLeft Coin : " + str(coin))
    elif game_button==4:
        print("\nClosing The Game")
        loading()
        print("Return Coin : " + str(coin))
        coin=-1
        
print("\n~GAME OVER~")

