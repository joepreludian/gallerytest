from django.shortcuts import render


def gallery(request, gallery_id=None):
    return render(request, 'base.html')