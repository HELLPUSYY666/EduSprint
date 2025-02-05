from django.contrib import admin

from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

    class Meta:
        model = Course
        fields = '__all__'
