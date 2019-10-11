import requests
import json

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

#https://api.telegram.org/bot962645516:AAFH_RuwvFilI_bP36TOkwKU66NbdeoBZWY/sendmessage?chat_id=798317922&text=Hi
def send_message(chat_id, text='Wait a second please...'):
	url = BASE_URL + f'sendmessage?chat_id={chat_id}&text={text}'
	requests.get(url)


def main():
	chat_id = get_message().get('chat_id')
	send_message(chat_id, '1234xxx')


if __name__ == '__main__':
	main()