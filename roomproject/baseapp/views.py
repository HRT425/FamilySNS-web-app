from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import List

# Create your views here.

def notfunc(request):
    return redirect('roomapp:signup')

# サインアップ画面を表示
def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'accounts/main.html', {})
        except IntegrityError:
            return render(request, 'accounts/signup.html', {'error':'このユーザは既に登録されています'})
    return render(request, 'accounts/signup.html', {})

# ログイン画面を表示
def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('roomapp:main')
        else:
            return render(request, 'accounts/login.html', {'error':'username又はpasswordが間違っています'})
    return render(request, 'accounts/login.html', {'context':'get method'})

# ログアウトされたらログイン画面に移動
def logoutfunc(request):
    logout(request)
    return redirect('roomapp:login')

# メイン画面を表示
def mainfunc(request):
    return render(request, 'accounts/main.html', {})

# リスト画面を表示
class HomeList(LoginRequiredMixin, ListView):
    model = List
    template_name = 'list/list.html'

    def get_queryset(self):
        return List.objects.exclude(user=self.request.user)

class MyList(LoginRequiredMixin, ListView):
   """自分の投稿のみ表示"""
   model = List
   template_name = 'list/mylist.html'

   def get_queryset(self):
       return List.objects.filter(user=self.request.user)

# リストを作る
class ListCreate(CreateView):
    template_name = 'list/create_list.html'
    model = List
    fields = ('title', 'content')
    success_url = reverse_lazy('roomapp:mylist')

    def form_valid(self, form):
       """投稿ユーザーをリクエストユーザーと紐付け"""
       form.instance.user = self.request.user
       return super().form_valid(form)

# リストを更新する
class ListUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'list/update_list.html'
    model = List
    fields = ('title', 'content')
   
    def get_success_url(self,  **kwargs):
       """編集完了後の遷移先"""
       pk = self.kwargs["pk"]
       return reverse_lazy('roomapp:detail_list', kwargs={"pk": pk})

    def test_func(self, **kwargs):
        pk = self.kwargs["pk"]
        post = List.objects.get(pk=pk)
        return (post.user == self.request.user)

    def form_valid(self, form):
       """投稿ユーザーをリクエストユーザーと紐付け"""
       form.instance.user = self.request.user
       return super().form_valid(form)
    
# リストの詳細を表示
class ListDetail(DetailView):
    model = List
    template_name = 'list/detail_list.html'

# リストを消す
class ListDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   """投稿編集ページ"""
   model = List
   template_name = 'list/delete_list.html'
   success_url = reverse_lazy('roomapp:mylist')

   def test_func(self, **kwargs):
       """アクセスできるユーザーを制限"""
       pk = self.kwargs["pk"]
       post = List.objects.get(pk=pk)
       return (post.user == self.request.user)