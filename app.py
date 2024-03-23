import json
import time
from flask import Flask, render_template, make_response
from urllib.request import urlopen

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    url = "https://api.thingspeak.com/channels/1720899/feeds/last.json?api_key=PAKMQ87MES1124SM&results=2"
    response = urlopen(url)
    variable = json.loads(response.read())
     
      

    power =  float(variable['field1'])
    motor_speed= float( variable['field2'])
    throttle = float(variable['field3'])
    distance_travelled = float(variable['field4'])
    x = time.time() + 19800

    

    

    data = [x * 1000,power,motor_speed,throttle,distance_travelled]

    print(data)

   
    time.sleep(1)
  
    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
