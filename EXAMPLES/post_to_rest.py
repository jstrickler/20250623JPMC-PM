from datetime import datetime
import time
import requests
import json

URL = 'http://httpbin.org/post'

for i in range(1, 4):
    data = {
        'date': datetime.now().ctime(),
        'label': 'test_' + str(i)
    }
    response = requests.post(  # POST data to server
        URL,
        # data=data,
        json=json.dumps(data),
        cookies={'python': 'testing'},
        headers={'X-Python': 'Guido van Rossum'},
    )
    if response.status_code in (requests.codes.OK, requests.codes.created):
        print(response.status_code)
        print(response.text)
        print()
        time.sleep(2)

