import requests
import sys

def main():
    if len(sys.argv) > 1:
        abv_limit = sys.argv[1]
    else:
        print('ABV Limit not defined. Taking the default ABV limit as 6')
        abv_limit = 6
    parse_data("https://api.punkapi.com/v2/beers",abv_limit)
    
def connect_api(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        print('API Call Succefful')
        json_data = response.json()
        print ('Printing the Response from the API')
        #print(json_data)
        return json_data
    else:
        print ("Error in getting data from API, Status Code : {}".format(response.status_code,))
        exit()

def parse_data(url,abv_limit=6):
    json_data_list = connect_api(url)

    print('Stage 1')
    for i in json_data_list:
        print(i['name'],i['abv'])
    print ('Bonus Stage : Printing only the beers with ABV greater than {}'.format(abv_limit,))
    for i in json_data_list:
        if i['abv'] > abv_limit:
            print(i['name'],i['abv'])
    
    print ('List of Beers with ABV values in Descending Order')
    #sorted_data_by_abv_descending = json_data_list.sort(key='abv', reverse=True)

    sorted_data_by_abv_descending = sorted(json_data_list, key=lambda k: k['abv'], reverse=True)
    for i in sorted_data_by_abv_descending:
        print(i['name'],i['abv'])


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
