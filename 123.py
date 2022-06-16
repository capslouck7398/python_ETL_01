from urllib import request as ur
import json , time , firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

with open('ETL_01.txt','r') as f:
  apiurl = f.read()

cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

url_array = ["001","005","009","013","017","021"]
for i in url_array:
  nowTime = int(time.time())
  struct_time = time.localtime(nowTime)
  timeString = time.strftime("%Y-%m-%d-%I:%M:%S-%P", struct_time)
  respone = json.loads(ur.urlopen("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-"+i+"?Authorization="+apiurl).read().decode('utf-8'))
  doc_ref = db.collection("homework").document("student01").collection("test01")
  doc_ref.document('weather-'+timeString+"-"+i).set({'weather':respone})




