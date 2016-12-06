from flask import Flask, render_template, request
from Connect_Wifi import Connection
app = Flask(__name__)



@app.route("/")
def index():
    global wifi_connection
    wifi_connection = Connection()
    AP = wifi_connection.getAllAP()
    return render_template('index.html',APs=AP)


@app.route("/setup",methods=['POST'])
def setup():
    _ssid =""
    _pwd = ""
    if request.method == "POST":
        _ssid = request.form['SSID']
        _pwd = request.form['PWD']

    wifi_connection.SSID = _ssid
    wifi_connection.PASSWORD = _pwd
    wifi_connection.connectToAP()
    return render_template('successfulWifi.html')
if __name__=="__main__":
    app.run(debug=True)
