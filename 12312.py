from django.db import models

class Advertisement(models.Model):
    title = models.CharField('���������', max_lenght = 128)
    description= models.TextField('��������')
    price = models.DecimalField('����', max_digits=10, decimal_places=2)
    auction = models.BooleanField('����', help_text='�������� ���� ���� �������')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =T




































































































































































