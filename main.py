import requests

from token import token
from config import start_msg

class zerBot:

    def __init__(self, token):
        self.token = token
        self.api_url = 'https://api.telegram.org/bot{}/'.format(token)
        self.api_coin_url = 'https://api.cryptonator.com/api/ticker'

    # Function get all updates in 24 hours
    def get_all_updates(self, offset = None, timeout = 30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    # Function get last update
    def get_last_update(self):
        results = self.get_all_updates()

        if len(results) > 0:
            last_update = results[-1]
        else:
            last_update = results[len(results)]

        return last_update

    # Function sending message
    def send_message(self, chat_id, message):
        method = 'sendMessage'
        params = {'chat_id': chat_id, 'text': message}
        resp = requests.post(self.api_url + method, params)
        return resp
    
    def get_coin(self, ticker):
        tick = requests.get(self.api_coin_url + ticker + '-usd')
        tick_json = tick.json()['ticker']
        return tick_json


bot = zerBot(token)
start = '/start'
btc = '/btc'
eth = '/eth'

def main():
    new_offset = None
    
    while True:
        bot.get_all_updates(new_offset)

        last_update = bot.get_last_update()

        last_update_id = last_update['update_id']
        print(last_update_id)
        print(new_offset)
        last_chat_id = last_update['message']['chat']['id']
        last_chat_text = last_update['message']['text']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text == start:
            bot.send_message(last_chat_id, 'Приветствую тебя, ' + last_chat_name + start_msg)

        elif last_chat_text == btc:
            coin = bot.get_coin(btc)['price']
            bot.send_message(last_chat_id, last_chat_name + ', курс Биткойна равен $' + coin)

        elif last_chat_text == eth:
            coin = bot.get_coin(eth)['price']
            bot.send_message(last_chat_id, last_chat_name + ', курс Эфириума равен $' + coin)

        else:
            bot.send_message(last_chat_id, last_chat_name + ', к сожалению, таких команд я не понимаю!')

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()



