import requests
import xmltodict

def get_nbkr_curs():
    nbkr_url = 'https://www.nbkr.kg/XML/daily.xml'

    response = requests.get(nbkr_url)

    curs_dict = xmltodict.parse(response.text)
    date = curs_dict['CurrencyRates']['@Date']
    print('Курсы валюты по НБКР', date)
    print(curs_dict)

    for currency in curs_dict['CurrencyRates']['Currency']:
        print(currency['@ISOCode'], ":",currency['Value'])

        if currency ['@ISOCode'] =="USD":
            print('Доллар',":",currency['Value'])

        if currency ['@ISOCode'] =="USD":
            print('Евро',":",currency['Value'])
        if currency ['@ISOCode'] =="USD":
            print('Тенге',":",currency['Value'])
        if currency ['@ISOCode'] =="USD":
            print('Рубль',":",currency['Value'])