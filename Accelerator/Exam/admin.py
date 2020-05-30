from django.contrib import admin
from .models import acc_questions
# Register your models here.
class Question(admin.ModelAdmin):
    fields=('qno','qdesc','qtype','opt1_desc','opt2_desc','opt3_desc','opt4_desc','opt5_desc','opt6_desc','marks_carry','notes')

admin.site.register(acc_questions)