import requests
import sys

def imdone(chapter, exercise):
    try:
        r = requests.get(f'https://206-167-181-43.cloud.computecanada.ca:8080/chap{chapter}ex{exercise}')
        if r.status_code < 200 or r.status_code >= 300:
            print(f"Failed to connect to server ({r.status_code})", file=sys.stderr)
    except:
        print("Failed to connect to server", file=sys.stderr)
