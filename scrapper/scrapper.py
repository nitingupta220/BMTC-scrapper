import urllib2
import json
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()


def stops_scrapper():
    stops_page = 'http://www.mybmtc.com/kn/bus_stations'
    stops_page = urllib2.urlopen(stops_page)
    stops_soup = BeautifulSoup(stops_page, 'html.parser')
    fields = stops_soup.find('div', attrs={'class': 'field-content'})
    all_stops = fields.find('table')
    first_list = all_stops.find_next('tbody')
    second_list = first_list.find_next('tbody')
    third_list = second_list.find_next('tbody')
    stops_array = (str(translator.translate(third_list.text))).split('\n')
    stops_array[0] = str(1)
    i=0
    stops={}
    stops_list=[]
    while i< len(stops_array) :
        if len(stops_array[i]) >= 1:
            stop={}
            #stop["number"] = int(stops_array[i])
            i+=3
            stop["name"]=stops_array[i]
            i+=3
            address=stops_array[i]
            stop["address"] = address
            json_string=json.dumps(stop)
            print json_string
            stops_list.append(json_string)
        i+=1
    stops["stops_list"]=(stops_list)
    #print stops
    with open('./json_storage/stops.json', 'w') as outfile:
        json.dump(stops, outfile)


def fare_type():
    fare_type = ['acs', 'gns', 'vvs']
    for fare in fare_type:
        fare_url = 'http://www.mybmtc.com/kn/ac-service?fareid='+fare+'&qt-home_quick_tab_bottom=2'
        fare_page = urllib2.urlopen(fare_url)
        fare_soup = BeautifulSoup(fare_page, 'html.parser')
        fare_table = fare_soup.find('table')
        fare_body = fare_table.find('tbody')
        print fare_body.text
        print '#######'

#
# def route_timings():
#     for route in range(1, 3000):
#         routes_url = 'http://www.mybmtc.com/route/schedule/' + str(route) + '/C?width=600&height=550&iframe=true'
#         routes_page = urllib2.urlopen(routes_url)
#         routes_soup = BeautifulSoup(routes_page, 'html.parser')
#         box = routes_soup.find('tr', attrs={'class': 'odd'})
#         list = box.find_next('tr', attrs={'class': 'odd'})
#         header = box.find('span', attrs={'class': 'subheader-label'})
#         ul = list.find('ul', attrs={'class': 'routestime'})
#         print header.text
#         print ul.text
#         print '####'


#stops_scrapper()

fare_type()