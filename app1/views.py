from django.http import HttpResponse
def homepage(request):
    return HttpResponse('this is the home page off app1')
def about(request):
    return HttpResponse('this is the about page off app1')
    