from base.models import Categoria
from django.core.cache import cache

def categorias_global(request):
    categorias = cache.get('categorias:padres')
    if categorias is None:
        categorias = Categoria.padres.all()
        cache.set('categorias:padres', categorias)
    return {'categorias_global': categorias}
