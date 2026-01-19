import random
import tkinter as tk


# =====================
# Model（ロジック）
# =====================

class Character:
    def __init__(self, hp, mp=0):
        self.hp = hp
        self.mp = mp

    def is_dead(self):
        return self.hp <= 0


class Player(Character):
    def attack(self, damage):
        return damage()

    def use_mp(self, cost):
        if self.mp < cost:
            return False
        self.mp -= cost
        return True


class Monster(Character):
    def attack(self):
        return random.randint(1, 2)


# =====================
# Game
# =====================

class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG")
        self.root.geometry("300x200")

        self.attacks = {
            "blade": lambda: random.randint(1, 2),
            "magic": lambda: random.randint(0, 0),
            "jump": lambda: random.randint(1, 2),
            "care": lambda: random.randint(5, 7),
        }

        monster_data = {
            "slime": lambda: random.randint(5, 6),
            "goblin": lambda: random.randint(4, 6),
        }

        name, hp_func = random.choice(list(monster_data.items()))
        self.monster = Monster(hp_func())
        self.player = Player(hp=10, mp=10)
        self.monster_name = name

        self.create_widgets()

    # -----------------
    # UI
    # -----------------

    def create_widgets(self):
        self.narrator = tk.Label(self.root, text="monster spawn")
        self.narrator.place(relx=0.5, rely=0.08, anchor="center")

        self.monster_label = tk.Label(self.root, text=self.monster_name)
        self.monster_label.place(relx=0.5, rely=0.18, anchor="center")

        self.monster_hp_label = tk.Label(self.root, text=f"HP {self.monster.hp}")
        self.player_label = tk.Label(
            self.root, text=f"HP {self.player.hp} MP {self.player.mp}"
        )
        self.player_label.place(relx=0.5, rely=0.37, anchor="center")

        self.message = tk.Label(self.root, text="")
        self.message.place(relx=0.5, rely=0.27, anchor="center")

        self.btn_fight = tk.Button(self.root, text="fight", command=self.start_fight)
        self.btn_run = tk.Button(self.root, text="run away", command=self.run_away)

        self.btn_fight.place(relx=0.4, rely=0.5, anchor="center")
        self.btn_run.place(relx=0.6, rely=0.5, anchor="center")

        self.attack_buttons = [
            tk.Button(self.root, text="blade", command=lambda: self.turn("blade")),
            tk.Button(self.root, text="magic", command=lambda: self.turn("magic", 2)),
            tk.Button(self.root, text="jump", command=lambda: self.turn("jump")),
            tk.Button(self.root, text="care", command=lambda: self.turn("care", 2, heal=True)),
        ]

    # -----------------
    # Game Flow
    # -----------------

    def start_fight(self):
        self.narrator.place_forget()
        self.btn_fight.place_forget()
        self.btn_run.place_forget()
        self.monster_hp_label.place(relx=0.5, rely=0.1, anchor="center")

        positions = [(0.4, 0.5), (0.6, 0.5), (0.4, 0.7), (0.6, 0.7)]
        for btn, (x, y) in zip(self.attack_buttons, positions):
            btn.place(relx=x, rely=y, anchor="center")

    def run_away(self):
        self.clear_screen()
        tk.Label(self.root, text="You ran away").place(relx=0.5, rely=0.3, anchor="center")

    def turn(self, attack_name, mp_cost=0, heal=False):
        if mp_cost and not self.player.use_mp(mp_cost):
            self.message.config(text="Not enough MP")
            return

        if heal:
            self.player.hp += self.attacks[attack_name]()
        else:
            self.monster.hp -= self.player.attack(self.attacks[attack_name])

        if self.check_end():
            return

        damage = self.monster.attack()
        self.player.hp -= damage
        self.message.config(text=f"Monster Attack HP-{damage}")

        self.update_ui()
        self.check_end()

    # -----------------
    # Utils
    # -----------------

    def update_ui(self):
        self.monster_hp_label.config(text=f"HP {self.monster.hp}")
        self.player_label.config(text=f"HP {self.player.hp} MP {self.player.mp}")

    def check_end(self):
        if self.player.is_dead():
            self.clear_screen()
            tk.Label(self.root, text="You are Dead!!!").place(
                relx=0.5, rely=0.27, anchor="center"
            )
            return True

        if self.monster.is_dead():
            self.clear_screen()
            tk.Label(self.root, text="Monster defeat!!!\nYou win !!!").place(
                relx=0.5, rely=0.08, anchor="center"
            )
            tk.Label(self.root, text="Thank you playing!!!!!!").place(
                relx=0.5, rely=0.3, anchor="center"
            )
            return True

        return False

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# =====================
# main
# =====================

root = tk.Tk()
RPGGame(root)
root.mainloop()
