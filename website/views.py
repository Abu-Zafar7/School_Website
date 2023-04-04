from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request,'website/base.html')


def homepage(request):
    return render(request,'website/index.html')


def about(request):
    return render(request,'website/about.html')


def academics(request):
    return render(request,'website/academics.html')

def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message was sent.")
            return redirect('contact')
    else:
        form = ContactForm()       
    return render(request,'website/contact.html',{'form':form}) 

    # return render(request,'website/contact.html')