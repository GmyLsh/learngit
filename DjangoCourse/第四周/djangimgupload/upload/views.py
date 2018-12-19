from django.shortcuts import render
from upload.models import Picture
from django.http import HttpResponse
# Create your views here.
def uploadimg(request):
    if request=='GET':
        img = Picture.objects.get(id=1)
        return render(request,'index.html',{'img':img})
    else:
        file=request.FILES.get('pic')
        pic=Picture(pic_url=file)
        pic.save()

        return HttpResponse('ok')