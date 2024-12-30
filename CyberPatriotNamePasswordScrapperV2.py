#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import sys, os

#driver = webdriver.Chrome()
#driver.get("https://www.uscyberpatriot.org/Pages/Readme/cpxvi_tr_e_ubu22_readme_s985tr69sq.aspx")
#driver.get(sys.argv[1]) #the link you pass to it when run
#user_data = driver.find_elements(By.TAG_NAME, "pre")

#f = open("textdump.txt", "w")

#for i in user_data:
#	print(i.text)
#	f.write(i.text)

#f.close()

#Example link https://www.uscyberpatriot.org/Pages/Readme/cpxvi_tr_e_ubu22_readme_s985tr69sq.aspx
os.system("curl -o textdump.html " + "https://www.uscyberpatriot.org/Pages/Readme/cpxvi_tr_e_ubu22_readme_s985tr69sq.aspx")

f = open("textdump.html", "r")
r = open("textdumprefined.txt", "w")

presection = False
for line in f.readlines():
	if line.find("<pre>") !=-1:
		presection = True
		continue
	elif line.find("</pre>") !=-1:
		presection = False
		continue
	if presection == True:
		r.write(line)
r.close()
f.close()

f = open("textdumprefined.txt", "r")

Admin = ""
User = ""

halfway = False
for line in f.readlines():
	line = line.replace("<b>","").replace("</b>","")
	if line == "\n":
		continue
	if halfway == False:
		if line == "Authorized Administrators:\n":
			continue
		elif line == "Authorized Users:\n":
			halfway = True
			continue
		else:
			RefinedLine = line.replace(" ", "").replace("(you)","")
			if RefinedLine.find("password") == -1: #if password not found in file
				RefinedLine = RefinedLine.replace("\n","-")
			else:
				continue
			Admin = Admin + str(RefinedLine.replace("\n"," "))
	else:
		User = User + str(line.replace("\n", " "))

f.close()
UserArray = User.split(" ")
AdminArray = Admin.split("-")
x = open((sys.argv[1] + "/authorized_users"), "w")
for line in UserArray:
    if line == "":
        continue
    x.write(line + "\n")

for line in AdminArray:
    if line == "":
        continue
    x.write(line + "\n")

x.close()

x = open((sys.argv[1] + "/authorized_sudoers"), "w")

for line in AdminArray:
    if line == "":
        continue
    print(line)
    print(AdminArray[len(AdminArray)-2])
    if line == AdminArray[len(AdminArray)-2]:
        print("FOOBAR")
        x.write(line)
        break
    x.write(line + ", ")

x.close()

x = open((sys.argv[1] + "/autologin_user"), "w")
x.write(AdminArray[0])
x.close()


print("User: " + User)
print("Admin: " + Admin)
