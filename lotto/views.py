from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import GuessNumbers
from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    
    lottos = GuessNumbers.objects.all()
    
    return render(request, 'lotto/default.html',{'lottos':lottos})

def post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            lotto = form.save(commit=False)
            print(type(lotto))
            print(lotto)
            lotto.generate()
            return redirect('index')
        else:
            form = PostForm()
            return render(request, "lotto/form.html",{"form":form})
        
    form = PostForm() # 상단 from .forms import PostForm 추가
    return render(request, "lotto/form.html", {"form": form})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, World!</h1>")

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/detail.html", {"lotto":lotto})