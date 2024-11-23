from django.db import models

# Create your models here.
class usuarios(models.Model):
    id=models.AutoField(primary_key=True)
    nombre_completo=models.CharField(max_length=45,null=False)
    contrasena=models.CharField(max_length=45,null=False)
    correo=models.CharField(max_length=45,null=False)
    nombre_usuario=models.CharField(max_length=45,null=False)

    def __str__(self):
     return self.nombre_completo+" "+self.correo+" "+self.contrasena+" "+self.nombre_usuario

class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre_completo=models.CharField(max_length=45,null=False)
    contrasena=models.CharField(max_length=45,null=False)
    correo=models.CharField(max_length=45,null=False)
    nombre_usuario=models.CharField(max_length=45,null=False)

    def __str__(self):
     return self.nombre_completo+" "+self.correo+" "+self.contrasena+" "+self.nombre_usuario
