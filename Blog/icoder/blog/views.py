from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
# Create your views here.
def blogHome(request):
    allposts=Post.objects.all()
    context={'allposts':allposts}
    return render(request,'blog/blogHome.html',context)
def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    post.views = post.views + 1;
    post.save()
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
   
    context={'post':post,'comments':comments,'replies':replies}
   
    return render(request,'blog/blogPost.html',context)

def postComment(request):
    if request.method == 'POST':
        postSno=request.POST['postsno']
        slug=Post.objects.get(sno=postSno)
        comment=request.POST['comment']
        user=request.user
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST['parentSno']
       
        if parentSno == "":
         
          pComment=BlogComment(comment=comment,user=user,post=post)
          messages.success(request,'Your comment has been posted successfully')
        else:
          
           parent=BlogComment.objects.get(sno=parentSno)
           
           pComment=BlogComment(comment=comment,user=user,post=post,parent=parent)  
           messages.success(request,'Your reply has been posted successfully')
        pComment.save()
        
        return redirect(f"/blog/{post.slug}")
   