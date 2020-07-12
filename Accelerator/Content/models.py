from django.db import models


# Create your models here.
class AccContent(models.Model):
    file = models.FileField(upload_to='cpe')

    class Meta:
        db_table = "acc_content"
