from django.shortcuts import render
from .models import Produto
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'home.html')

def lista_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    try:
        data['list'] = Produto.objects.all()
    except:
         data['error'].append("Erro ao carregar Produto! ")
    return render(request, 'produto.html', data)

@csrf_exempt
def novo_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'POST':
        id = int(request.POST.get('id', -1))
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        try:
            if (id == -1):
                prod = Produto(nome=nome, descricao=descricao, preco=preco)
                prod.save()
            else:
                prod = Produto.objects.get(id=id)
                prod.nome = nome
                prod.descricao = descricao
                prod.preco = preco
                prod.save()
        except:
            data['error'].append("produto nao cadastrado - Erro! ")
            return render(request, 'produto.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar Produto! ")
            return render(request, 'produto.html', data)
        return render(request, 'produto.html', data)
    else:
        data['error'].append("Erro ! ")
        return render(request, 'produto.html', data)

def deletar_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        try:
            prod = Produto.objects.get(id=id)
            prod.delete()
        except:
            data['error'].append("Erro ao deletar o produto ")
            return render(request, 'produto.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar Produto! ")
            return render(request, 'produto.html', data)
        return render(request, 'produto.html', data)
    else:
        data['error'].append("Erro ! ")
        return render(request, 'produto.html', data)
        
def atualizar_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    data['prod'] = []
    if request.method == 'GET':
        id = request.GET.get('id')
        try:
            data['prod'].append(Produto.objects.get(id=id))
        except:
            data['error'].append("Erro ao carregar produtos! ")
            return render(request, 'produto.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar produtos! ")
            return render(request, 'produto.html', data)
        return render(request, 'produto.html', data)
    else:
        data['Error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'produto.html', data)

        