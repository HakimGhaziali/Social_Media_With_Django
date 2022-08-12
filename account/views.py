from django.shortcuts import render
from django.views.generic import View
from .forms import RegisterForm


class RegisterView(View):

    def get(self , request):

        form = RegisterForm()
        
        return render(request , 'account/register.html' , {'form': form } )

    
    def  post(self, request):
        return render(request , 'account/register.html')