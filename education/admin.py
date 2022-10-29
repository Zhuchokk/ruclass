from django.contrib import admin
from .models import Course, Task


class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ['members']


admin.site.register(Course, CourseAdmin)
admin.site.register(Task)