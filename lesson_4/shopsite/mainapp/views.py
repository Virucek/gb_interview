from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mainapp.models import Goods
from mainapp.forms import GoodForm


def get_goods():
    return Goods.objects.all()


def main(request):
    context = {
        'title': 'Товары',
        'goods': get_goods(),
    }
    return render(request, 'mainapp/goods_list.html', context=context)


def create_good(request):
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('goods:goods_list'))
    else:
        form = GoodForm()
    context = {
        'title': 'Добавление товара',
        'form': form
    }
    return render(request, 'mainapp/good_create.html', context=context)
