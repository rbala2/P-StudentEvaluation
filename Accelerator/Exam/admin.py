from django.contrib import admin
from .models import AccQuestions,AccTests,AccTestQuestions,AccStudentTests
# Register your models here.
class Question(admin.ModelAdmin):
    fields=('qno','qdesc','qtype','opt1_desc','opt2_desc','opt3_desc','opt4_desc','opt5_desc','opt6_desc','marks_carry','notes')

class Tests(admin.ModelAdmin):
    fields=('test_desc','test_type','test_duration','test_status')

class TestQuestions(admin.ModelAdmin):
    fields=('question_id_id','test_id_id')

class StudentTests(admin.ModelAdmin):
    fields=('student_id_id','test_id_id')

admin.site.register(AccQuestions)
admin.site.register(AccTests)
admin.site.register(AccTestQuestions)
admin.site.register(AccStudentTests)