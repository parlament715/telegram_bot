from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, StateFilter
from app.keyboard import kb1, kb2, kb3
from aiogram import F
from aiogram.fsm.context import FSMContext
from app.database.request import to_write

date = 0
router = Router( )


@router.message(CommandStart())
async def cmd_start(message :Message):
    await message.answer('Привет',reply_markup=kb1)


@router.message(F.text == 'Я старший воспитатель')
async def first_keyboard_reaction(message : Message):
    await message.answer('Посмотреть информацию?', reply_markup=kb2 )

@router.message(F.text == 'Я воспитатель')
async def second_keyboard_reaction(message : Message, state : FSMContext):
    await state.set_state('step 1')
    await message.answer('snnsjnsjnsd',reply_markup=kb2)
    date = 1
    print(date)

@router.message(StateFilter('step 1'))
async def accept_state(messege : Message, state : FSMContext):
    # await state.update_data(messege.text)
    await messege.answer("skdjksdjf",reply_markup=kb3)
    # await state.rename_state_to("step 2")


