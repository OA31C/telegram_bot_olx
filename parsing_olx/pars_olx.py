import requests
import csv
from bs4 import BeautifulSoup

headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
base_url = 'https://www.olx.ua/nedvizhimost/kvartiry-komnaty/arenda-kvartir-komnat/q-Луцьк/?page=1' 


def parse_olx(url, headers):
	advertisements_apartments = []
	urls = []
	session = requests.Session()
	request = session.get(url, headers=headers)
	if request.status_code == 200:
		soup = BeautifulSoup(request.content, 'lxml')

		pagination = soup.find_all('a', attrs={'class': 'block br3 brc8 large tdnone lheight24'})
		count_pages = int(pagination[-1].text)

		try:
			for i in range(count_pages + 1):
				if i == 0:
					continue

				url = f'https://www.olx.ua/nedvizhimost/kvartiry-komnaty/arenda-kvartir-komnat/q-Луцьк/?page={i}'
				urls.append(url)
		except:
			print('Error parsing urls')

		for url in urls:
			request = session.get(url, headers=headers)
			soup = BeautifulSoup(request.content, 'lxml')
			advertisements = soup.find_all('tr', attrs={'class': 'wrap'})
			for advertisement in advertisements:
				try:
					title = advertisement.find('h3', attrs={'class': 
						    'lheight22'}).find('a', attrs={'class':
						    'marginright5'}).find('strong').text

					href = advertisement.find('h3', attrs={'class': 
						    'lheight22'}).find('a', attrs={'class':
						    'marginright5'}).get('href')
					

					price = advertisement.find('p', attrs={'class': 'price'}).text.strip()

					block_city_and_date = advertisement.find('td', attrs={
										  'class': 'bottom-cell'}).find_all('small', 
										  attrs={'class': 'breadcrumb x-normal'})
					city = block_city_and_date[0].text.strip()
					date = block_city_and_date[1].text.strip()
					
					advertisements_apartments.append({
							'title': title,
							'href': href,
							'price': price,
							'city': city,
							'date': date
						})
				except:
					pass
	else:
		print('Error ' + str(request.status_code))

	return advertisements_apartments

def files_writer(advertisements_apartments):
	with open('parsed_advertisements_apartments.csv', 'w') as file:
		a_pen = csv.writer(file)
		a_pen.writerow(('Заголовок', 'Силка', 'Ціна', 'Місто', 'Дата'))
		for a_apartment in advertisements_apartments:
			a_pen.writerow((a_apartment.get('title'), a_apartment.get('href'), 
							a_apartment.get('price'), a_apartment.get('city'),
							a_apartment.get('date')))

# advertisements_apartments = parse_olx(base_url, headers)
# files_writer(advertisements_apartments)