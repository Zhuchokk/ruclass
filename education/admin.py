from django.contrib import admin
from .models import Course, Task, Work
from django_summernote.admin import SummernoteModelAdmin


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ['members']


class WorkAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', )

admin.site.register(Course, CourseAdmin)
admin.site.register(Task)
admin.site.register(Work, WorkAdmin)