# Telegram Download Bot
Telegram bot to download files on Telegram with no size limit.

## Requirements
- Python 3.7+

## Install
1. Install this bot:
	```bash
	git clone https://github.com/RtiM0/telegram-download-bot.git
	cd telegram-download-bot
	python3 -m venv env
	source env/bin/activate
	python -m pip install -r requirements.txt
	deactivate
	```
2. Set your Bot Token (can be obtained by [@BotFather](https://t.me/BotFather)) in `line  14`
	```python
	TOKEN = "BOT-TOKEN"
	```	
	Set your output directory to store the downloaded files in `line 16`
	```python
	OUTPUT_DIR  =  "/home/potato/tgdownloadbot/"
	```
3. You need to run [Telegram Bot API Server](https://github.com/tdlib/telegram-bot-api#usage) locally on your machine to bypass the 20MB Download limit imposed with official Bot API.
Use this [guide to quickly install Telegram Bot API Server locally](https://tdlib.github.io/telegram-bot-api/build.html).
4. Run the Telegram Bot API Server
	```bash
	cd telegram-bot-api/bin/
	./telegram-bot-api --api-id <API-ID> --api-hash <API-HASH> --local
	```
5. In a new terminal run the bot.
	```bash
	cd telegram-download-bot
	source env/bin/activate
	python bot.py
	```
## Usage
Just send or forward the bot any document and it will download it on your server!