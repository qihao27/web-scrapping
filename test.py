from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://eservices.mas.gov.sg/fid/institution/detail/3502-ABN-AMRO-BANK-N-V').text
soup = BeautifulSoup(html_text, 'lxml')

bank = soup.find('h1')
print(bank.text)

# personnel_list = soup.find_all('div', class_='personnel')
# for p in personnel_list:
#     title = p.h3.text
#     print(title)
#     name = p.span.text
#     print(name)


# with open('output.txt', 'w') as f:
#     for a in fi_list.find_all('a', href=True, class_=''):
#         f.write(a['href']+'\n')
#         # print(a['href'])
