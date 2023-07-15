from django.views import generic
from .models import Article
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import SearchForm

from django.contrib.auth.mixins import LoginRequiredMixin # インポート
from django.core.exceptions import PermissionDenied # インポート

class IndexView(generic.ListView):
    model = Article
    template_name = 'bbs/index.html'

class DetailView(generic.DetailView):
    model = Article
    template_name = 'bbs/detail.html'

# CreateViewクラスを作成
class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = ['content'] # 項目をcontentのみに変更

    #格納する値をチェック
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

# UpdateViewクラスを作成
class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = ['content'] # 項目をcontentのみに変更

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('編集権限がありません。')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

# DeleteViewクラスを作成
class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Article
    template_name = 'bbs/delete.html'
    success_url = reverse_lazy('bbs:index')

# 検索機能のビュー
def search(request):
    articles = None
    searchform = SearchForm(request.GET)

    # Formに正常なデータがあれば
    if searchform.is_valid():
        query = searchform.cleaned_data['query']
        articles = Article.objects.filter(content__icontains=query)
    return render(request, 'bbs/results.html', {'articles': articles, 'searchform': searchform})