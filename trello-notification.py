from datetime import datetime, date, time
from trello import TrelloClient
import telebot
import client

#
# settings your API connect in client.py
#
client = TrelloClient(
    api_key=client.TRELLO_API_KEY,
    token=client.TRELLO_TOKEN
)
bot = telebot.TeleBot(client.TELEGRAM_TOKEN)
chatId = client.TELEGRAM_CHATID

# last datetime update
last_date = datetime(2022, 1, 26, 16, 0, 0)

# message to Telegram
message = "**Есть работа!!!**\nпроверьте доску {}\n{}\n{}"

# all boards in Trello
all_boards = client.list_boards()

for board in all_boards:
    # all card in board
    for card in board.open_cards():
        date_card = card.created_date.replace(tzinfo=None)

        # select new card
        if last_date < date_card:
            # sent message to Telegram
            bot.send_message(chatId, message.format(card.board.name, card.name, date_card))