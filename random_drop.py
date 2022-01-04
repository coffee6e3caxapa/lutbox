from lutbox.priz import *
import random
from lutbox.lutbox_wot import *
from tkinter import messagebox

class Gamer:
    money: int = 500
    lutbox: dict = {'nov_god': 0,
                    'christ_year': 0,
                    'east_year': 0,
                    'magic_year': 0
                    }
    supply = {
        'gold': 0,
        'silver': 0,
        'premium_days': 0
    }

    tanks_high_lvl_2022 = {}
    tanks_low_lvl_2020 = {}
    style3d = {}

class Drop_items:
    count = 1
    count2 = 1
    def tanks_8_lvl(self):
        if random.random() <= 0.024:
            prize_high_tank = random.choice(lst_tanks_high_lvl_2022)
            print(prize_high_tank)
            if prize_high_tank not in Gamer.tanks_high_lvl_2022: # Статистика выпадений
                Gamer.tanks_high_lvl_2022[prize_high_tank]=1
            else:
                if len(Gamer.tanks_high_lvl_2022) <= len(lst_tanks_high_lvl_2022):  # Блок проверки
                    if prize_high_tank in Gamer.tanks_high_lvl_2022:
                        while prize_high_tank in Gamer.tanks_high_lvl_2022:
                            prize_high_tank = random.choice(lst_tanks_high_lvl_2022)
                        Gamer.tanks_high_lvl_2022[prize_high_tank] = 1
                else:
                    if prize_high_tank in Gamer.tanks_high_lvl_2022:
                        Gamer.tanks_high_lvl_2022[prize_high_tank] +=1
                        Gamer.supply['gold'] += 10000
            #messagebox.showinfo('Выйгрыш', f'Танк 8 уровня {prize_high_tank}')
        elif Drop_items.count == 50:
            prize_high_tank = random.choice(lst_tanks_high_lvl_2022)
            if prize_high_tank not in Gamer.tanks_high_lvl_2022: # Статистика выпадений
                Gamer.tanks_high_lvl_2022[prize_high_tank]=1
            else:
                if prize_high_tank in Gamer.tanks_high_lvl_2022:
                    if len(Gamer.tanks_high_lvl_2022)<=len(lst_tanks_high_lvl_2022): # Блок проверки
                        while prize_high_tank in Gamer.tanks_high_lvl_2022:
                            prize_high_tank = random.choice(lst_tanks_high_lvl_2022)
                        Gamer.tanks_high_lvl_2022[prize_high_tank] = 1
                    else:
                        Gamer.tanks_high_lvl_2022[prize_high_tank] += 1
                        Gamer.supply['gold'] += 10000
            Drop_items.count = 1
            print(prize_high_tank)
            #messagebox.showinfo('Выйгрыш', f'Танк 8 уровня {prize_high_tank}')

    def tanks_low_lvl(self):
        if random.random() <= 0.1166:
            prize = random.choice(lst_tanks_low_lvl_2022)
            if prize not in Gamer.tanks_low_lvl_2020:
                Gamer.tanks_low_lvl_2020[prize] = 1
            elif prize in Gamer.tanks_low_lvl_2020:
                Gamer.tanks_low_lvl_2020[prize] += 1
                Gamer.supply['gold'] += 1000
            print(prize)

    def style3d(self):
        if random.random() <= 0.05:
            prize = random.choice(style3D)
            print(prize)
            if prize not in Gamer.style3d:
                Gamer.style3d[prize] = 1
            elif prize in Gamer.style3d:
                if len(Gamer.style3d) < len(style3D): # Блок проверки
                    while prize in Gamer.style3d:
                        prize = random.choice(style3D)
                    Gamer.style3d[prize] = 1
                else:
                    Gamer.style3d[prize]+=1

            #messagebox.showinfo('Выйгрыш', f'3D тиль на танк {prize}')

    def add_drop(self):
        if random.random() <= 0.8594:
            prize = (lst_premium_days + golds_tuple + silvers_tuple)
            prize = random.choice(prize)
            print(prize[1])
            if prize[2] in Gamer.supply:
                Gamer.supply[prize[2]] += prize[0]

    def drop(self):
        exit = ''
        while exit != 'Exit':
        #while len(Gamer.tanks_high_lvl_2022)<10:
        #while Drop_items.count<400:
            print('Ваш выйгрыш')
            print('Украшение, ', '250 ед.игрового золота')
            self.add_drop()
            self.tanks_8_lvl()
            self.tanks_low_lvl()
            self.style3d()
            Gamer.supply['gold'] += 250
            print(Gamer.supply)
            for i in (Gamer.tanks_high_lvl_2022,Gamer.tanks_low_lvl_2020,Gamer.style3d):
                if i:
                    print(i)
            print(len(Gamer.tanks_high_lvl_2022))
            print(len(Gamer.style3d))
            # if Gamer.tanks_high_lvl_2022:
            #     print(Gamer.tanks_high_lvl_2022)
            #     print(Gamer.tanks_low_lvl_2020)
            #     print(Gamer.style3d)
            print(Drop_items.count, 'счетчик')
            print(Drop_items.count2, 'счетчик')

            Drop_items.count += 1
            Drop_items.count2 += 1
            exit = input('нажмите любую кнопку для продолжения,введите Exit для выхода')
            print('-' * 10)


# game = Drop_items()
# game.drop()
