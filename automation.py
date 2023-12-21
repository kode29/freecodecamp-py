from credentials import mobile_number
import requests

# Python schedule DOCS: pypi.org/project/schedule/
import schedule
import time
# Although CRON should be recommended

def send_message():
    resp = requests.post("https://textbelt.com/text", {
        'phone': mobile_number,
        'message': 'Hello from Python',
        'key': 'textbelt'
    })
    print(resp.json())
    
# schedule.every().day.at('08:00').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)