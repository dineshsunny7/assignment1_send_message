import requests
import json
import schedule
import time
import mysql.connector
# ******** collecting from database******
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="employee")
mycursor=mydb.cursor()
mycursor.execute("select * from empolyee_details")
result=mycursor.fetchall()
# API
URL="https://chat.googleapis.com/v1/spaces/AAAA-g_xaCI/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=90z-aSoITvCl00hIkBxhzBk7CoHWoOZW61vDpFFa5yI%3D"
# FUNCTION TO SEND MESSAGE
def send_message():
    string="ID     NAME     SALARY"+"\n"
    for i in range(len(result)):
        string=string+str(result[i][0])+"      "+str(result[i][1])+"   "+str(result[i][2])+"\n"
    message={'text':string}
    requests.post(URL,data=json.dumps(message))
    return

schedule.every(3).seconds.do(send_message)
while 1:
  schedule.run_pending()
  time.sleep(1)
