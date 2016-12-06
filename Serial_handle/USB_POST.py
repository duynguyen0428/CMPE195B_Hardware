import requests
import json

URL = "https://usb-server.herokuapp.com/business"
header = {"Content-type":"application/json"}
payload ={"owner":"Tester","name":"San Jose State","address":"test address"}
#r = requests.get(URL)
r_Post = requests.post(URL,headers=header,data=json.dumps(payload))
print(r_Post.status_code)

        #"Accept":"text/plain"}
#connection = httpclient.HTTPConnection(URL,80)
#connection.request("GET","/business")
#response = connection.getresponse()
#print(response.status,response.reason)
