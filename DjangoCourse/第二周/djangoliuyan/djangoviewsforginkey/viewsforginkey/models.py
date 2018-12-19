from django.db import models


# Create your models here.
# 数据库:一对多。他指的是两个表之间的关系，一指的是主表中的一条数据，多指的是从表中的多条数据。
# 两个表：
# 班级表(1班，2班，3班)
# 学生表(张三-1，李四-1，王五-1，赵六-2，麻子-3，小明-2)
# 这两个表:班级表就是主表，因为班级表一条数据(比如1班)对应了学生表的多条数据，所以学生表是从表。
class Classes(models.Model):
    """
    这是班级表，是主表；
    """
    c_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'classes'


class Student(models.Model):
    """
    这是从表，学生表;
    主表中的一条数据可以对应从表中的多条数据；
    从表中的一条数据只能对应主表中的一条数据
    """
    s_name = models.CharField(max_length=20)
    # 如何在从表中关联主表的ID?
    # ForeignKey()外键，在Student表中，关联外部表Classes的主键，所以称为外键。
    # on_delete:必须设置。表示从表数据所关联的主表数据被删除以后，从表应该怎么办。
    # 1.如果主表数据丢失，从表对应的数据也全部删除
    # 比如:张三、李四、王五关联的都是1班，如果1班这条数据被删除了，那么，对应的张三、李四、王五也全部删除；
    # 2.SET_NULL:如果主表数据删除，从表数据保留，但是这种外键的关联关系classes_id设置为NULL。


    #从表关联两个主表的外键。related_name指定外键的关联名称，这个名称是用于将来查询数据使用的。只在主表查从表时会用到。
    classes_one = models.ForeignKey(Classes, on_delete=models.CASCADE,related_name='cls_one')
    classes_two =models.ForeignKey(Classes,on_delete=models.CASCADE,related_name='cls_two')

    class Meta:
        db_table = 'student'
