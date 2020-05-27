from django.http import HttpResponse


# Create view
def index(request):
    return HttpResponse("Hello world. You're at the polls index.")
