
def randomize():
    for i in range(2):
        for j in range(10):
            card_a = random.randint(0,8)
            card_b = random.randint(0,8)
            tmp = card[i][card_a]
            card[i][card_a] = card[i][card_b]
            card[i][card_b] = tmp
    return

def check(select_t,select_l):
    if card[0][select_t] == card[1][select_l]:
        card_t[select_t] = card[0][select_t]
        card_l[select_l] = card[1][select_l]
        return True
    else:
        return False
def add_memory(select_t,select_l):
    if len(comp_memory0)+len(comp_memory1) < 5:
        if not ([select_t,card[0][select_t]] in comp_memory0):
            comp_memory0.append([select_t,card[0][select_t]])
        if not([select_l,card[1][select_l]] in comp_memory1):
            comp_memory1.append([select_l,card[1][select_l]])
    return

def del_memory(select_t,select_l):
    for i in range(len(comp_memory0)):
        if comp_memory0[i][0] == select_t:
            del comp_memory0[i]
            break

    for j in range(len(comp_memory1)):
        if comp_memory1[j][0] == select_l:
            del comp_memory1[j]
            break
    return

def display():
    print("現在の勝利:",num_of_wins,"勝",num_of_losses,"敗")
    print("現在のカードの状況")
    print(card_t)
    print(card_l)
    print()
    return

def yours_turn(num_of_wins):
    while True:
        text = input("上のカードの場所を選んでください")
        if text.isdigit():
            select_t = int(text) - 1
            if 0 <= select_t <= 8:
                break
        print("0~9で入力してください")
            
    while True:
        if card_t[select_t] == "*":
            break
        text = input("その場所のカードはすでにペアになっています。選びなおしてください。")
        if text.isdigit():
            select_t = int(text) - 1
            if 0 <= select_t <= 8:
                break
        print("０～９で入力してください")
    print("上の(場所、カード):","(",select_t+1,",",card[0][select_t],")")
    while True:
        text = input("下のカードの場所を選んでください")
        if text.isdigit():
            select_l = int(text) - 1
            if 0 <= select_l <= 8:
                break
        print("0~9で入力してください")
    
    while True:
        if card_l[select_l] == "*":
            break
        text = input("その場所のカードはすでにペアになっています。選びなおしてください")
        if text.isdigit():
            select_l = int(text) - 1
            if 0 <= select_l <= 8:
                break
        print("0~9で入力してください")
    print("下の(場所、カード):","(",select_l+1,",",card[1][select_l],")")
    if check(select_t,select_l):
        num_of_wins += 1
        print("あたり")
        del_memory(select_t,select_l)
    else:
        print("はずれ")
        add_memory(select_t,select_l)
    return num_of_wins
def comp_turn(num_of_losses):
    found_ans = False
    for i in range(len(comp_memory0)):
        for j in range(len(comp_memory1)):
            if comp_memory0[i][1] == comp_memory1[j][1]:
                select_t = comp_memory0[i][0]
                select_l = comp_memory1[j][0]
                found_ans = True
                break
        if found_ans:
            break

    if not(found_ans):
        while True:
            select_t = random.randint(0,8)
            if card_t[select_t] == "*":
                break
        found_mem = False
        for j in range(len(comp_memory1)):
            if card_t[select_t] == comp_memory1[j][1]:
                select_l = comp_memory1[j][0]
                found_mem = True
        if not(found_mem):
            while True:
                select_l = random.randint(0,8)
                if card_l[select_l] == "*":
                    break
    print("上の（場所、カード）:","(",select_t+1,",",card[0][select_t],")")
    print("下の（場所、カード）：","(",select_l+1,",",card[1][select_l],")")
    if check(select_t,select_l):
        num_of_losses += 1
        print("あたり")
        del_memory(select_t,select_l)
        return num_of_losses
    else:
        print("はずれ")
        add_memory(select_t,select_l)
        return num_of_losses

import random 
from IPython.display import clear_output
card = [["1","2","3","4","5","6","7","8","9"],["1","2","3","4","5","6","7","8","9"]]
randomize()
card_t = ["*"] * 9
card_l =["*"] * 9
num_of_wins = 0
num_of_losses = 0
comp_memory0 = []
comp_memory1 = []
turn = random.randint(1,2)
while num_of_wins + num_of_losses < 9 :
    if turn % 2 == 0:
        clear_output(True)
        print("コンピュータのターン")
        num_of_losses = comp_turn(num_of_losses)
        display()
        turn += 1
    else:
        print("あなたのターン")
        display()
        num_of_wins = yours_turn(num_of_wins)
        turn += 1
        input("Enterで次のターンへ")
print("ゲーム終了：",num_of_wins,"勝",num_of_losses,"敗")
if num_of_wins > num_of_losses:
    print("あなたの勝ち")
else:
    print("コンピュータの勝ち")



    

        
