from django.db import models

# Create your models here.
class AccQuestions(models.Model):
    qno = models.IntegerField()
    qdesc = models.TextField()
    qtype = models.CharField(max_length=10, default='OBJ')
    opt1_desc = models.CharField(max_length=4000, default='NA')
    opt2_desc = models.CharField(max_length=4000, default='NA')
    opt3_desc = models.CharField(max_length=4000, default='NA')
    opt4_desc = models.CharField(max_length=4000, default='NA')
    opt5_desc = models.CharField(max_length=4000, default='NA')
    opt6_desc = models.CharField(max_length=4000, default='NA')
    marks_carry = models.IntegerField(default=1)
    notes = models.CharField(max_length=4000, null=True)

    def __str__(self):
        return self.qdesc[:100]

    class Meta:
        db_table = "acc_questions"

class AccTests(models.Model):
    test_desc = models.CharField(max_length=100, unique=True)
    test_type = models.CharField(max_length=10, default='NA')
    test_duration = models.IntegerField(default=60)
    test_status = models.CharField(max_length=50, default='Open')
    total_questions = models.IntegerField(default=50)

    def __str__(self):
        return self.test_desc[:50]

    class Meta:
        db_table = "acc_tests"

class AccTestQuestions(models.Model):
    test_id = models.ForeignKey(AccTests, on_delete=models.CASCADE)
    question_id = models.ForeignKey(AccQuestions, on_delete=models.CASCADE)

    class Meta:
        db_table="acc_test_questions"
