from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
import nested_admin

from .models import (
    Category, Customer, Product, Order, Lesson, Page, Paragraph, Video, Quiz,
    Question, Answer, Test, TestQuestion, TestAnswer, Profile, Enrollment
)

# Registering simple models directly
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)

# ======================
# Profile Inline for User
# ======================
class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1
    fields = ('course', 'progress', 'quiz_score', 'test_score', 'overall_score', 'completed', 'badge', 'certificate_url')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    inlines = [EnrollmentInline]

# Unregister original User admin and re-register with Profile inline
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [EnrollmentInline]
    list_display = ('user',)


admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

# ======================
# Product Admin
# ======================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

# ======================
# Lesson Admin with nested content
# ======================
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

@admin.register(Lesson)
class LessonAdmin(nested_admin.NestedModelAdmin):
    list_display = ['title', 'course', 'order']
    inlines = [PageInline, QuizInline]

@admin.register(Page)
class PageAdmin(nested_admin.NestedModelAdmin):
    list_display = ['title']
    inlines = [ParagraphInline, VideoInline]

# ======================
# Test Admin
# ======================
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
