# 如何在单独的.py文件中，使用django的运行环境。
import django, os

# 配置django的运行环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resultproject.settings')
# 启动django环境
django.setup()

from stuapp.models import StuModel

if __name__ == "__main__":
    for x in range(10):
        stu = StuModel()
        stu.name = 'a' + str(x)
        stu.age = '10' + str(x)
        stu.save()
