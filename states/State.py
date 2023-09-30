from aiogram.dispatcher.filters.state import StatesGroup, State


class AuthState(StatesGroup):
    name = State()
    phone_number = State()
    location = State()

class RegistrationStates(StatesGroup):
    waiting_for_phone_number = State()
    waiting_for_name = State()
    waiting_for_location = State()

class OrderCustomState(StatesGroup):
    message = State()


class CommentState(StatesGroup):
    comment = State()

