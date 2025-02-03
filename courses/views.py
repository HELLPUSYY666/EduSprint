from rest_framework.generics import ListAPIView
from django.shortcuts import render

from courses.models import Course, Lesson, Quiz
from courses.serializer import CourseSerializer, LessonSerializer, QuizSerializer


class CourseListView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.all()


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        return Lesson.objects.all()


class QuizListView(ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.all()
