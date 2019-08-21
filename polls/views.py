from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Product, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Product
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Product
    template_name = 'polls/results.html'



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
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'polls/results.html', {'product': product})

def vote(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        selected_choice = product.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the product voting form.
        return render(request, 'polls/detail.html', {
            'product': product,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(product.id,)))

def index(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_product_list': latest_product_list,
    }
    return HttpResponse(template.render(context, request))