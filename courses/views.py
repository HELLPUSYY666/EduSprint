from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .forms import CourseForm, LessonForm, QuizForm
from courses.models import Course, Lesson, Quiz
from courses.serializer import CourseSerializer, LessonSerializer, QuizSerializer
from rest_framework.generics import ListAPIView


class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = '/'


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = '/'


class CourseDeleteView(DeleteView):
    model = Course
    success_url = '/'
    template_name = 'courses/course_del.html'


class LessonListView(ListView):
    model = Lesson
    template_name = 'courses/lesson_list.html'
    context_object_name = 'lessons'


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'courses/lesson_detail.html'
    context_object_name = 'lesson'


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'courses/lesson_form.html'
    success_url = '/'


class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'courses/lesson_form.html'
    success_url = '/'


class QuizListView(ListView):
    model = Quiz
    template_name = 'courses/quiz_list.html'
    context_object_name = 'quizzes'


class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'courses/quiz_detail.html'
    context_object_name = 'quiz'


class QuizCreateView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'courses/quiz_form.html'
    success_url = '/'


class QuizUpdateView(UpdateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'courses/quiz_form.html'
    success_url = '/'
