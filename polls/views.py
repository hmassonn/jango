from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.template import loader
from .models import Product

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, product_id):
    # try:
    #     product = Product.objects.get(pk=product_id)
    # except Product.DoesNotExist:
    #     raise Http404("product does not exist")
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'polls/detail.html', {'product': product})

def results(request, product_id):
    response = "You're looking at the results of product %s."
    return HttpResponse(response % product_id)

def vote(request, product_id):
    return HttpResponse("You're voting on product %s." % product_id)

def index(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_product_list': latest_product_list,
    }
    return HttpResponse(template.render(context, request))