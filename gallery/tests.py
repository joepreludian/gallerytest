from django.test import TestCase
from gallery.models import Galeria, Foto

import os
from django.conf import settings


class MyAppViewsTests(TestCase):
    def setUp(self):
        image_root = os.path.abspath(os.path.dirname(__file__))

        self.galeria = Galeria(nome="Minha galeria teste")
        self.galeria.save()

        self.foto1 = Foto(galeria=self.galeria,
                          foto=os.path.join(image_root, 'testdata/image.jpg'))
        self.foto1.save()

        self.foto2 = Foto(galeria=self.galeria,
                          foto=os.path.join(image_root, 'testdata/image.jpg'))
        self.foto2.save()

    def tearDown(self):
        pass

    def test_gallery(self):
        self.assertEqual(self.galeria.nome, 'Minha galeria teste')

    def test_gallery_photos(self):
        self.assertEqual(self.galeria.fotos.count(), 2)

    def test_photos(self):
        self.assertNotEqual(self.foto1.foto.name.find('testdata/image.jpg'), -1)

