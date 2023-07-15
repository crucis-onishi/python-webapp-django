from .forms import SearchForm

def search_form(request):
    return {'searchform': SearchForm()}