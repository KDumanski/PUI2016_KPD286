
# coding: utf-8

# In[3]:

import sys
#pass arguments into command line sys.argv
import requests
#scrape data
import json
#parse data
import csv
#read data into csv format

#pass arguments into command line
if __name__=='__main__':
#capture data
    url = ('http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2].upper()))
    response = requests.get(url)
#load to json
    json_data = json.loads(response.text)
    Vechicles = json_data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    
    #create csv 
    with open(sys.argv[3], 'wb') as csvfile:
        opener = csv.writer(csvfile)
        opener.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])
       
    #parse data
        for eachbus  in Vechicles
            latitude = EachBus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
            longitude = EachBus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
            
            if:
                StopName = EachBus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
                StopStatus = EachBus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
            
            else 
                EachBus["MonitoredVehicleJourney"]["OnwardCalls"]
                StopName = "N/A"
                StopStatus = "N/A"

                
            row = [latitude, longitude, StopName, StopStatus]
            opener.writerow(row)
            
    #send out
    print '%s, %s, %s, %s' %(latitude, longitude, StopName, StopStatus)
            
        
    
   


# In[ ]:



