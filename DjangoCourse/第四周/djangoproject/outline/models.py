from django.db import models
from stage.models import Stage
class Outline(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    days = models.IntegerField(null=True)
    advancing = models.CharField(max_length=255, null=True)
    number = models.IntegerField(null=False)
    remark = models.CharField(max_length=255, null=True, blank=True,
                              verbose_name='备注')
    status = models.IntegerField(null=True)
    creater = models.IntegerField(null=True, verbose_name='添加人')
    create_time = models.DateTimeField(null=False, auto_now_add=True,
                                       verbose_name='添加时间')
    updater = models.IntegerField(null=True, blank=True)
    update_time = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        db_table = 'outline'
        verbose_name = '教学大纲信息'
        verbose_name_plural = verbose_name
        ordering = ['number']
