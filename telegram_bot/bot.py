import requests
import json

token = '962645516:AAFH_RuwvFilI_bP36TOkwKU66NbdeoBZWY'

#https://api.telegram.org/bot962645516:AAFH_RuwvFilI_bP36TOkwKU66NbdeoBZWY/getUpdates
def get_html():
	base_url = 'https://api.telegram.org/bot' + token + '/getUpdates'
	request = requests.get(base_url)
	return request.json()



def main():
	get_html()


if __name__ == '__main__':
	main()