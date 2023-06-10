from bs4 import BeautifulSoup as bs
import requests
import re

links = ["https://humboldt-schule.de/kollegium/", "https://humboldt-schule.de/kollegium/page/2/", "https://humboldt-schule.de/kollegium/page/3/", "https://humboldt-schule.de/kollegium/page/4", "https://humboldt-schule.de/kollegium/page/5", "https://humboldt-schule.de/kollegium/page/6", "https://humboldt-schule.de/kollegium/page/7", ]

for i in links:
    page = requests.get(i)
    # <Response [200]>
    soup = bs(page.content)
    email_raw = soup.find_all(class_='mail')
    string_email_raw = str(email_raw)

    match = re.findall('\S+@\S+' , string_email_raw)   
    
    
    with open('emails.txt', mode='a', encoding='utf-8') as myfile:
            myfile.write('\n'.join(match))
            myfile.write('\n')
