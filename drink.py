import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pump = 8
valve1 = 10
valve2 = 12

GPIO.setup(pump, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(valve1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(valve2, GPIO.OUT, initial=GPIO.LOW)

app = Flask(__name__)
@app.route("/")
def index():
   return render_template('index.html')

@app.route("/<action>")
def drink(action):
   if action == "on":
      print("The pump is ON")
      GPIO.output(pump, GPIO.HIGH)
      time.sleep(1)
      GPIO.output(valve2, GPIO.HIGH)
      print('Valve 2 is open')
      time.sleep(3)
      GPIO.output(valve2, GPIO.LOW)
      print('Valve 2 is closed')
      GPIO.output(valve1, GPIO.HIGH)
      print('Valve 1 is open')
      time.sleep(3)
      GPIO.output(valve1, GPIO.LOW)
      print('Valve is closed')
      GPIO.output(pump, GPIO.LOW)
      print('The pump is OFF')

   return render_template('index.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
