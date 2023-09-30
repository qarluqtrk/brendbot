from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.brand_inline_button import main_menu_back
from loader import dp, comment
from states.State import CommentState


@dp.message_handler(state=CommentState.comment)
async def comment_view(message: types.Message, state: FSMContext):
    # comment.add_comment(comment=message.text,
    #                user_id=message.from_user.id
    #                )
    comment.add_comment(comment=message.text,
                        user_id=message.chat.id)
    await message.answer(text="Fikrlaringiz uchun rahmat ! ",
                         reply_markup=main_menu_back())
    await state.finish()
