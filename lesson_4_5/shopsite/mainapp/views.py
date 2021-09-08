from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
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
    else:
        form = GoodForm()
    template_name = 'mainapp/good_create.html'
    return save_good_form(request, form, template_name)


def save_good_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            goods = get_goods()
            context = {
                'goods': goods
            }
            data['html_good_list'] = render_to_string('mainapp/include/partial_goods_list.html',
                                                      context=context)
        else:
            data['form_is_valid'] = False
            print(f'Error form validation!\n{form.errors}')
    context = {
        'title': 'Добавление товара',
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request)
    return JsonResponse(data)
