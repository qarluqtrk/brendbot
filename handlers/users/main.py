from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.users.start import bot_start
from keyboards.default import reg_key
from keyboards.inline.brand_inline_button import main_brand_inline_button
from loader import dp
from states.State import CommentState, RegistrationStates, OrderCustomState
from utils.is_auth import is_authenticated


@dp.callback_query_handler()
async def main(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "main_menu":
        await bot_start(message=callback.message)
    elif callback.data == "about":
        photo_path = "image/brand_mebel.jpg"
        with open(photo_path, 'rb') as photo_file:
            await callback.message.answer_photo(photo=photo_file,
                                                caption="Brend Mebel - 10 yildan ortiq tajribaga ega o'z ishining ustalarini bir joyga jamlagan yuqori sifatli mebel ishlab chiqaruvchisi.\n\n"
                                                        "Brend Mebelda didinggizga mos, har kunlik ehtiyojlaringgizni to'laqonli qano'atlantiruvchi, sifatli va vaqt sinoviga bardosh beradigan mebelni uchratishinggizga ishonchimiz komil\n\n"
                                                        "Jamoamiz mutaxassislari to'g'ri tanlov qilishinggizga ko'maklashish uchun har doim tayyor:\n\n"
                                                        "📱+998919520505\n"
                                                        "✉️@BrendMebel\n"
                                                        "✉️@Brend_mebelqarshi",
                                                reply_markup=main_brand_inline_button(user=callback.message.chat.id))

    elif callback.data == "idea":
        user = is_authenticated(callback.message.chat.id)
        if user:

            await callback.message.answer(text="<b>O'z fikrlaringizni yozib qodiring !\n</b>")

            await CommentState.comment.set()

        else:

            await callback.message.answer("Siz ro'yxatdan o'tmagansiz! Iltimos davom etish uchun ro'yxatdan o'ting",
                                          reply_markup=main_brand_inline_button(callback.message.chat.id))

    elif callback.data == 'register':
        await callback.message.reply("Ro'yxatdan o'tish uchun telefon raqaminggizni jo'nating",
                                     reply_markup=reg_key.phone_num())
        await RegistrationStates.waiting_for_phone_number.set()


    elif callback.data == 'order':
        user = is_authenticated(callback.message.chat.id)
        if user:

            await callback.message.answer(text="<b>Buyurtmanggizni batafsil yozib yuboring!\n</b>"
                                               "Tez orada xodimlarimiz siz bilan bog'lanishadi")

            await OrderCustomState.message.set()

        else:

            await callback.message.answer("Siz ro'yxatdan o'tmagansiz! Iltimos davom etish uchun ro'yxatdan o'ting",
                                          reply_markup=main_brand_inline_button(callback.message.chat.id))



@dp.message_handler(Text(equals='bekor qilish'), state='*')
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await bot_start(message=message)


@dp.message_handler(Text(equals='Asosiy Menyu'), state='*')
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await bot_start(message=message)
