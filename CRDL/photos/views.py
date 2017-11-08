from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from .forms import PhotoForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login

import os
import sys

# Create your views here.
def hello(request):
    return HttpResponse('HELLO WORLD!')

def detail(request, pk):
    # photo = Photo.objects.get(pk=pk)
    photo = get_object_or_404(Photo, pk=pk)

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )

    #FACE RECOGNITION
    client_id = "5zovqRQc2MKOPbpBMOvA"
    client_secret = "L2gb7YtMce"
    url = "https://openapi.naver.com/v1/vision/face"  # 얼굴감지
    files = {'image': open('uploads/2017/11/07/orig/3.jpg', 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    response = HttpResponse.post(url, files=files, headers=headers)
    rescode = response.status_code
    if (rescode == 200):
        print (response.text)
    else:
        print("Error Code:" + rescode)

    return HttpResponse('\n'.join(messages))

@login_required
def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect(obj)

    ctx = {
        'form': form,
    }

    return render(request, 'edit.html', ctx)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('')

        else:
            form = UserForm()
            return render(request, 'progiles/signup.html', {'form': form})
