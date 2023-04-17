from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import asyncio
import buttons
import config as cfg
from ClientClass import ClientInfo
import logging
import time
import functions as func

#func
async def Filling_Form(user_id, stage):
    if stage == 5 or stage == 8 or stage == 9 or stage == 10 or stage == 11 or stage == 15:
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[buttons.returnButton],[buttons.mainmenuButton]])
        msg1 = func.GetMessageByStage(stage)
        msg2 = func.GetMessageByStage(17)
        match stage:
            case 5:
                kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=
                                            [[buttons.numreqButton1],[buttons.numreqButton2],
                                                [buttons.numreqButton3],[buttons.numreqButton4],
                                                [buttons.numreqButton5]])
            case 8:
                kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=
                                               [[buttons.taplinktypeButton1],[buttons.taplinktypeButton2],
                                                [buttons.taplinktypeButton3]])
            case 9:
                kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=
                                               [[buttons.deadlineButton1],[buttons.deadlineButton2],
                                                [buttons.deadlineButton3],[buttons.deadlineButton4]])
            case 10:
                kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=
                                               [[buttons.budgetButton1],[buttons.budgetButton2],
                                                [buttons.budgetButton3],[buttons.budgetButton4],
                                                [buttons.budgetButton5]])
            case 11:
                kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=
                                               [[buttons.targetButton1],[buttons.targetButton2],
                                                [buttons.targetButton3],[buttons.targetButton4]])
            case 15:
                kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=
                                               [[buttons.paymentButton1],[buttons.paymentButton2],
                                                [buttons.paymentButton3],[buttons.paymentButton4],
                                                [buttons.paymentButton5],[buttons.paymentButton6]])
        await bot.send_message(user_id,f"{msg1}",reply_markup=kb)
        await bot.send_message(user_id,f"{msg2}",reply_markup=keyboard)
        return
    if stage == 1:
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[buttons.mainmenuButton]])
    else:
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[buttons.returnButton],[buttons.mainmenuButton]])
    msg = func.GetMessageByStage(stage)
    await bot.send_message(user_id, f"{msg}", reply_markup=keyboard)


#log
logging.basicConfig(level=logging.INFO)

#init
bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)
clients = dict()

#start
@dp.message_handler(commands=['start'])
async def send_welcome_message(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[[buttons.fillFormButton],[buttons.googleformButton],[buttons.answerButton],[buttons.callButton]])
    await bot.send_message(message.chat.id, "Вы находитесь в главном меню. Выберите необходимое действие", reply_markup=keyboard)

#callbacks
@dp.callback_query_handler(Text(startswith="call"))
async def callbacks_buy(call: types.CallbackQuery):
    action = call.data.split("_")[1]
    match action:
        case 'menu':
            clients[call.from_user.id] = None
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[buttons.fillFormButton],[buttons.googleformButton],[buttons.answerButton],[buttons.callButton]])
            await bot.send_message(call.from_user.id, "Вы находитесь в главном меню. Выберите необходимое действие", reply_markup=keyboard)
        case 'fill':
            clients[call.from_user.id] = ClientInfo()
            await Filling_Form(call.from_user.id, 1)
        case 'back':
            objClient = clients.get(call.from_user.id)
            objClient.dec_stage()
            await Filling_Form(call.from_user.id, objClient.get_stage())
        case 'view':
            msg = func.MakeForm(clients.get(call.from_user.id))
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[buttons.acceptButton],[buttons.mainmenuButton]])
            await bot.send_message(call.from_user.id,msg,reply_markup=keyboard)
        case 'gform':
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[buttons.urlgformButton],[buttons.mainmenuButton]])
            await bot.send_message(call.from_user.id,'Перейдите с помощью кнопки на гугл-форму', reply_markup=keyboard)
        case 'accept':
            obj = clients.get(call.from_user.id)
            if obj.isAllowedAccept == True:
                msg = func.MakeForm(obj)
                await bot.send_message(cfg.SUBADMIN_ID, f"Получена новая заявка от @{call.from_user.username}")
                await bot.send_message(cfg.SUBADMIN_ID, msg)            
                await bot.send_message(cfg.ADMIN_ID, f"Получена новая заявка от @{call.from_user.username}")
                await bot.send_message(cfg.ADMIN_ID, msg)
                keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[buttons.mainmenuButton]])
                await bot.send_message(call.from_user.id,'Анкета успешно отправлена',reply_markup=keyboard)
                obj.disable_accept()
        case 'answer':
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[buttons.mainmenuButton]])
            with open(cfg.PHOTO_PATH, 'rb') as photo:
                await bot.send_photo(call.from_user.id, photo, f"С удовольствием отвечу на ваш вопрос и помогу разобраться\n@ansteykrau",reply_markup=keyboard)
        case 'callback':
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[buttons.mainmenuButton]])
            with open(cfg.PHOTO_PATH, 'rb') as photo:
                await bot.send_photo(chat_id = call.from_user.id, photo = photo, caption = f"Отлично! Напишите мне @ansteykrau\nВыберем удобное время для того, чтобы созвониться",reply_markup=keyboard)

#text
@dp.message_handler(content_types=['text'])
async def check_text(message: types.Message):
    objClient = clients.get(message.from_user.id)            
    stage = objClient.get_stage()
    match stage:
        case 1:
            objClient.set_name(message.text)
        case 2:
            objClient.set_link(message.text)
        case 3:
            objClient.set_promotion(message.text)
        case 4:
            objClient.set_product(message.text)
        case 5:
            objClient.set_numreq(message.text)
        case 6:
            objClient.set_paybring(message.text)
        case 7:
            objClient.set_disadv(message.text)
        case 8:
            objClient.set_taplinktype(message.text)
        case 9:
            objClient.set_deadline(message.text)
        case 10:
            objClient.set_budget(message.text)
        case 11:
            objClient.set_target(message.text)
        case 12:
            objClient.set_emotions(message.text)
        case 13:
            objClient.set_blocks(message.text)
        case 14:
            objClient.set_functional(message.text)
        case 15:
            objClient.set_payment(message.text)
    objClient.inc_stage()
    if objClient.get_stage() < 16:
        await Filling_Form(message.from_user.id,objClient.get_stage()) 
    elif objClient.get_stage() == 16:
        msg = func.GetMessageByStage(16)
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[buttons.viewButton],[buttons.acceptButton],[buttons.mainmenuButton]])
        objClient.allow_accept()
        await bot.send_message(message.from_user.id, msg, reply_markup=keyboard)

#run
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = False)
