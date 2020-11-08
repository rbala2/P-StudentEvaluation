from django.db import models

# Create your models here.


class AccTestUploads(models.Model):
    file = models.FileField(upload_to='uploads')

    class Meta:
        db_table = "acc_test_bulk_uploads"
