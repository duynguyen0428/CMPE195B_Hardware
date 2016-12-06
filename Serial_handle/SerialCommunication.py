import serial
import sys
import requests
import json

def make_post(_payload=None):
    payload = {}
    URL = "https://usb-server.herokuapp.com/business"
    header = {"Content-type":"application/json"}
    if _payload is None:
        payload ={"owner":"Tester","name":"San Jose State","address":"test address"}
        r_Post = requests.post(URL,headers=header,data=json.dumps(payload))
        if r_Post.status_code == 201:
            print 'successfully post data'
    else:
        payload = _payload
        r_Post = requests.post(URL,headers=header,data=json.dumps(payload))
        if r_Post.status_code == 201:
            print 'successfully post data'
            
port = '/dev/ttyACM0'
conn = serial.Serial(port)

print("entering while")
while True:
    try:        
        inData = ""
        bytoread = 0
        if(conn.isOpen() == True):
            bytoread = conn.inWaiting()
            print(bytoread)
            if bytoread > 0:
                #print(bytoread)
                inData = conn.read(bytoread)
                #inData = conn.readline()
                
                #inData = conn.readline()
        else:
            conn.open()
            bytoread = conn.inWaiting()
            if bytoread > 0:                
                #print(bytoread)
                #inData = conn.read(bytoread)
                inData = conn.readline()
        if not inData == "":
            output = "".join(inData)
            #out = json.loads(output)
            print(len(output))
            print(output)
            make_post(output)
    except Exception as ex:
        print(ex.args)
        sys.exit()
    finally:
        conn.close() 



