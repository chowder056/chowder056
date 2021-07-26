from django.db import models

class caosnews(models.Model):
       nombre_caosnews=models.CharField(max_length=50)
       apellido_caosnews=models.CharField(max_length=50)
       rut = models.CharField(max_length=12, null= True)
       correo_caosnews=models.EmailField()
       contraseña_caosnews=models.CharField(max_length=50)
       con_contraseña_caosnews=models.CharField(max_length=50)
       pais=models.CharField(max_length=50,null=True)
       direccion=models.CharField(max_length=50,null=True)


class corta(models.Model):
       chiste=models.CharField(max_length=300)
       resp=models.CharField(max_length=300)



