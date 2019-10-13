import requests
import json
from parsing_olx.pars_olx import *


token = '962645516:AAFH_RuwvFilI_bP36TOkwKU66NbdeoBZWY'
BASE_URL = 'https://api.telegram.org/bot' + token + '/'


def get_html():
	url = BASE_URL + 'getUpdates'
	request = requests.get(url)
	return request.json()


def get_message():
	data = get_html()

	chat_id = data.get('result')[-1].get('message').get('chat').get('id')
	text = data.get('result')[-1].get('message').get('text')

	message = {
		'chat_id': chat_id,
		'text': text
	}

	return message


def send_message(chat_id, text='Wait a second please...'):
	url = BASE_URL + f'sendmessage?chat_id={chat_id}&text={text}'
	requests.get(url)


def main():
	data = get_message()
	chat_id = data.get('chat_id')

	if 'квартири' in data.get('text'):
		advertisements_apartments = parse_olx(base_url, headers)
		for advertisement in advertisements_apartments:
			send_message(chat_id, advertisement)


if __name__ == '__main__':
	main()