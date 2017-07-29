import json
import urllib.request
import csv
#Writing the Header records
list_column_name  = ['LATITUDE', 'LONGITUDE', 'ZIP_CODE_LAT_LONG','ADDRESS']
with open ('E:\Rise Spring 2017\Advance Business Intelligence\Project-Biased Algo\zip_code_by_lat_log.csv','w',newline='') as csvfile:
    a = csv.writer(csvfile, delimiter=',')
    a.writerow(list_column_name)
    csvfile.close()
#Reading latitude and longitude to find ZIP CODES by google Map API    
with open ('E:\Rise Spring 2017\Advance Business Intelligence\Project-Biased Algo\lat_long_data.txt',"r+",encoding='utf-8') as textfile:
    for row in textfile:
        row=row.strip()
        list_data = []
        row_split = row.split(',')
        list_data.append(row_split[0])
        list_data.append(row_split[1])
        weblink = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+row+"&APIkey=XXXX"
        #print(weblink)
        webURL = urllib.request.urlopen(weblink)
        data = webURL.read()
        jsonToPython = json.loads(data.decode('utf-8'))
        #zip_code = (jsonToPython['results'][0]['address_components'][7]['short_name'])
        formatted_address = (jsonToPython['results'][0]['formatted_address'])

        address_split = formatted_address.split(',')

        address_split[2]=address_split[2].strip()
        state_zip = address_split[2].split(' ')
        try:
            zip_code = state_zip[1]
        except:
            zip_code = " "
      
        # Opening the 
        with open ('E:\Rise Spring 2017\Advance Business Intelligence\Project-Biased Algo\zip_code_by_lat_log.csv','a',newline='') as csvfile:
            csvfile = csv.writer(csvfile, delimiter=',')
            list_data.append(zip_code)
            list_data.append(formatted_address)
            csvfile.writerow(list_data)
        print(list_data)
        
        
        
        
