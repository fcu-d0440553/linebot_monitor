from flask import Flask, request
import requests

def send_alert():
    # 在此處實現告警通知的邏輯，如使用LINE Notify API
    headers = {
        "Authorization": "Bearer " + 'Nn7y98CE3lEOge4ogKCp1lzkA6YjuysR7mJuHKgPwLA', 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': 'monitor故障!!' }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)

if __name__ == '__main__':
    try:
        # 用您的監控應用程式實際的URL替換下面的URL
        response = requests.post('https://9249-211-72-238-179.ngrok.io/check')
        if response.status_code != 200:
            print(f"Error sending POST to monitor: {response.status_code}")
            send_alert()
    except Exception as e:
        print(f"Error sending POST to monitor: {e}")
        send_alert()
