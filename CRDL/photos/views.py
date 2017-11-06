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
