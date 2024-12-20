from django.contrib import admin
import nested_admin
from .models import (
    Category, Customer, Product, Order, Course, Lesson, Page, Quiz, Question, Answer,
    Test, TestQuestion, TestAnswer
)

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)

class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer
    extra = 1

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    inlines = [AnswerInline]
    extra = 1

class QuizInline(nested_admin.NestedStackedInline):
    model = Quiz
    inlines = [QuestionInline]
    extra = 1

class PageInline(nested_admin.NestedStackedInline):
    model = Page
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

@admin.register(Lesson)
class LessonAdmin(nested_admin.NestedModelAdmin):
    list_display = ['title', 'course', 'order']
    inlines = [PageInline, QuizInline]

class TestQuestionInline(admin.TabularInline):
    model = TestQuestion
    extra = 1

class TestAnswerInline(admin.TabularInline):
    model = TestAnswer
    extra = 1

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    inlines = [TestQuestionInline]
    list_display = ['title', 'course']

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    inlines = [TestAnswerInline]
    list_display = ['text', 'test']