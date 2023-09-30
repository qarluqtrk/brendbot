from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.reg_key import back_to_main
from loader import dp, order
from states.State import OrderCustomState


@dp.message_handler(state=OrderCustomState.message)
async def order_view(message: types.Message, state: FSMContext):
    order_text = message.text
    order.add_order(order_text, message.chat.id)
    await state.finish()
    await message.answer('Buyurtmanggiz qabul qilindi!\n'
                         "Xodimlarimiz qo'ng'irog'ini kuting",
                         reply_markup=back_to_main())
