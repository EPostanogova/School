from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='ДА'
        ),
        KeyboardButton(
            text='НЕТ'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери кнопку ↓', selective=True)

reply_keyboard_gender = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Мужской'
        ),
        KeyboardButton(
            text='Женский'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери кнопку ↓', selective=True)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Отправить геолокацию',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text='Отправить свой контакт',
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text='Создать викторину',
            request_poll=KeyboardButtonPollType()
        )
    ]
], resize_keyboard=True, one_time_keyboard=False,
    input_field_placeholder='Отправь локацию, номер телефона или создай викторину/опрос ↓')


