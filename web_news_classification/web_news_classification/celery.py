
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

# 创建Celery应用
app = Celery('web_news_classification')

# 从Django的设置中加载Celery配置
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动加载所有已注册的django app中的任务
app.autodiscover_tasks()

# 在这里设置定时任务，也可以在Django的settings中设置
app.conf.beat_schedule = {
    'train_model_every_week': {
        'task': 'home.tasks.train_model_task',  # task的全路径名
        'schedule': crontab(day_of_week=0, hour=0, minute=0),  # 每周日0点运行任务
    },
}