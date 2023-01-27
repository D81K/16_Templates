from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request):
    # print(request)  gives info about the request object
    # print(request.GET)  returns values brought by GET method
    # print(request.GET.get("q")) retturns the value of q
    # print(request.COOKIES) csrf token for protection
    # print(request.user)  AnonymousUser
    # print(request.path) /
    # print(request.method) GET
    # print(request.META) all informations about your request
    # if request.method == "POST":
    #     print("This is a POST METHOD!")
    # else:
    #     print('WHAT?')

    # html = "<html><body>Hello world!</body></html>"
    # return HttpResponse(html)

    # return render(request, "home/home.html")

    context = {
        'first_name': 'Gerard',
        'last_name': 'Yves',
        'age': 28,
    }

    return render(request, 'home/home.html', context)