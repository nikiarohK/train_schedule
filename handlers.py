from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


router = Router()

class Path(StatesGroup):
    start_point = State()
    end_point = State()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"Привет {message.from_user.full_name} !\nВыбери нужный диаметр",reply_markup=kb.start_menu)


@router.message(F.text.in_({"МЦД-1", "МЦД-2", "МЦД-3", "МЦД-4"}))
async def start_pos(message: Message, state: FSMContext):
    if message.text == "МЦД-1":
        await state.set_state(Path.start_point)
        await message.answer("Выбери начальную станцию")
        
    elif message.text == "МЦД-2":
        await state.set_state(Path.start_point)
        await message.answer("Выбери начальную станцию")
        
    elif message.text == "МЦД-3":
        await state.set_state(Path.start_point)
        await message.answer("Выбери начальную станцию")
        
    elif message.text == "МЦД-4":
        await state.set_state(Path.start_point)
        await message.answer("Выбери начальную станцию")    
    
    
@router.message(Path.start_point)
async def end_pos(message: Message, state: FSMContext):
    await state.update_data(start_point = message.text)
    await state.set_state(Path.end_point)
    await message.answer("Выбери конечную станцию")
    

@router.message(Path.end_point)
async def finish_pos(message: Message, state: FSMContext):
    await state.update_data(end_point = message.text)
    data = await state.get_data()
    await message.answer(f"Блиайшая электричка от {data['start_point']} до {data['end_point']}")
    await state.clear()