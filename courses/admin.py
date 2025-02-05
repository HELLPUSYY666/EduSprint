from django.contrib import admin

from courses.models import Course, Lesson, Quiz


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'content', 'video_url')
    search_fields = ('course', 'title', 'content')


@admin.register(Quiz)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'question', 'answer')
    search_fields = ('lesson', 'question', 'answer')