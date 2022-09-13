from bs4 import BeautifulSoup
import requests

url = "https://eservices.mas.gov.sg/fid/institution?sector=Banking&count=0"
html_text = requests.get(url).text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')

fi_list = soup.find('div', class_='result-list')
# print(fi_list.prettify())

with open('list.txt', 'w') as list_file:
    for a in fi_list.find_all('a', href=True, class_=''):
        list_file.write(a['href']+'\n')
list_file.close()
print("List of links compiled into list.txt")

with open('list.txt','r') as file:
    links = file.read().splitlines()

with open('output.txt', 'w') as f:
    for link in links:
        html_text = requests.get('https://eservices.mas.gov.sg' + link).text
        soup = BeautifulSoup(html_text, 'lxml')

        bank = soup.find('h1')
        f.write("Bank: " + bank.text + '\n')

        personnel_list = soup.find_all('div', class_='personnel')
        for p in personnel_list:
            title = p.h3.text
            title = title.replace(u'\xa0', u' ')
            f.write("Title: " + title + '\n')
            name = p.span
            f.write("Name: " + name.text + '\n')
        f.write("\n")

f.close()
print("Done!")
