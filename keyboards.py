from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

class Kb:
    def __init__(self, *args):
        self.titles = list(args)

    def make_keyboard(self):
        buttons = []
        for title in self.titles:
            buttons.append([KeyboardButton(text = title)])
        kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=buttons) 
        return kb


choose_diametr = Kb("МЦД-1", "МЦД-2", "МЦД-3", "МЦД-4").make_keyboard()
diametr1 = None
diametr2 = Kb("Подольск", "Силикатная", "Остафьево", "Щербинка", "Бутово", "Битца", "Красный строитель", "Покровская", "Котляково", "Царицыно", "Москворечье", "Курьяново", "Перерва", "Депо", "Люблино", "Печатники", "Текстильщики", "Новохохловская", "Калитники", "Москва-Товарная", "Курский вокзал", "Каланчевская", "Ржевская", "Марьина роща", "Дмитровская", "Гражданская", "Красный балтиец", "Стрешнево", "Щукинская", "Тушино", "Трикотажная", "Волоколамская", "Пенягино", "Павшино", "Красногорская", "Опалиха", "Аникеевка", "Нахабино").make_keyboard()
diametr3 = None
diametr4 = None