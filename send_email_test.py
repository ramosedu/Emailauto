from utils.emailmanager import LomaEmailSmtp
import smtplib, ssl
import requests

'''
LomaEmailSmtp requires an @gmail email address and may need configuration
changes to authenticate.
'''

try:
    resp = requests.get('https://blockchain.info/ticker')
    btc_price = resp.json().get('USD', {}).get('last', '')
    message = 'Bitcoin price is ${:,}'.format(btc_price)
except Exception as e:
    message = f'There was an error getting the bitcoin price {e}'
    
message += " Message generated by cron"
recipients = [""]
with open("/home/kali/Documents/Jobs/test/yolo.txt", 'r') as file:
    lines = file.readlines()
    username = lines[0].strip('\n')
    password = lines[1].strip('\n')


emailmanager = LomaEmailSmtp(username, password)
emailmanager.send_txt_email(recipients, message)
