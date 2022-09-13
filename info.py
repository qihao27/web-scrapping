from bs4 import BeautifulSoup
import requests

with open('list.txt','r') as file:
    links = file.read().splitlines()

with open('output.txt', 'w') as f:
    for link in links:
        html_text = requests.get('https://eservices.mas.gov.sg' + link).text
        soup = BeautifulSoup(html_text, 'lxml')

        bank = soup.find('h1')
        f.write("\nBank: " + bank.text + '\n')

        personnel_list = soup.find_all('div', class_='personnel')
        for p in personnel_list:
            title = p.h3.text
            title = title.replace(u'\xa0', u' ')
            f.write("Title: " + title + '\n')
            name = p.span
            f.write("Name: " + name.text + '\n')

f.close()
print("Done!")
