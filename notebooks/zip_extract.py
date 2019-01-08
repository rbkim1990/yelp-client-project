import requests
from bs4 import BeautifulSoup
import re

def zip_data(zip):
    dicto = {}
    url = 'http://www.city-data.com/zips/'+str(zip)+'.html'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    pop = soup.find('div', {'class':'row'}).text.split('\n')[1].split(':')[3].strip().replace(',','')
    pop = float(pop)
    cost_of_living = soup.find('div', {'class':'row'}).text.split('\n')[6].split(':')[1].split('(')[0].strip()
    cost_of_living = float(cost_of_living)
    area = soup.find('div', {'class':'row'}).text.split('\n')[7].split(':')[1].strip().split(" ")[0]
    area = float(area)
    
    save = ""
    for s in soup.find_all('div', {'class':'hgraph'}):
        if s.text.find('median household income') > 0:
            save = s
    
    a = save.text.split(":")[2]
    med_income = re.findall('[^A-Z]*',a)[0].replace(',','').replace('$','')
    med_income = float(med_income)
    
    dicto['zip'] = zip
    dicto['population'] = pop
    dicto['cost_of_living'] = cost_of_living
    dicto['area'] = area
    dicto['median_income'] = med_income
    
    return dicto
