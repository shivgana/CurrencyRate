from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
# List of currency option in google search
currencyOptionWithName=dict({"/m/019vxc":"Afghan Afghani", "/m/01n64b":"Albanian Lek", "/m/04wcz0":"Algerian Dinar", "/m/03c7mb":"Angolan Kwanza",
                "/m/024nzm":"Argentine Peso", "/m/033xr3":"Armenian Dram", "/m/08s1k3":"Aruban Florin", "/m/0kz1h":"Australian Dollar", "/m/04bq4y":"Azerbaijani Manat",
                "/m/01l6dm":"Bahamian Dollar", "/m/04wd20":"Bahraini Dinar", "/m/05hy7p":"Bajan dollar", "/m/02gsv3":"Bangladeshi Taka", "/m/05c9_x":"Belarusian Ruble",
                "/m/02bwg4":"Belize Dollar", "/m/04xb8t":"Bermudan Dollar", "/m/02gt45":"Bhutan currency", "/m/04tkg7":"Bolivian Boliviano",
                "/m/02lnq3":"Bosnia-Herzegovina Convertible Mark", "/m/02nksv":"Botswanan Pula", "/m/03385m":"Brazilian Real", "/m/021x2r":"Brunei Dollar",
                "/m/01nmfw":"Bulgarian Lev", "/m/05jc3y":"Burundian Franc", "/m/01qyjx":"CFP Franc", "/m/03_m0v":"Cambodian riel", "/m/0ptk_":"Canadian Dollar",
                "/m/06plyy":"Cape Verdean Escudo", "/m/04xbgl":"Cayman Islands Dollar", "/m/025sw2b":"Central African CFA franc", "/m/0172zs":"Chilean Peso",
                "/m/0775_k":"Chilean Unit of Account (UF)", "/m/0hn4_":"Chinese Yuan", "/g/11c54p47s9":"Chinese Yuan (offshore)", "/m/034sw6":"Colombian Peso",
                "/m/05yxq3":"Comorian franc", "/m/04h1d6":"Congolese Franc", "/m/04wccn":"Costa Rican Colón", "/m/02z8jt":"Croatian Kuna", "/m/049p2z":"Cuban Peso",
                "/m/04rpc3":"Czech Koruna", "/m/01j9nc":"Danish Krone", "/m/05yxn7":"Djiboutian Franc", "/m/04lt7_":"Dominican Peso", "/m/02r4k":"East Caribbean Dollar",
                "/m/04phzg":"Egyptian Pound", "/m/02_mbk":"Ethiopian Birr", "/m/02l6h":"Euro", "/m/04xbp1":"Fijian Dollar", "/m/04wctd":"Gambian dalasi",
                "/m/03nh77":"Georgian Lari", "/m/01s733":"Ghanaian Cedi", "/m/01crby":"Guatemalan Quetzal", "/m/05yxld":"Guinean Franc", "/m/059mfk":"Guyanaese Dollar",
                "/m/04xrp0":"Haitian Gourde", "/m/04krzv":"Honduran Lempira", "/m/02nb4kq":"Hong Kong Dollar", "/m/01hfll":"Hungarian Forint",
                "/m/012nk9":"Icelandic Króna","/m/02gsvk":"Indian Rupee", "/m/0203sy":"Indonesian Rupiah", "/m/034n11":"Iranian Rial", "/m/01kpb3":"Iraqi Dinar",
                "/m/01jcw8":"Israeli New Shekel", "/m/04xc2m":"Jamaican Dollar", "/m/088n7":"Japanese Yen", "/m/028qvh":"Jordanian Dinar", "/m/01km4c":"Kazakhstani Tenge",
                "/m/05yxpb":"Kenyan Shilling", "/m/01j2v3":"Kuwaiti Dinar", "/m/04k5c6":"Kyrgystani Som", "/m/04k4j1":"Laotian Kip", "/m/025tsrc":"Lebanese pound",
                "/m/04xm1m":"Lesotho loti", "/m/05g359":"Liberian Dollar", "/m/024xpm":"Libyan Dinar", "/m/02fbly":"Macanese Pataca", "/m/022dkb":"Macedonian Denar",
                "/m/04hx_7":"Malagasy Ariary", "/m/0fr4w":"Malawian Kwacha", "/m/01_c9q":"Malaysian Ringgit", "/m/02gsxf":"Maldivian Rufiyaa",
                "/m/023c2n":"Mauritanian Ouguiya (1973–2017)", "/m/02scxb":"Mauritian Rupee", "/m/012ts8":"Mexican Peso", "/m/02z6sq":"Moldovan Leu",
                "/m/06qsj1":"Moroccan Dirham", "/m/05yxqw":"Mozambican metical", "/m/04r7gc":"Myanmar Kyat", "/m/01y8jz":"Namibian dollar", "/m/02f4f4":"Nepalese Rupee",
                "/m/08njbf":"Netherlands Antillean Guilder", "/m/01t0lt":"New Taiwan dollar", "/m/015f1d":"New Zealand Dollar", "/m/02fvtk":"Nicaraguan Córdoba",
                "/m/018cg3":"Nigerian Naira", "/m/0h5dw":"Norwegian Krone", "/m/04_66x":"Omani Rial", "/m/02svsf":"Pakistani Rupee", "/m/0200cp":"Panamanian Balboa",
                "/m/04xblj":"Papua New Guinean Kina", "/m/04w7dd":"Paraguayan Guarani", "/m/01h5bw":"Philippine peso", "/m/0glfp":"Poland złoty", "/m/01nv4h":"Pound sterling",
                "/m/05lf7w":"Qatari Rial", "/m/02zsyq":"Romanian Leu", "/m/01hy_q":"Russian Ruble", "/m/05yxkm":"Rwandan franc", "/m/04wcnp":"Salvadoran Colón",
                "/m/02d1cm":"Saudi Riyal", "/m/02kz6b":"Serbian Dinar", "/m/01lvjz":"Seychellois Rupee", "/m/02vqvn":"Sierra Leonean Leone", "/m/02f32g":"Singapore Dollar",
                "/m/0b423v":"Sol", "/m/05jpx1":"Solomon Islands Dollar", "/m/05yxgz":"Somali Shilling", "/m/01rmbs":"South African Rand", "/m/01rn1k":"South Korean won",
                "/g/11bc5b_s84":"Sovereign Bolivar", "/m/02gsxw":"Sri Lankan Rupee", "/m/08d4zw":"Sudanese pound", "/m/02dl9v":"Surinamese Dollar", "/m/02pmxj":"Swazi Lilangeni",
                "/m/0485n":"Swedish Krona", "/m/01_h4b":"Swiss Franc", "/m/0370bp":"Tajikistani Somoni", "/m/04s1qh":"Tanzanian Shilling", "/m/0mcb5":"Thai Baht",
                "/m/040qbv":"Tongan Paʻanga", "/m/04xcgz":"Trinidad &amp; Tobago Dollar", "/m/04z4ml":"Tunisian Dinar", "/m/04dq0w":"Turkish lira",
                "/m/0425kx":"Turkmenistani manat", "/m/04b6vh":"Ugandan Shilling", "/m/035qkb":"Ukrainian hryvnia", "/m/02zl8q":"United Arab Emirates Dirham",
                "/m/09nqf":"United States Dollar", "/m/04wblx":"Uruguayan Peso", "/m/04l7bl":"Uzbekistani Som", "/m/03ksl6":"Vietnamese dong",
                "/m/025sw2q":"West African CFA franc", "/m/05yxwz":"Yemeni Rial", "/m/0fr4f":"Zambian Kwacha"})

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
currency=[] #List to store name of the Currency
rate=[] #List to store price of the Rate
# ddelement= Select(driver.find_element_by_id('id_of_element')) 
driver.get('https://www.google.com/search?q=afghan+currency+to+inr')
print( "The title is  : " + driver.title) #  R9zNe vk_bk Uekwlc
for curr in currencyOptionWithName.keys():
    if curr == '/m/02gsvk':
        continue
    ddelement= Select(driver.find_element(by=By.CLASS_NAME, value='l84FKc'))
    ddelement.select_by_value(str(curr))
    time.sleep(1)
    content = driver.page_source
    soup = BeautifulSoup(content)
    price=soup.find('span', attrs={'class':'DFlfde SwHCTb'})
    currency.append(currencyOptionWithName[curr])
    rate.append(price.text)
    
    
df = pd.DataFrame({'Currency':currency,'Rate':rate}) 
df.to_csv('othercurrency-to-indian.csv', index=False, encoding='utf-8')
