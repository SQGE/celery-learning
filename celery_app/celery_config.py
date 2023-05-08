from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://:123456@172.16.200.249:6379/1'
CELERY_RESULT_BACKEND = 'redis://:123456@172.16.200.249:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

# 导入任务
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),  # 10秒执行一次
        'args': (2, 8)
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=15, minute=46), # 定时执行
        'args': (3, 2)
    }
}
