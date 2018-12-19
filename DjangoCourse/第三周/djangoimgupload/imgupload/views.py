from django.shortcuts import render
from .models import PictureModel
from django.conf import settings
from django.http import HttpResponse
"""
图片上传:
1.将图片上传至static文件夹下；
2.将图片上传至自定义文件夹下；
"""

#第一种：上传至static文件夹下；
#1.配置static根所搜目录；
#2.配置图片上传之后，保存的文件目录；默认情况下，Django是将上传的图片保存在本地目录下:MEDIA_ROOT
#3.定义一个Model类，在Model声明一个用于保存图片地址的字段，放在数据库的表中；
#4.在html文件中添加上传文件的表单；点击上传

def uploadimg(request):
    if request.method=='GET':
        img=PictureModel.objects.get(id=5)
        print(img)
        return render(request, 'index.html',{'img':img})
        # return render(request,'index.html')
    else:
        #需要从表单input中，获取上传的文件对象(图片)
        pic=request.FILES.get('picture')

        #1.创建Model对象，保存图像路径到数据库
        model=PictureModel()
        model.pic_url='imguploadapp/'+pic.name
        print('---')
        model.save()
        #2.开始处理图片，将图片写入到指定目录。(/static/media/imguploadapp/)
        #拼接图片路径
        url=settings.MEDIA_ROOT+'/imguploadapp/'+pic.name
        with open(url,'wb') as f:
            # pic.chunks()循环读取图片内容，每次只从本地磁盘读取一部分图片内容，加载到内存中，并将这一部分内容写入到目录下，写完以后，内存清空；下一次再从本地磁盘取一部分数据放入内存。就是为了节省内存空间
            for data in pic.chunks():
                f.write(data)
        return HttpResponse('图片上传成功')