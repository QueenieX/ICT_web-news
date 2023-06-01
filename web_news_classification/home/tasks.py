from future import absolute_import, unicode_literals
from celery import shared_task
import runpy

@shared_task
def train_model_task():
    runpy.run_path('ICT_web-news-MachineLearning/ANN_Model.py')  # 运行你的Python文件
    return 'Model training completed'