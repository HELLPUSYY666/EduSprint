from django import forms
from .models import Course, Lesson, Quiz


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'video_url', 'content']


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['lesson', 'question', 'answer']
