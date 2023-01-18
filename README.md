# TRELLO NOTIFICATION
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fandrei-sharykau%2Ftrello-it-service.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fandrei-sharykau%2Ftrello-it-service?ref=badge_shield)

Script for checking new cards in Trello and sending a notification to Telegram. 

* trello-notification.py - executable script
* client.py - your settings
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
```
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
```

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fandrei-sharykau%2Ftrello-it-service.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fandrei-sharykau%2Ftrello-it-service?ref=badge_large)