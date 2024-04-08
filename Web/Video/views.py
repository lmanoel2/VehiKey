from django.shortcuts import render


def video(request):
    if request.method == 'GET':
        return render(request, 'video.html')
    if request.method == 'POST':
        return render(request, 'video.html')
