import configparser
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

config=configparser.ConfigParser()
config.read("config.ini")

def sendMailUsingSendGrid(API,from_email,to_email,subject,html_content):
    if API!=None and from_email!=None and len(to_email)>0:
        message=Mail(from_email,to_e
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)

mail,subject,html_content)
        try:
            sg = SendGridAPIClient(API)        except Exception as e:
            print(e.message)



try:
    settings=config["SETTINGS"]
except:
    settings={}

API = settings.get("APIKEY",None)
from_email=settings.get("FROM,None")
to_email=settings.get("To","")

subject="Sample Test"
html_content="Message successfully sent"




