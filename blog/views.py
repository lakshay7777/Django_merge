from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Comment
from .forms import PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserSignUpForm
from .forms import userloginForm
from .forms import ProfileForm
from django.contrib import auth
from .models import Profile
from django.contrib.auth.models import User

###############################################################################
from django.urls import reverse





# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)
    # Post.objects.get(pk=pk)
    
def post_detail(request, slug):
    if request.method == "POST":
        reply = request.POST.get('reply', None,)
        parent = request.POST.get('comment', None)
        comment = Comment.objects.filter(id=parent).first()
        post = get_object_or_404(Post, slug=slug)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        text = request.POST.get('text', None)
        
        if comment is not None:
            Comment.objects.create(text=reply, post=post, parent=comment)
        else:
            print('y')
            Comment.objects.create(name=name, email=email, text=text, post=post)
        return redirect(reverse('post_detail', kwargs={'slug': post.slug}))
    else:
        post = get_object_or_404(Post, slug=slug)
        comment = Comment.objects.filter(post=post, parent__isnull=True)
        return render(request, 'blog/post_detail.html', {'post': post, 'comment': comment})
#def post_detail(request, slug):
    #post = get_object_or_404(Post, slug=slug)
   #return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            
            ######################
            post.tag.clear()
            tag = request.POST.getlist('tag', '')
            for tag in tag:
                tag = tag.strip()
                if tag:
                    post.tag.add(tag)
            
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# def userSignUpViews(request):
#     if request.method == 'POST':
#         form = UserSignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserSignUpForm()
#     return render(request, 'blog/signup.html', {'form': form})
from django.contrib.auth.hashers import make_password

def userSignUpViews(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)  # Hash the password
            user.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserSignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

# def login(request):
#     if request.method=="POST":
#         username = request.post['username']
#         password = request.post['password']
#         user = auth.authenticate(username=username , password=password)

#         if user is not None:
#             auth.login(request.user)
#             return render ('post_list')
        
#     return render(request,'blog/login.html')    



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password, "password>>>>>>>>>>>>>>>>>")
        user = authenticate(username=username, password=password)
        # print(user, "user>>>>>>>>>>>>>>>>>>>>>>>>>")
        if user is not None:   
            print("----====------")
            login(request,user=user)
            messages.success(request,"You are now logged in as {username}")
            return redirect("post_list")
        # print('request data>>>>>>>>>>>>>>>>')
        # form = userloginForm(data=request.POST)
        # print(form.errors, "form error>>>>>>>>>>>")
        # if form.is_valid():
        #     print("foem valid>>>>>>>>>>>>>")
        #     username = form.cleaned_data.get('username')
        #     password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=password)
            # print(user, "user>>>>>>>>>>>>>>>>>>>>>>>>")
            # if user is not None:
            #     login(user)
            #     messages.success(request,"You are now logged in as {username}")
            #     return redirect("post_list")
        # else:
        #     messages.error(request, "Invalid username or password.")
    form = userloginForm()
    print("else blank foerm>>>>>>>>>>>>>>")
    return render(request, "blog/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('post_list')  # Redirect to a home page or another page

# def home(request):
#     return render(request, 'home.html')

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'blog/profile.html', {'user': user})

# @login_required
# def profile_view(request):
#     Profile = Profile.objects.get(user=request.user)
#     return render(request, 'blog/profile.html', {'Profile': Profile})

# def userlogin(request):
#     if request.method == 'POST':
#         form = userloginForm(request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('post_list')
#     else:
#         form = userloginForm()
#     return render(request, 'blog/login.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     return redirect('login')

# @login_required
# def profile_view(request):
#     return render(request, 'blog/profile.html', {'user': request.user})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'blog/profile_edit.html', {'form': form})


###################################################################33

#class AddCommentView(CreateView)

#######
#3########