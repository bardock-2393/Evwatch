import time as t
import calendar
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import serial.tools.list_ports
import boto3
import random

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, MESSAGE, TOPIC, and RANGE
ENDPOINT = "a3q6iolg4f1005-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "Thing-Test"
PATH_TO_CERTIFICATE = "certificates/6921ad84520f982ca2672a046551ba399cdc3a6b5e553521ec54baa197a354d6-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "certificates/6921ad84520f982ca2672a046551ba399cdc3a6b5e553521ec54baa197a354d6-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "certificates/root.pem"
MESSAGE = "Hello World"
TOPIC = "test/testing"
RANGE = 20

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)

myAWSIoTMQTTClient.connect()
# ports = serial.tools.list_ports.comports()
# serialInst = serial.Serial()
# portList = []
# for onePort in ports:
#     portList.append(str(onePort))
#     print(str(onePort))
# val = input("select port:COM")

# for x in range(0,len(portList)):
#     if portList[x].startswith("COM"+str(val)):
#         portVar = "COM" + str(val)
#         print(portList[x])

# serialInst.baudrate = 9600
# serialInst.port = portVar
# serialInst.open()
# def customCallback(client,userdata,message):
    
#     print(message.payload)
print('Begin Publish')
for i in range (RANGE):
    while True:
    #  if serialInst.in_waiting:
        # packet = serialInst.readline()
        # converted_str = str(packet)
        # size = len(converted_str )   # text length
        # replacement = "X"  # replace with this
        # converted_str  = converted_str .replace(converted_str [size - 5:], replacement)
        # char1 = '$'
        # char2 = 'X'
        # converted_str = converted_str[converted_str.find(char1)+1 : converted_str.find(char2)]
        # converted_str = converted_str.split(',')
        current_GMT = t.gmtime()
        ts = calendar.timegm(current_GMT)
        id = 0* 100
        Fram_index = int(id)
        Dc_current =  random.random() * 100
        Dc_current = int(Dc_current)
        Dc_voltage =random.random() * 100
        Dc_voltage = int(Dc_voltage)
        Dc_power = random.random() * 100
        Dc_power = int(Dc_power)
        Ac_current =random.random() * 100
        Ac_current = int(Ac_current)
        Ac_voltage =random.random() * 100
        Ac_voltage = int(Ac_voltage)
        motor_speed = random.random() * 100
        motor_speed = int(motor_speed)
        controller_temperture = random.random() * 100
        controller_temperture = int(controller_temperture)
        moter_temperture = random.random() * 100
        moter_temperture = int(moter_temperture)
        throttle = random.random() * 100
        throttle = int(throttle)
        data1 = "{}".format(Fram_index)
        # data2 = "{}".format(i)
        data2 = "{}".format(Dc_current)
        data3 = "{}".format(Dc_voltage)
        data4 = "{}".format(Dc_power)
        data5 = "{}".format(Ac_current)
        data6 = "{}".format(Ac_voltage)
        data7 = "{}".format(motor_speed)
        data8 = "{}".format(controller_temperture)
        data9 = "{}".format(moter_temperture)
        data10 = "{}".format(throttle)
        message = {"id" : Fram_index ,"timestamp" : ts ,"current":Dc_current,"voltage":Dc_voltage,"power":Dc_power,"motor_speed":motor_speed,"controller_temperture":controller_temperture,"moter_temperture":moter_temperture,"throttle":throttle}
        myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
        print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
        t.sleep(1)
        i += 1
        # myAWSIoTMQTTClient.subscribe(TOPIC, 1, customCallback)

print('Publish End')
myAWSIoTMQTTClient.disconnect()
