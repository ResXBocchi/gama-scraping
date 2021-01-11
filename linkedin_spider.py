import scrapy
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import requests

driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver')
driver.maximize_window()
sleep(0.5)

driver.get('https://linkedin.com/')
sleep(3)

driver.find_element_by_xpath('//a[text()="Sign in"]').click()
sleep(3)

user_field = driver.find_element_by_xpath('//input[@name="session_key"]')
user_field.send_keys(input('insert your id'))

password_field = driver.find_element_by_xpath('//input[@name="session_password"]')
password_field.send_keys(input('insert your password'))

driver.find_element_by_xpath("//button[text()='Sign in']").click()
sleep(3)



profiles = ['https://www.linkedin.com/in/maris-araujo/',
 'https://www.linkedin.com/in/guijunqueira/',
 'https://www.linkedin.com/in/bruno-moretti-a4671713/',
 'https://www.linkedin.com/in/rlassance/',
 'https://www.linkedin.com/in/luisquintanilha/',
 'https://www.linkedin.com/in/vitorferreira91/',
 'https://www.linkedin.com/in/joaopaulospfaria/',
 'https://www.linkedin.com/in/ceciliabere/',
 'https://www.linkedin.com/in/farneyvictor/',
 'https://www.linkedin.com/in/andreluisferreiraramalho/',
 'https://www.linkedin.com/in/giovanna-passos/',
 'https://www.linkedin.com/in/belalian/',
 'https://www.linkedin.com/in/monicalima1/',
 'https://www.linkedin.com/in/lakabolina/',
 'https://www.linkedin.com/in/leandrinhovieira/',
 'https://www.linkedin.com/in/rafaelkiso/',
 'https://www.linkedin.com/in/thiagolevenhagen/',
 'https://www.linkedin.com/in/andreaamaral/',
 'https://www.linkedin.com/in/salmogardino/',
 'https://www.linkedin.com/in/alexandrepaez/',
 'https://www.linkedin.com/in/quiterio-ferreira/',
 'https://www.linkedin.com/in/viniciusvaleiro/',
 'https://www.linkedin.com/in/carolinayamauti/',
 'https://www.linkedin.com/in/mateusquelhas/',
 'https://www.linkedin.com/in/professor-isidro-phd-8a85a979/',
 'https://www.linkedin.com/in/thaysgiotto/',
 'https://www.linkedin.com/in/jcbombardelli/',
 'https://www.linkedin.com/in/guilhermevpr/',
 'https://www.linkedin.com/in/vitorfgsantos/',
 'https://www.linkedin.com/in/danilo-aparecido-dos-santos-03101034/',
 'https://www.linkedin.com/in/danielobara/',
 'https://www.linkedin.com/in/giullia-gomes-12749712a/',
 'https://www.linkedin.com/in/marcellaschneider/',
 'https://www.linkedin.com/in/thaisfalabella/',
 'https://www.linkedin.com/in/suzanaribeiro/',
 'https://www.linkedin.com/in/luisfelipefernandes/',
 'https://www.linkedin.com/in/uxmatheuspinheiro/',
 'https://www.linkedin.com/in/carladebona/',
 'https://www.linkedin.com/in/trindadelarissa/',
 'https://www.linkedin.com/in/rudneisilvestre/',
 'https://www.linkedin.com/in/nicoliferraz/',
 'https://www.linkedin.com/in/giovannidelnegro/',
 'https://www.linkedin.com/in/amanda-nideck-b8706ab6/',
 'https://www.linkedin.com/in/ranitalks/',
 'https://www.linkedin.com/in/rodrigo-ricco/',
 'https://www.linkedin.com/in/roberta-alencars/',
 'https://www.linkedin.com/in/yuri-felipe/',
 'https://www.linkedin.com/in/rlcorrea/',
 'https://www.linkedin.com/in/kewin-moya/',
 'https://www.linkedin.com/in/lizi-rodrigues-148a2951/',
 'https://www.linkedin.com/in/eduvlld/',
 'https://www.linkedin.com/in/camelyrabelo/',
 'https://www.linkedin.com/in/thiagosoaresdeoliveira/']

for profile in profiles:
    driver.get(profile)
    sleep(2)
    img = driver.find_element_by_xpath('//*[@class="pv-top-card__photo presence-entity__image EntityPhoto-circle-9 lazy-image ember-view"]')
    src = img.get_attribute('src');
    url = src
    name = driver.find_element_by_xpath('//*[@class="inline t-24 t-black t-normal break-words"]').text.replace(' ','').replace('.','')
    filename = '{}.jpeg'.format(name)
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)

class LinkedinSpiderSpider(scrapy.Spider):
    name = 'linkedin_spider'
    allowed_domains = ['linkedin.com']
    start_urls = ['http://linkedin.com/']

    def parse(self, response):
        pass
