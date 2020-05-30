from django.db import models

# Create your models here.
class acc_questions(models.Model):
    qno = models.IntegerField()
    qdesc = models.TextField()
    qtype = models.CharField(max_length=10, default='OBJ')
    opt1_desc = models.CharField(max_length=4000, default='NA')
    opt2_desc = models.CharField(max_length=4000, default='NA')
    opt3_desc = models.CharField(max_length=4000, default='NA')
    opt4_desc = models.CharField(max_length=4000, default='NA')
    opt5_desc = models.CharField(max_length=4000, default='NA')
    opt6_desc = models.CharField(max_length=4000, default='NA')
    marks_carry = models.IntegerField(default=0)
    notes = models.CharField(max_length=400, null=True)

    class Meta:
        db_table = "acc_questions"
