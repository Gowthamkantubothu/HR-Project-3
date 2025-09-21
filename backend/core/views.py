from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to HR Project 3 API"})
