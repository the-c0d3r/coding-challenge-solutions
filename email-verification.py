import random
import smtplib
import getpass

print("[+] Please Login to Continue")

while True:
    username = input("Enter email : ")
    if '@' not in username:
        print("[!] Username is invalid (xxx@gmail.com)")
    else:
        password = getpass.getpass("Enter Password : ")
        if password:
            break

data = "Verification Code is %d" % random.choice([i for i in range(000000,999999)])
try:
    mailServer = smtplib.SMTP('smtp.gmail.com:587')
    mailServer.starttls()
    mailServer.login(username,password)
    mailServer.send(username,username,data)
except smtplib.SMTPAuthenticationError:
    print("[!] Unable to login")
else:
    print("[+] Verification Code sent to email")