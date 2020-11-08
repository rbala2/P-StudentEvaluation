from django.conf import settings
from django.db import models


# Create your models here.
class AccQuestions(models.Model):
    qno = models.IntegerField()
    qdesc = models.TextField()
    qtype = models.CharField(max_length=10, default='OBJ')
    category = models.CharField(max_length=10, default='GEN')
    sub_category = models.CharField(max_length=10, default='GEN')
    opt1_desc = models.CharField(max_length=4000, default='NA')
    opt2_desc = models.CharField(max_length=4000, default='NA')
    opt3_desc = models.CharField(max_length=4000, default='NA')
    opt4_desc = models.CharField(max_length=4000, default='NA')
    opt5_desc = models.CharField(max_length=4000, default='NA')
    opt6_desc = models.CharField(max_length=4000, default='NA')
    marks_carry = models.IntegerField(default=1)
    answer = models.CharField(max_length=100, default='NA')
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
    negative_marking = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    total_marks = models.IntegerField(default=50)

    def __str__(self):
        return self.test_desc[:50]

    class Meta:
        db_table = "acc_tests"


class AccTestQuestions(models.Model):
    test_id = models.ForeignKey(AccTests, on_delete=models.CASCADE)
    question_id = models.ForeignKey(AccQuestions, on_delete=models.CASCADE)

    class Meta:
        db_table = "acc_test_questions"


class AccResultsSummary(models.Model):
    student_id = models.CharField(max_length=10, default=None)
    testid = models.IntegerField(default=0)
    test_desc = models.CharField(max_length=100, default=None)
    session = models.CharField(max_length=200, primary_key=True)
    test_start_time = models.DateTimeField(null=True, blank=True)
    test_end_time = models.DateTimeField(null=True, blank=True)
    test_result_status = models.CharField(max_length=20, default='NA')
    marks_obtained = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total_marks = models.IntegerField(default=0)
    questions_attempted = models.IntegerField(default=0)
    answered_correct = models.IntegerField(default=0)
    answered_wrong = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)

    class Meta:
        db_table = 'acc_results_summary'


class AccResults(models.Model):
    login_id = models.CharField(max_length=30)
    session = models.ForeignKey(AccResultsSummary, on_delete=models.CASCADE,default=None)
    testid = models.ForeignKey(AccTests, on_delete=models.CASCADE)
    qno = models.IntegerField(default=-1)
    qtype = models.CharField(max_length=10)
    answer_desc = models.CharField(max_length=4000, default='NA')
    answer_fill = models.CharField(max_length=4000, default='NA')
    answer_obj = models.CharField(max_length=100, default='NA')
    student_id = models.CharField(max_length=10, default=None)
    test_starttime = models.DateTimeField()
    test_endtime = models.DateTimeField()

    class Meta:
        db_table = "acc_results"


class AccStudentTests(models.Model):
    student_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    test_id = models.ForeignKey(AccTests, on_delete=models.CASCADE)
    test_assigned_dt = models.DateTimeField(null=True, blank=True)
    test_taken_dt = models.DateTimeField(null=True, blank=True)
    test_expiry_dt = models.DateTimeField(null=True, blank=True)
    test_status = models.CharField(max_length=50, default='Ready')

    class Meta:
        db_table = 'acc_student_tests'


