
from django.test import TestCase
from GRUPO_Q11.GCPM.models import Usuario


class UsuarioTest(TestCase):
    def setUp(self):
        user = Usuario(nombre_usuario='user1', nombre='nom', apellido='ap')
        user.set_password('password')

    def testListar(self):
        usuarios = Usuario.objects.all()
        self.assertEqual(usuarios.count(),1)