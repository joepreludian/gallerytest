from django.db import models
from versatileimagefield.fields import VersatileImageField


class Galeria(models.Model):
    nome = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nome

    @property
    def fotos_quantidade(self):
        return self.fotos.count()


class Foto(models.Model):
    galeria = models.ForeignKey(Galeria, related_name='fotos')
    foto = VersatileImageField(upload_to='galeria/')

    def __unicode__(self):
        return 'Foto #%s - %s' % (self.id, self.galeria)
