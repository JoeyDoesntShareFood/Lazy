import pyrebase

config = {
    "apiKey": "AIzaSyDYWRcuwOEDLvdRq6nVDrpnoCO2bXybWb4",
    "authDomain": "dhishna-test.firebaseapp.com",
    "databaseURL": "https://dhishna-test.firebaseio.com",
    "projectId": "dhishna-test",
    "storageBucket": "dhishna-test.appspot.com"
} 
# config = {
# 	"apiKey" : "AIzaSyAZHCLuovX2oNhccuxjetkHNgAcrWcZLGo",
#     "authDomain": "dhisna-ac7e0.firebaseapp.com",
#     "databaseURL": "https://dhisna-ac7e0.firebaseio.com",
#     "projectId": "dhisna-ac7e0",
#     "storageBucket": "dhisna-ac7e0.appspot.com"
# } 

firebase = pyrebase.initialize_app(config)


print("Fetching the names of the departments.")
db = firebase.database()
depts = []
temp = db.child("events").get()
for dep in temp.each():
	depts.append(dep.key())

print("Fetching the names of the events.")
deptEventsList = []
for dep in depts:
	deptEventsList.append([])	
	temp = db.child("events").child(dep).get()
	for event in temp.each():
		deptEventsList[-1].append(event.key())

print("Event names fetched.")
for x in xrange(0, len(depts)):
	for y in xrange(0,len(deptEventsList[x])):
		print("events.add( " + deptEventsList[x][y] + " );")
