from django.db import models

# Create your models here.


class Homer(models.Model):
    """员工 任务记录"""
    name = models.CharField(max_length=20)  # 自动清理
    def __str__(self):
        return self.name
