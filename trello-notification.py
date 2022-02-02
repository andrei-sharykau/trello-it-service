from datetime import datetime, date, time, timedelta
from trello import TrelloClient
import time
import schedule
import telebot
import client


client = TrelloClient(
    api_key=client.TRELLO_API_KEY,
    token=client.TRELLO_TOKEN
)
bot = telebot.TeleBot(client.TELEGRAM_TOKEN)
chatId = client.TELEGRAM_CHATID


# variable for last_date
last_date = datetime.now() - timedelta(days=1)

def check_new_cards():

    global last_date

    check_date = datetime.now()

    # all boards in Trello
    all_boards = client.list_boards()

    for board in all_boards:
        # all card in board
        for card in board.open_cards():
            date_card = card.created_date.replace(tzinfo=None)

            # select new card
            if last_date < date_card:
                # sent message to Telegram
                bot.send_message(chatId, client.MESSAGE.format(card.board.name, card.name, date_card))

    last_date = check_date

schedule.every(client.CHECK_TIMEOUT).minutes.do(check_new_cards)

while True:
    schedule.run_pending()
    time.sleep(1)