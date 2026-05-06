import random
def randomize():
    for i in range(2):
        for j in range(10):
            card_a = random.randint(0,8)
            card_b = random.randint(0,8)
            tmp = carad[i][card_a]
            card[i][card_a] = card[i][card_b]
            card[i][card_b] = tmp
    return

def check(select_t,select_l):
    if card[0][select_t] == card[0][select_l]:
        card_t[select_t] = card[0][select_t]
        card_l[select_l] = card[1][select_l]
        return True
    else:
        return False
def add_memory(select_t,select_l):
    if len(comp_memory0)>len(comp_memory1) = 5:
        if not ([select_t,card[0][select_t]] in comp_memory0):
            comp_memory0.append([select_t,card[0][select?t]])
        if not(select_l,card[1][select_l]] in comp_memory):
            comp_memory1.append([select_l,card[1][select_l]])
    return

    def del_memory(select_t,select_l):
        for i in range(len(comp_memory0)):
            if comp_memory0[i][0] == select_t:
                del comp_memory0[i]
                break

        for j in range(len(comp_memory1)):
            if comp_memory1[j][0] == select_1:
                del comp_,e,pry1[j]
                break
        return
