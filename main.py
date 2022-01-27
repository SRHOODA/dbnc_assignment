##pip install requests(used this command to install requests)

import requests
import csv

##post url
url = 'https://tools.usps.com/tools/app/ziplookup/zipByAddress'

##used it to avoid the request from redirection
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

##defined a empty list 
address_status = []

##used this context manager for handling file(opening and closing specifically)
with open('input_sheet.csv') as file:
    reader = csv.reader(file)

    #coverted it into list to ignore the first header row
    #(we can also ignore the header using next(reader, None))
    list_reader = list(reader)

    for row in list_reader[1:]:

        ##making payload dynamic here
        payload = {
            'companyName': row[0],
            'address1': row[1],
            'address2': "",
            'city': row[2],
            'state': row[3],
            'urbanCode': "",
            'zip': row[4]
        }

        ##sending http post request here
        response_data = requests.post(url, data= payload, headers= headers)
        address_status.append(response_data.json()['resultStatus'])  ##jst storing resultStatus from the response_data i am getting from the server
    
    ##for updating the csv file with is_valid_address column and its values 
    with open('input_sheet.csv', 'w') as file:
        writer = csv.writer(file)        #this csv module has a method for creating csv, i.e. writer() 
        i = 1

        for row in list_reader[:1]:
            writer.writerow([row[0],row[1],row[2],row[3], row[4], 'Address_Status'])

        for index, row in enumerate(list_reader[1:]):
            writer.writerow([row[0],row[1],row[2],row[3], row[4], address_status[index]])  ##only adding resultStatus(we can also add the entire json)

        ##rather than using these two loops we can also use python dictionary to update the csv file
        ##and we can also use pandas package here that will make this more easier

        print('csv file successfully updated')


        ##i just used and mentioned all these things to tell you guys that i am really comfortable & well versed in python programming and its libraries
