import tkinter as tk
from random import shuffle
from random import *
from tkinter.messagebox import showinfo, showerror
from tkinter import messagebox
from priz import *
import random


class Gamer:
    money: int = 500000
    lutbox: dict = {'nov_god': 0,
              'christ_year': 0,
              'east_year': 0,
              'magic_year': 0
              }

    supply: dict = {
        'gold': 0,
        'silver': 0,
        'premium_days': 0
    }
    tanks_high_lvl_2022: dict = {}
    tanks_low_lvl_2020: dict = {}
    style3d: dict = {}
    sum_lutbox: int = 0
    IS_GAME_OVER = True


class Lutbox:
    win = tk.Tk()
    win.geometry(f'630x550+50+50')
    win['bg'] = '#B72E8E'
    win.title('Lutbox_WoT')
    win.resizable(False, False)
    years: dict = {1: 'nov_god',
                   2: 'christ_year',
                   3: 'east_year',
                   4: 'magic_year'}

    def __init__(self):
        pass

    def open_toplevel(self):
        """ Создает дополнительное окна по нажатию кнопки начать розыгрыш
        в окне производится игра открытия новогодних коробок"""
        self.win_2 = tk.Toplevel()
        self.win_2.geometry('850x400+700+50')
        self.win_2.title('Открытие новогодних коробок')
        self.win_2.resizable(False, False)
        self.win_2['bg'] = '#B72E8E'
        self.win_2.grab_set()

        save_btn = tk.Button(self.win_2, text='Открыть', bg='#000000', fg='#FF0404', command=games.drop)
        save_btn.grid(row=3, column=0, columnspan=2, stick='wens', padx=5, pady=5)

        lbl = tk.Label(self.win_2, text='Открытие Новогодних коробок', bg='#000000', fg='#FF0404')
        lbl.grid(row=0, column=0, columnspan=6, stick='wens', padx=5, pady=5)



        self.tanks_high = tk.Label(self.win_2,text='', bg='#B72E8E', fg='#FF0404')
        self.tanks_high.grid(row=1, column=0, columnspan=1, stick='wens', padx=5, pady=5)
        self.tanks_low = tk.Label(self.win_2, text='', bg='#B72E8E', fg='#FF0404')
        self.tanks_low.grid(row=1, column=1, columnspan=1, stick='wens', padx=5, pady=5)
        self.style = tk.Label(self.win_2, text='', bg='#B72E8E', fg='#FF0404')
        self.style.grid(row=1, column=2, columnspan=1, stick='wens', padx=5, pady=5)
        self.add_prize = tk.Label(self.win_2, text='', bg='#B72E8E', fg='#FF0404')
        self.add_prize.grid(row=1, column=3, columnspan=1, stick='wens', padx=5, pady=5)
        tk.Label(self.win_2, text='250 золота', bg='#000000', fg='#FF0404').grid(row=1,column=4,stick='wens',padx=5,pady=5)
        tk.Label(self.win_2, text='Украшение', bg='#000000', fg='#FF0404').grid(row=1,column=5,stick='wens',padx=5,pady=5)

        self.lbl2 = tk.Label(self.win_2, text=f'Коробок осталось ({Gamer.sum_lutbox})', bg='#000000', fg='#FF0404')
        self.lbl2.grid(row=3, column=2, columnspan=4, stick='wens', padx=5, pady=5)

        for i in range(6):
            tk.Label(self.win_2,text='Здесь располагается \nваш выйгрыш', bg='#000000', fg='#FF0404').grid(row=2, column=i, stick='wens',padx=5,pady=5)

        for i in range(3):
            self.win_2.grid_columnconfigure(0, minsize=150)
            self.win_2.grid_columnconfigure(i,minsize=100)
            self.win_2.grid_rowconfigure(i, minsize=100)


    def open_prize(self,prize: str):
        return self.tanks_high.config(text=prize, bg='#000000', fg='#FF0404')

    def open_style(self, prize: str):
        return self.style.config(text=prize, bg='#000000', fg='#FF0404')

    def open_tanks_low(self, prize: str):
        return self.tanks_low.config(text=prize, bg='#000000', fg='#FF0404')

    def open_add_prize(self, prize: str):
        return self.add_prize.config(text=f'{prize}', bg='#000000', fg='#FF0404')

    def clear_screen(self):
         self.tanks_high.config(text='', bg='#B72E8E', fg='#FF0404')
         self.style.config(text='', bg='#B72E8E', fg='#FF0404')
         self.tanks_low.config(text='', bg='#B72E8E', fg='#FF0404')
         self.add_prize.config(text='', bg='#B72E8E', fg='#FF0404')



    def create_label(self):
        """Создание лейблов наличия коробок"""
        self.choise = tk.Label(Lutbox.win, text='Выберите какую коробку вы хотите купить', bg='#000000', fg='#FF0404')
        self.choise.grid(row=0, column=0, columnspan=5, stick='wens', padx=5)
        self.total = tk.Label(Lutbox.win, text='Осталось коробок всего (0)', bg='#000000', fg='#FF0404')
        self.total.grid(row=5, column=2, columnspan=2, stick='wens', padx=5, pady=10)
        self.box_ng = tk.Label(Lutbox.win, text='В наличии Новогодних \n коробок (0)', bg='#000000', fg='#FF0404')
        self.box_ng.grid(row=4, column=0, stick='wens', padx=5, pady=10)
        self.box_christmas = tk.Label(Lutbox.win, text='В наличии Рождественских \n коробок (0)', bg='#000000',
                                      fg='#FF0404')
        self.box_christmas.grid(row=4, column=1, stick='wens', padx=5, pady=10)
        self.box_east = tk.Label(Lutbox.win, text='В наличии Восточных \n коробок (0)', bg='#000000', fg='#FF0404')
        self.box_east.grid(row=4, column=2, stick='wens', padx=5, pady=10)
        self.box_magic = tk.Label(Lutbox.win, text='В наличии Волшебных \n коробок (0)', bg='#000000', fg='#FF0404')
        self.box_magic.grid(row=4, column=3, stick='wens', padx=5, pady=10)

    def create_btn(self):
        """Кнопки покупки коробок"""
        tk.Button(text='Новогодняя коробка 1\nЦена 110р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(1, 1)).grid(row=1, column=0, stick='wens',
                                                                   padx=5, pady=10)
        tk.Button(text='Новогодние коробки 5\nЦена 500р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(5, 1)).grid(row=2, column=0, stick='wens', padx=5,
                                                                   pady=10)
        tk.Button(text='Новогодние коробки 20\nЦена 2000р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(20, 1)).grid(row=3, column=0, stick='wens', padx=5,
                                                                    pady=10)
        tk.Button(text='Рождественская коробка 1\nЦена 110р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(1, 2)).grid(row=1, column=1, stick='wens',
                                                                   padx=5, pady=10)
        tk.Button(text='Рождественские коробки 5\nЦена 500р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(5, 2)).grid(row=2, column=1, stick='wens',
                                                                   padx=5, pady=10)
        tk.Button(text='Рождественские коробки 20\nЦена 2000р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(20, 2)).grid(row=3, column=1, stick='wens',
                                                                    padx=5, pady=10)
        tk.Button(text='Восточная  коробка 1\nЦена 110р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(1, 3)).grid(row=1, column=2, stick='wens', padx=5,
                                                                   pady=10)
        tk.Button(text='Восточные  коробки 5\nЦена 500р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(5, 3)).grid(row=2, column=2, stick='wens', padx=5,
                                                                   pady=10)
        tk.Button(text='Восточные  коробки 20\nЦена 2000р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(20, 3)).grid(row=3, column=2, stick='wens', padx=5,
                                                                    pady=10)
        tk.Button(text='Волшебная коробка 1\nЦена 110р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(1, 4)).grid(row=1, column=3, stick='wens', padx=5,
                                                                   pady=10)
        tk.Button(text='Волшебные коробки 5\nЦена 500р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(5, 4)).grid(row=2, column=3, stick='wens', padx=5,
                                                                   pady=10)
        tk.Button(text='Волшебные коробки 20\nЦена 2000р', bg='#000000', fg='#FF0404',
                  command=lambda: self.add_box_nov_god(20, 4)).grid(row=3, column=3, stick='wens', padx=5,
                                                                    pady=10)
        tk.Button(text='Открыть окно розыгрыша', bg='#000000', fg='#FF0404', command=self.open_toplevel).grid(row=5,
                                                                                                              column=0,
                                                                                                              columnspan=2,
                                                                                                              stick='wens',
                                                                                                              padx=5,pady=10)
        for i in range(6):
            Lutbox.win.grid_columnconfigure(i, minsize=10)  # размер кнопок с номером ряда и колонки
            Lutbox.win.grid_rowconfigure(0, minsize=50)
            Lutbox.win.grid_rowconfigure(i, minsize=100)


    def sum_box(self, box: int):
        """ Подсчет общего количества коробок игрока"""
        Gamer.sum_lutbox += box
        return self.total.config(text=f'Осталось коробок всего ({Gamer.sum_lutbox})')


    def box(self):
        return self.total.config(text=f'Осталось коробок всего ({Gamer.sum_lutbox})'), self.lbl2.config(text=f'Коробок осталось ({Gamer.sum_lutbox})')


    def add_box_nov_god(self, box: int, year: int):
        if box == 1 and Gamer.money >= 110:
            Gamer.lutbox[Lutbox.years[year]] += box
            Gamer.money -= 110
            print(Gamer.money)
        elif box > 2 and box * 100 <= Gamer.money:
            Gamer.lutbox[Lutbox.years[year]] += box
            Gamer.money -= box * 100
            print(Gamer.money)
        elif Gamer.money < box * 110:
            print('Не достаточно денег для покупки коробки')
            showerror('Game over', 'Не достаточно денег для покупки коробок')

        if year == 1:
            self.box_ng.config(text=f"В наличии Новогодних \n коробок ({Gamer.lutbox[Lutbox.years[year]]})")
            print(type(Gamer.lutbox[Lutbox.years[year]]))

        if year == 2:
            self.box_christmas.config(text=f"В наличии Рождественских \n коробок ({Gamer.lutbox[Lutbox.years[year]]})")

        if year == 3:
            self.box_east.config(text=f"В наличии Восточных \n коробок ({Gamer.lutbox[Lutbox.years[year]]})")

        if year == 4:
            self.box_magic.config(text=f"В наличии Волшебных \n коробок ({Gamer.lutbox[Lutbox.years[year]]})")

        self.sum_box(box)
        return Gamer.lutbox[Lutbox.years[year]]

    def reduce_nov_god_box(self):
        if Gamer.lutbox['nov_god']>0:
            Gamer.lutbox['nov_god']-=1
            return self.box_ng.config(text=f"В наличии Новогодних \n коробок ({Gamer.lutbox['nov_god']})")
        elif Gamer.lutbox['christ_year']>0:
            Gamer.lutbox['christ_year']-=1
            return self.box_christmas.config(text=f"В наличии Рождественских \n коробок ({Gamer.lutbox['christ_year']})")
        elif Gamer.lutbox['east_year']>0:
            Gamer.lutbox['east_year']-=1
            return self.box_east.config(text=f"В наличии Восточных \n коробок ({ Gamer.lutbox['east_year']})")
        elif Gamer.lutbox['magic_year']>0:
            Gamer.lutbox['magic_year']-=1
            return self.box_magic.config(text=f"В наличии Волшебных \n коробок ({Gamer.lutbox['magic_year']})")

    def start(self):
        self.create_label()
        self.create_btn()
        Lutbox.win.mainloop()


class Drop_items:
    count = 1
    count2 = 1

    def tanks_8_lvl(self):
        if random.random() <= 0.024:
            prize_high_tank = random.choice(lst_tanks_high_lvl_2022)
            print(prize_high_tank)
            if prize_high_tank not in Gamer.tanks_high_lvl_2022:  # Статистика выпадений
                Gamer.tanks_high_lvl_2022[prize_high_tank] = 1
            else:
                if len(Gamer.tanks_high_lvl_2022) <= len(lst_tanks_high_lvl_2022):  # Блок проверки
                    if prize_high_tank in Gamer.tanks_high_lvl_2022:
                        while prize_high_tank in Gamer.tanks_high_lvl_2022:
                            prize_high_tank = random.choice(lst_tanks_high_lvl_2022)
                        Gamer.tanks_high_lvl_2022[prize_high_tank] = 1
                else:
                    if prize_high_tank in Gamer.tanks_high_lvl_2022:
                        Gamer.tanks_high_lvl_2022[prize_high_tank] += 1
                        Gamer.supply['gold'] += 10000
            messagebox.showinfo('Выйгрыш', f'Танк 8 уровня {prize_high_tank}')
        elif Drop_items.count == 50:
            prize_high_tank = random.choice(lst_tanks_high_lvl_2022)
            if prize_high_tank not in Gamer.tanks_high_lvl_2022:  # Статистика выпадений
                Gamer.tanks_high_lvl_2022[prize_high_tank] = 1
            else:
                if prize_high_tank in Gamer.tanks_high_lvl_2022:
                    if len(Gamer.tanks_high_lvl_2022) <= len(lst_tanks_high_lvl_2022):  # Блок проверки
                        while prize_high_tank in Gamer.tanks_high_lvl_2022:
                            prize_high_tank = random.choice(lst_tanks_high_lvl_2022)
                        Gamer.tanks_high_lvl_2022[prize_high_tank] = 1
                    else:
                        Gamer.tanks_high_lvl_2022[prize_high_tank] += 1
                        Gamer.supply['gold'] += 10000
            Drop_items.count = 1
            print(prize_high_tank)
            messagebox.showinfo('Выйгрыш', f'Танк 8 уровня {prize_high_tank}')
            return Lutbox.open_prize(a,prize_high_tank)

    def tanks_low_lvl(self):
        if random.random() <= 0.1166:
            prize = random.choice(lst_tanks_low_lvl_2022)
            if prize not in Gamer.tanks_low_lvl_2020:
                Gamer.tanks_low_lvl_2020[prize] = 1
            elif prize in Gamer.tanks_low_lvl_2020:
                Gamer.tanks_low_lvl_2020[prize] += 1
                Gamer.supply['gold'] += 1000
            print(prize)
            return Lutbox.open_tanks_low(a,prize)

    def style3d(self):
        if random.random() <= 0.05:
            prize = random.choice(style3D)
            print(prize)
            if prize not in Gamer.style3d:
                Gamer.style3d[prize] = 1
            elif prize in Gamer.style3d:
                if len(Gamer.style3d) < len(style3D):  # Блок проверки
                    while prize in Gamer.style3d:
                        prize = random.choice(style3D)
                    Gamer.style3d[prize] = 1
                else:
                    Gamer.style3d[prize] += 1
            Lutbox.open_style(a,prize)

            messagebox.showinfo('Выйгрыш', f'3D тиль на танк {prize}')

    def add_drop(self):
        if random.random() <= 0.8594:
            prize = (lst_premium_days + golds_tuple + silvers_tuple)
            prize = random.choice(prize)
            print(prize[1])
            if prize[2] in Gamer.supply:
                Gamer.supply[prize[2]] += prize[0]
            return Lutbox.open_add_prize(a,prize[1])

    def drop(self):

        if Gamer.sum_lutbox <= 0:
            Gamer.IS_GAME_OVER=False

        if Gamer.sum_lutbox:
            print('Ваш выйгрыш')
            print('Украшение, ', '250 ед.игрового золота')
            Lutbox.clear_screen(a)
            self.add_drop()
            self.tanks_8_lvl()
            self.tanks_low_lvl()
            self.style3d()
            Gamer.supply['gold'] += 250
            print(Gamer.supply)
            for i in (Gamer.tanks_high_lvl_2022, Gamer.tanks_low_lvl_2020, Gamer.style3d):
                if i:
                    print(i)
            print(len(Gamer.tanks_high_lvl_2022))
            print(len(Gamer.style3d))
            print(Drop_items.count, 'счетчик')
            print(Drop_items.count2, 'счетчик')
            Drop_items.count += 1 # Счетчик до 100% выпадения танка 8 уровня
            Drop_items.count2 += 1  # Просто счетчик
            Gamer.sum_lutbox -= 1 # Уменьшенин числа коробок
            Lutbox.box(a)  # Возвращает остаток коробок
            Lutbox.reduce_nov_god_box(a)
            # exit = input('нажмите любую кнопку для продолжения,введите Exit для выхода')
            print('-' * 10)
        else:
            print('У вас закончились новогодние коробки')
            messagebox.showinfo('Game Over', 'У вас закончились коробки')


a = Lutbox()
games = Drop_items()
a.start()
