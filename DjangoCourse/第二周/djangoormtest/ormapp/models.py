from django.db import models

# Create your models here.
"""
model.py这个文件中定义的model模型，对应的是数据库中的表及字段。ORM

只要操作数据库，会出现两个新的命令
1.python manage.py makemigrations 作用：收集model.py文件中发生变化的模型类，执行完这个命令，如果出现NO changes detected，说明django没有检测到当前model发生变化。
2.python manage.py migrate 作用：将model模型的这些变化(增删改)同步至数据库中，因为model对应的就是表和字段，所以只要是model发生变化，一定要同步至数据库，保证model和数据库内容一致。

所以：第二个命令python manage.py migrate,在项目第一次运行的时必须执行，会生成Django框架内置的数据库到本地。
"""


# 如何向数据库中，添加自定义表以及相关字段。
# 1.定义一个model类：该类中声明字段；
# 2.执行makemigrations和migrate命令，将这个model类映射为数据库中的表；model类中的属性映射为表的字段；

class Person(models.Model):
    # primary_key=True:表示一个table表的主键，既然爬pid这个字段作为主键，那么这个字段默认带有一些约束：非空、唯一。需要指定一个默认值(但是需要手动更新默认值的，一般不设置)。
    # AutoField()表示的是一个自动递增的证书字段，一般用于表示主键。如果model中设置了主键，那么就表中就采用model设置的主键。如果model没有设置主键，表就会自动生成一个id主键
    pid = models.AutoField(primary_key=True)
    # max_length:用于设置这个字符串的长度。一般范围在0-255。根据内容长度的大小设置合适的max_length，主要是为了节省内存空间。
    # default=None
    user_name = models.CharField(max_length=20, default=None)
    # null=True表示数据库中的user_height字段的值可以为空，默认值是False
    # blank=True 表示html页面中，在填写这个字段时是否必须要填写，True表示页面中这个字段的数据可以忽略不写，False表示页面中这个字段的数据必须要填写。一般这个blank针对的是表单数据。
    user_height = models.IntegerField(null=True, blank=True)

    # null的值对字段的影响
    # null=False 非空：指的是user_name的值不能为NULL(等价于None)，保证user_name的值是存在的，即便是一个空字符串也表示非空。''也是一个对象。
    # Django在加载这些字段的时候，会依次读取每一个字段的默认值，如果model存在默认值就直接使用，如果model没有指定默认值，会采用Django内部封装的默认值。


class Meta:
    # 默认的表名是:当前app的名称_模型的名称
    db_table = 'people'
