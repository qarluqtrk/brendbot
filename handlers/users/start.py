from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.brand_inline_button import main_brand_inline_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.chat.id == 5689352779:
        pass
    else:
        photo_path = "image/brand_mebel.jpg"
        with open(photo_path, 'rb') as photo_file:
            await message.answer_photo(photo=photo_file,
                                       caption="Sifatli mebel qanaqa bo'lishini o'zinggiz uchun qayta kashf eting. Sifat, chidamlilik va qulaylik uchun Brend Mebelni tanlang. Uyinggizni faqat sifatli, vaqt sinoviga bardosh bera oladigan, pul sarflashga arzigulik mebellar bilan jihozlang",
                                       reply_markup=main_brand_inline_button(user=message.chat.id))
