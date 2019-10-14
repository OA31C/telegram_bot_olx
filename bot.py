import requests
import telegram
import json
from parsing_olx.pars_olx import *


token = '962645516:AAFH_RuwvFilI_bP36TOkwKU66NbdeoBZWY'
BASE_URL = 'https://api.telegram.org/bot' + token + '/'

last_update_id = 0

def get_html():
	url = BASE_URL + 'getUpdates'
	request = requests.get(url)
	return request.json()


def get_message():
	data = get_html()

	last_object = data.get('result')[-1]
	current_update_id = last_object['update_id']

	global last_update_id
	if last_update_id != current_update_id:
		last_update_id = current_update_id

		chat_id = last_object.get('message').get('chat').get('id')
		text = last_object.get('message').get('text')

		message = {
			'chat_id': chat_id,
			'text': text
		}

		return message
	return None


def send_message(chat_id, text='Wait a second please...'):
	url = BASE_URL + f'sendmessage?chat_id={chat_id}&text={text}'
	requests.get(url)


def send_document(chat_id):
	url = BASE_URL + 'sendDocument';
	files = {'document': open('parsed_advertisements_apartments.csv', 'rb')}
	data = {'chat_id' : chat_id}
	r = requests.post(url, files=files, data=data)


def main():
	while True:
		answer = get_message()
		if answer != None:
			chat_id = answer.get('chat_id')
			if 'квартири' in answer.get('text'):
				advertisements_apartments = parse_olx(base_url, headers)
				files_writer(advertisements_apartments)
				send_message(chat_id, 'Дані по аренді квартир з olx.ua')
				send_document(chat_id)
			else:
				continue


if __name__ == '__main__':
	main()