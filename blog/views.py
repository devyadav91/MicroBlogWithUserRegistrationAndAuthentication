from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import SignUpForm, LogInForm, AddPostForm
from django.contrib import messages
from django.views.generic.list import ListView
from .models import article
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import Group

class home(ListView):
    model = article
    fields = ['title','content']
    template_name = 'home.html'

def about(request):
    return render(request,'about.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LogInForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upassword = form.cleaned_data['password']
                user = authenticate(username=uname,password=upassword)
                if user is not None:
                    login(request,user)
                    messages.success(request,"logged in success !!")
                    return HttpResponseRedirect('/dashboard')
        else:
            form = LogInForm()
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)
            messages.success(request,"User created !!!")
            return HttpResponseRedirect('/login')
    else:
        form=SignUpForm()
    context = {'form':form}
    return render(request,'signup.html',context)


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        fullName = user.get_full_name()
        grp = user.groups.all()
        ip =  request.META.get('REMOTE_ADDR')
        posts = article.objects.all().order_by("-id")
        return render(request,'dashboard.html',{'posts':posts,'fullName':fullName,'groups':grp,'ip':ip})
    else:
        return HttpResponseRedirect('login')

def PostForm(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            form.author= request.user
            if form.is_valid():
                form.save()
                messages.success(request,"form saved successfully !!")
                return HttpResponseRedirect('/dashboard')
            else:
                return HttpResponseRedirect('/postarticle')
        else:
            form = AddPostForm()
            return render(request,'post.html',{'form':form})  
    return HttpResponseRedirect('/login') 

def UpdatePost(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            GetPost = article.objects.get(id=pk)
            form = AddPostForm(request.POST,instance=GetPost)
            form.author= request.user
            if form.is_valid():
                form.save()
                messages.success(request,"form saved successfully !!")
                return HttpResponseRedirect('/dashboard')
            else:
                return HttpResponseRedirect('/updatepost/pk')
        else:
            GetPost = article.objects.get(id=pk)
            form = AddPostForm(instance=GetPost)
            return render(request,'post.html',{'form':form})  
    return HttpResponseRedirect('/login')

def DeletePost(request,pk):
    if request.user.is_authenticated and request.user.has_perm('applications.admin_access'): # check authentication as well as group permissions
        post = article.objects.get(pk=pk)
        if request.method=='POST':
            post.delete()
            messages.success(request,"Post Deleted Successfully !!")
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request,'DeletePost.html',{'post':post})
    else:
        return HttpResponseRedirect('/login')  
    