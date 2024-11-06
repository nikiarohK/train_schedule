from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import keyboards 
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import sqlite3
from bs4 import BeautifulSoup
import requests



connection = sqlite3.connect('name_stations.db')
cursor = connection.cursor()

router = Router()


class Path(StatesGroup):
    start_point = State()
    end_point = State()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"Привет {message.from_user.full_name} !\nВыбери нужный диаметр", reply_markup=keyboards.choose_diametr)


@router.message(F.text.in_({"МЦД-1", "МЦД-2", "МЦД-3", "МЦД-4"}))
async def start_pos(message: Message, state: FSMContext):
    if message.text == "МЦД-1":
        await state.set_state(Path.start_point)
        await message.answer("Выбери начальную станцию", reply_markup=keyboards.diametr1)
        
    elif message.text == "МЦД-2":
        await state.set_state(Path.start_point)
        await message.answer("Выбери начальную станцию", reply_markup=keyboards.diametr2)
        
    elif message.text == "МЦД-3":
        await state.set_state(Path.start_point)
        await message.answer("Выбери начальную станцию", reply_markup=keyboards.diametr3)
        
    elif message.text == "МЦД-4":
        await state.set_state(Path.start_point)
        await message.answer("Выбери начальную станцию", reply_markup=keyboards.diametr4)    
    
    
@router.message(Path.start_point)
async def end_pos(message: Message, state: FSMContext):
    await state.update_data(start_point = message.text)
    await state.set_state(Path.end_point)
    await message.answer("Выбери конечную станцию")
    

@router.message(Path.end_point)
async def finish_pos(message: Message, state: FSMContext):
    await state.update_data(end_point = message.text)
    
    data = await state.get_data()
    url = await make_url(data['start_point'], data['end_point'])
    await get_time(url)
    await message.answer(f"Блиайшая электричка от {str(data['start_point']).lower()} до {str(data['end_point']).lower()}", reply_markup=keyboards.choose_diametr)
    await state.clear()
    
    
async def make_url(start_point_name, end_point_name):
    
    cursor.execute('SELECT title_for_url FROM diametr2 WHERE title = ?', (start_point_name,))
    start = cursor.fetchall()

    cursor.execute('SELECT title_for_url FROM diametr2 WHERE title = ?', (end_point_name,))
    end = cursor.fetchall()
    
    return f"https://rasp.yandex.ru/suburban/{start[0][0]}--{end[0][0]}/today"

async def get_time(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    block = soup.find_all("tr")
    print(block)

