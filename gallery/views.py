from django.shortcuts import render
from gallery.models import Galeria


def gallery(request, gallery_id=None):

    galerias = Galeria.objects.all()
    return render(request, 'pages/gallery_select.html', {'lista': galerias})


def gallery_detail(request, gallery_id=None):

    galeria = Galeria.objects.get(id=gallery_id)
    fotos = galeria.fotos.all()

    return render(request, 'pages/gallery_detail.html', {'galeria': galeria,
                                                         'fotos': fotos})