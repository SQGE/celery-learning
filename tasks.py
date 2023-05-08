import time
from celery import Celery

broker = 'redis://:123456@172.16.200.249:6379/1'
backend = 'redis://:123456@172.16.200.249:6379/2'

app = Celery('my_task', broker=broker, backend=backend)

@app.task
def add(x, y):
    print('enter call func ...')
    time.sleep(5)
    return x + y
