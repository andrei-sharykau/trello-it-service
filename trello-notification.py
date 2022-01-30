from datetime import datetime, date, time
from client import client


today = datetime(2022, 1, 26, 16, 0, 0)

def main():
    all_boards = client.list_boards()

    for board in all_boards:
        cards = board.open_cards()
        for card in cards:
            date_card = card.created_date.replace(tzinfo=None)
            if today < date_card:
                print("%s %s %s" %(card.board.name, card.name, date_card))


if __name__ == "__main__":
    main()