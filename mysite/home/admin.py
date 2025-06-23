from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
import nested_admin

from .models import (
    Category, Customer, Product, Order, Lesson, Page, Paragraph, Video, Quiz,
    Question, Answer, Test, TestQuestion, TestAnswer, Profile, Enrollment, ContentCount,
    UserProgress, QuizSubmission, TestSubmission
)

# ========== Register Basic Models ==========
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)

# ========== Inlines ==========

class UserProgressInline(nested_admin.NestedTabularInline):
    model = UserProgress
    extra = 0
    fields = ("content", "completed")
    readonly_fields = ("completed_at",)
    show_change_link = True

class EnrollmentInline(nested_admin.NestedStackedInline):
    model = Enrollment
    extra = 0
    fields = (
        'course', 'progress', 'quiz_score', 'test_score',
        'overall_score', 'completed', 'badge', 'certificate_url'
    )
    inlines = [UserProgressInline]

class QuizSubmissionInline(admin.TabularInline):
    model = QuizSubmission
    extra = 0
    fields = ("content", "score", "submitted_time")
    readonly_fields = ("submitted_time",)
    show_change_link = True

class TestSubmissionInline(admin.TabularInline):
    model = TestSubmission
    extra = 0
    fields = ("content", "score", "submitted_time")
    readonly_fields = ("submitted_time",)
    show_change_link = True

# ========== Profile Admin ==========
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [EnrollmentInline, QuizSubmissionInline, TestSubmissionInline]
    list_display = ('user',)

# ========== Unregister & Re-register User with Profile ==========
admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

# ========== Product Admin ==========
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    search_fields = ['name']  # required for autocomplete_fields to work

# ========== Lesson Admin ==========
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

# ========== Test Admin ==========
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
