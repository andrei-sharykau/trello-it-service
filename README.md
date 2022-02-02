# TRELLO NOTIFICATION
Script for checking new cards in Trello and sending a notification to Telegram. 

* trello-notification.py - executable script 
* requirements.txt - modules used python
* Dockerfile - docker image build file 

## SETTINGS

to run the script, you need to create a client.by file in the same directory with the contents

**Trello API**
[https://trello.com/app-key](https://trello.com/app-key)

**Create Telegram bot**
Token for your bot
[https://core.telegram.org/bots#6-botfather](https://core.telegram.org/bots#6-botfather)

@my_id_bot - Use this bot to get your Telegram ID or add it to group to see its ID


**exmple:**
'''
# API Trello
TRELLO_API_KEY='your-trello-api-key'
TRELLO_TOKEN='your-trello-token'

# API Telegram
TELEGRAM_TOKEN='your-telegram-token'
TELEGRAM_CHATID='your-telegram-chat-id'

# timeout minutes checking new card in Trello 
CHECK_TIMEOUT=15

# message to Telegram
MESSAGE = "**Got a job!!!**\ncheck the board **{}**\n{}\n{}"
'''