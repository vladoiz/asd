from django.shortcuts import render

# Create your views here.
def admin_start(request):
    return render(request, 'my_admin/start_admin.html')