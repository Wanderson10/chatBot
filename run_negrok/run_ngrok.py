import subprocess
import schedule
import time

def start_ngrok():
    ngrok_path = r"C:\caminho\para\ngronk\ngrok.exe"
    subprocess.Popen([ngrok_path, "http", "5000"])

start_ngrok()

schedule.every(1).hours.do(start_ngrok)

while True:
    schedule.run_pending()
    time.sleep(1)