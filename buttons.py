from aiogram import types

profileButton = types.KeyboardButton(text='👤 Профиль')
subButton = types.KeyboardButton(text='💰 Оплатить подписку')

mainmenuButton = types.InlineKeyboardButton(text='🏠Вернуться в главное меню', callback_data='call_menu')
returnButton = types.InlineKeyboardButton(text='↩️Вернуться к предыдущему шагу', callback_data='call_back')
fillFormButton = types.InlineKeyboardButton(text='📝Заполнить анкету', callback_data='call_fill')
googleformButton = types.InlineKeyboardButton(text='🗒️Заполнить гугл-форму', callback_data='call_gform')
urlgformButton = types.InlineKeyboardButton(text='Ссылка на гугл-форму', url='https://docs.google.com/forms/d/e/1FAIpQLScmgmFyXUGzf75xIbsSP3xNudbvUaC2Pd6SN1YIy4NXPEhl8A/viewform')
changeButton = types.InlineKeyboardButton(text='✏️Изменить данные', callback_data='call_change')
acceptButton = types.InlineKeyboardButton(text='✅Готово', callback_data='call_accept')
viewButton = types.InlineKeyboardButton(text='📋Посмотреть на анкету', callback_data='call_view')
answerButton = types.InlineKeyboardButton(text='❓Хочу задать вопрос', callback_data='call_answer')
callButton = types.InlineKeyboardButton(text='📞Хочу созвониться', callback_data='call_callback')

numreqButton1 = types.KeyboardButton(text='До 10')
numreqButton2 = types.KeyboardButton(text='10-30')
numreqButton3 = types.KeyboardButton(text='30-50')
numreqButton4 = types.KeyboardButton(text='50-100')
numreqButton5 = types.KeyboardButton(text='100+')

targetButton1 = types.KeyboardButton(text='Увеличение продаж, услуг, товаров')
targetButton2 = types.KeyboardButton(text='Разместить информацию о себе')
targetButton3 = types.KeyboardButton(text='Вся информация в одном месте')
targetButton4 = types.KeyboardButton(text='Запуск курса/марафона')

taplinktypeButton1 = types.KeyboardButton(text='Одностраничный таплинк')
taplinktypeButton2 = types.KeyboardButton(text='Многостраничный таплинк')
taplinktypeButton3 = types.KeyboardButton(text='Интернет-магазин')

deadlineButton1 = types.KeyboardButton(text='Сроки горят')
deadlineButton2 = types.KeyboardButton(text='5-7 дней')
deadlineButton3 = types.KeyboardButton(text='Месяц')
deadlineButton4 = types.KeyboardButton(text='Не принципиально')

budgetButton1 = types.KeyboardButton(text='10 000 - 20 000₽')
budgetButton2 = types.KeyboardButton(text='До 30 000₽')
budgetButton3 = types.KeyboardButton(text='До 40 000₽')
budgetButton4 = types.KeyboardButton(text='До 50 000₽')
budgetButton5 = types.KeyboardButton(text='Бюджет неограничен')

paymentButton1 = types.KeyboardButton(text='Юмани')
paymentButton2 = types.KeyboardButton(text='Сбербанк')
paymentButton3 = types.KeyboardButton(text='Тинькофф')
paymentButton4 = types.KeyboardButton(text='Капуста')
paymentButton5 = types.KeyboardButton(text='Продамус')
paymentButton6 = types.KeyboardButton(text='Оплата на сайте не требуется')
