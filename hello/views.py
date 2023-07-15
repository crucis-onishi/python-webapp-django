from django.views import generic
from .models import Article

# IndexView クラスを作成
class IndexView(generic.ListView):
    model = Article
    template_name = 'hello/index.html' # テンプレート名を指定