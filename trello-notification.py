from datetime import datetime, date, time
from client import client

#
# settings your API connect in client.py
#
# from trello import TrelloClient
# client = TrelloClient(
#     api_key='your-API-key',
#     token='your-token'
# )

# last datetime update
last_date = datetime(2022, 1, 26, 16, 0, 0)


# all boards in Trello
all_boards = client.list_boards()

for board in all_boards:
    # all card in board
    for card in board.open_cards():
        date_card = card.created_date.replace(tzinfo=None)

        # select new card
        if last_date < date_card:
            print("%s %s %s" %(card.board.name, card.name, date_card))