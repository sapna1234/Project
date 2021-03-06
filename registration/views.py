from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserFoms

# Create your views here.
class  UserFormView(View):
    form_class = UserFoms
    template_name = 'user/Registration_form.html'

    #display balnk form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

     #process form data
    def post(self,request):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})

        if form.is_valid():

           user = form.save(commit=False)

           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user.set_password(password)
           user.save()


           user = authenticate(username=username , password=password)

           if user is not None:

              if user.is_active:
                 login(request,user)
                 return  render('index')

        return render(request, self.template_name, {'form': form})
