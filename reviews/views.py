from django.shortcuts import render
from .models import Reviews
from django.views.generic import DetailView, ListView

# Create your views here.
def reviews(request):
    return render(request, 'reviews/Review.html')


class Show_review_list(ListView):
        
    model = Reviews
    template_name = 'reviews/Review.html'
    context_object_name = 'reviewget'
    paginate_by = 3

    def get_context_data(self, **kwards):
        ctx=super(Show_review_list, self).get_context_data(**kwards)
        return ctx