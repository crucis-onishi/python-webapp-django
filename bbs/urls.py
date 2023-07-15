from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # 一覧ページのビュー
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # 投稿詳細ページ
    path('create/', views.CreateView.as_view(), name='create'), # 新規投稿ページ
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'), # 投稿編集ページ
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'), # 削除ページ
    path('search/', views.search, name='search'), # 検索
]