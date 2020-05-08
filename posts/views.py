from django.shortcuts import render
from .models import User, Image, Post
from django.views.generic import edit
from django.views import generic
from django.urls import reverse, reverse_lazy
from .forms import UserCreateForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
# Create your views here.
class UserCreateView(edit.CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'posts/user_create_form.html'
    success_url = reverse_lazy('posts:login')

def userlogin(request):
    if request.method =='POST':
        #if request method is post
        form = LoginForm(request.POST)

        if form.is_valid():
            #if form is valid
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            print('user is authenticated', user)
            if user is not None:
                #if user is authenticated
                login(request,user)
                return HttpResponseRedirect(reverse('posts:detail',args=[user.id]))
            else:
                #if user is not authenticated
                message = 'Invalid Credentials or Signup'
                form = LoginForm()
                return render(request,'posts/login.html',context = {'message':message,'form':form,})

        else:
            #if form validation fails
            message = 'Invalid form'
            form = LoginForm()
            return render(request,'posts/login.html',context={'message':message,'form':form})
    else:
        #if request method is get
        form = LoginForm()
        return render(request, 'posts/login.html',{'form':form})

def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('posts:login'))

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'posts/user_detail.html'

class SelectImage(generic.CreateView):
    fields = ['image_field']
    model = Image

    def form_valid(self,form):
        self.object= form.save(commit=False)
        self.object.uploaded_by = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:post-create',args=[self.object.uploaded_by.pk])

class CreatePost(generic.CreateView):
    fields=['title','image']
    model = Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.uploaded_by = self.request.user
        self.object.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('posts:detail',args=[self.object.uploaded_by.pk])

# class PostDetail(generic.DetailView, mixins.LoginRequiredMixin):
#     model = Post
#     template_name = 'posts/post_detail.html'
class PostDetail(generic.DetailView):
    model = Post

class PostList(generic.ListView):
    model = Post
