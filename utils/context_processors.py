from base.models import Categoria

def categorias_global(request):
  return {'categorias_global': Categoria.padres.all()}
