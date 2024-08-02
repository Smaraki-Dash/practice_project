from django.shortcuts import render
from .models import*
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request,'home.html')

def home(request):
    rollno='2'
    name='anny'
    pno='9861153750'
    email='anny@gmail.com'
    cls='12'
    st=Student(name=name, rollno=rollno, pno=pno, email=email, cls=cls)
    st.save()
    user={'rollno':rollno, 'name':name, 'pno':pno, 'email':email, 'cls':cls}
    return render(request,'home.html', user)

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        empo=emp(name=name, pno=pno, email=email, username=un, pw=pw)
        empo.save()
        return HttpResponse('Registered successful')
    return render(request,'register.html')


