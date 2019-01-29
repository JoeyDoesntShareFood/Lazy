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

depts.remove("acc")
depts.remove("pre")

for x in deptEventsList:
    if ('female' in x) or ('Make-a-Ton' in x):
            deptEventsList.remove(x)



print("Starting downloads.")
storage = firebase.storage()



# curDept = depts[0]
# curEvent = deptEventsList[0][0]
# print("Department: " + curDept)
# print("Event: " + curEvent )
storage.child("events").child("event.xml").put("a.svg")
		
for x in xrange(0, len(depts)):
	curDept = depts[x]
	print("Department: " + curDept + "(" + str(x+1) + " out of " + str(len(depts)) + ")")
	for y in xrange(0,len(deptEventsList[x])):
		curEvent = deptEventsList[x][y]
		print("Event: " + curEvent + "(" + str(y+1) + " out of " + str(len(deptEventsList[x])) + ")")
		print("Downloading...")
		storage.child("events").child(curDept).child(curEvent).child("event.svg").download("a.svg")
		print("Download finished.")
		print("Processing...")

# Enter processing stuff here.

		print("Uploading...")
		#uploads to the database. HANDLE WITH CARE.
		#storage.child("events").child(curDept).child(curEvent).child("event.xml").put("a.svg")
		print("Upload finished. Press enter to download next.")
		ent = raw_input("")
		
		
		
from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", 'PATH TO DESKTOP')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(firefox_profile=profile)
driver.get("Name of web site I'm grabbing from")
driver.find_element_by_xpath("//a[contains(text(), 'DEV.tgz')]").click()
