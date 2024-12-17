from django.contrib import admin
from .models import( 
    Category, Customer, Product, Order, Course, Lesson, Page, Quiz, Question, Answer,
    Test, TestQuestion, TestAnswer
    )

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class TestQuestionInline(admin.TabularInline):
    model = TestQuestion
    extra = 1


class TestAnswerInline(admin.TabularInline):
    model = TestAnswer
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'lesson']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['text', 'quiz']


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    inlines = [TestQuestionInline]
    list_display = ['title', 'course']


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    inlines = [TestAnswerInline]
    list_display = ['text', 'test']