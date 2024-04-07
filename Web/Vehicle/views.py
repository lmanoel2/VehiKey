from django.http import JsonResponse, HttpResponse

def vehicle(request):
    if request.method == 'GET':
        return HttpResponse('GET Vehicle OK')
    if request.method == 'POST':
        return HttpResponse('POST Vehicle OK')
