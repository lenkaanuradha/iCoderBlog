from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from blog.models import Post
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    popular_posts=Post.objects.order_by('-views')[:3]
    context={'popular_posts':popular_posts}
    return render(request,'home/home.html',context)

def about(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'home/about.html',context)
def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        contact=Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
    return render(request,'home/contact.html')

def search(request):
    query=request.GET['query']
    if len(query) > 78 or len(query) == 0:
        allposts=Post.objects.none()
       
    else:
       allpoststitle=Post.objects.filter(title__icontains=query)
       allpostscontent=Post.objects.filter(content__icontains=query)
       allposts=allpoststitle.union(allpostscontent)
    if allposts.count() == 0:
     messages.warning(request,'No search results found.Please refine your query.')
    params={'allposts':allposts,'query':query}

    print(params)
    return render(request,'home/search.html',params)

def handlesignup(request):
    if request.method == 'POST':
      username=request.POST['name']   
      fname=request.POST['fname']
      lname=request.POST['lname']
      email=request.POST['email']
      password=request.POST['password']
      password2=request.POST['password2']
      if len(username) > 10:
         messages.error(request,"Your Username should be under 10 characters")
         return redirect('home')
      if password != password2:
         messages.error(request,"password and confirm password do not match")
      if not username.isalnum():
         messages.error(request,"Your username should be alphanumeric")
         return redirect('home')
         
      myuser=User.objects.create_user(username=username,email=email,password=password)
      myuser.fname=fname
      myuser.lname=lname
      myuser.save()
      messages.success(request,"Your iCoders account has been created successfully")
      return redirect('home')
    

    else:
      return HttpResponse("404 Page Not Found")
    
def handlelogin(request):
   if request.method == 'POST':
     username=request.POST['loginusername']
     password=request.POST['loginpassword']
     user=authenticate(username=username,password=password)
     if user is not None:
        login(request,user)
        messages.success(request,"You are successfully logged in")
        return redirect('home')
     else:
        messages.error(request,"Invalid credentials")
        return redirect('home')
   else:
      return HttpResponse("404-Not Found")
def handlelogout(request):
   logout(request)
   return redirect('home')