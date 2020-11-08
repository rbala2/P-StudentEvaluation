from django.db import models

# Create your models here.


class AccTestUploads(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "acc_test_bulk_uploads"
