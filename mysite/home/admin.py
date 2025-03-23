from django.contrib import admin
import nested_admin
from .models import (
    Category, Customer, Product, Order, Lesson, Page, Paragraph, Video, Quiz, Question, Answer,
    Test, TestQuestion, TestAnswer
)

# Registering simple models directly
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)

# Nested admin inlines
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

class ParagraphInline(nested_admin.NestedStackedInline):  
    model = Paragraph
    extra = 1

class VideoInline(nested_admin.NestedStackedInline):  
    model = Video
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

@admin.register(Lesson)
class LessonAdmin(nested_admin.NestedModelAdmin):
    list_display = ['title', 'course', 'order']
    inlines = [PageInline, QuizInline]

@admin.register(Page)
class PageAdmin(nested_admin.NestedModelAdmin):
    list_display = ['title']
    inlines = [ParagraphInline, VideoInline]

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