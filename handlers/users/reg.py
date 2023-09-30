from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from handlers.users.start import bot_start
from keyboards.default.reg_key import cancel_key, loc
from loader import dp, db
from states.State import RegistrationStates


@dp.message_handler(state=RegistrationStates.waiting_for_phone_number, content_types=types.ContentType.CONTACT)
async def process_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tgid'] = message['from']['id']
        data['phone_number'] = message['contact']['phone_number']

    await message.reply("Isminggizni kiriting:", reply_markup=cancel_key())
    await RegistrationStates.waiting_for_name.set()


@dp.message_handler(state=RegistrationStates.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    # Ask for location
    await message.reply("Ajoyib! Endi manzilinggizni jo'nating", reply_markup=loc())
    await RegistrationStates.waiting_for_location.set()


@dp.message_handler(content_types=types.ContentTypes.LOCATION, state=RegistrationStates.waiting_for_location)
async def process_location(message: types.Message, state: FSMContext):
    # Save location in state
    location = message.location
    async with state.proxy() as data:
        data['latitude'] = location.latitude
        data['longitude'] = location.longitude

    # Retrieve data from state
    db.add_user(name=data['name'],
                 phone_number=data['phone_number'],
                 longitude=data['longitude'],
                 latitude=data['latitude'],
                 tgid=message.from_id)

    await state.finish()

    await message.reply("Ro'yxatdan o'tganinggiz uchun rahmat!",
                        reply_markup=ReplyKeyboardRemove())
    await bot_start(message=message)
