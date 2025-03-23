from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
import datetime

# Categories of classes
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default="", blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return f"Order: {self.quantity} x {self.product.name} by {self.customer.first_name}"


class Lesson(models.Model):
    course = models.ForeignKey(Product, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    preview_text = models.CharField(max_length=500)
    video = models.FileField(blank=True, upload_to='videos/')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.course.name}"

#Page Models

class Page(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    page_number = models.IntegerField(default=1)

    def __str__(self):
        return f"Page {self.page_number}: {self.title} - {self.lesson.title}"
    
class Paragraph(models.Model):
    page = models.ForeignKey(Page, related_name="paragraphs", on_delete=models.CASCADE)
    header = models.CharField(max_length=225, blank=True, null=True)
    content = RichTextField()

    def __str__(self):
        return self.header if self.header else f"Paragraph {self.id}"
    
class Video(models.Model):
    page = models.ForeignKey(Page, related_name="videos", on_delete=models.CASCADE)
    title = models.CharField(max_length=225, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True) 
    uploaded_video = models.FileField(upload_to="videos/", blank=True, null=True)

    def __str__(self):
        return self.title if self.title else f"Video {self.id}"
    
# End of page realated or inline models


# Quiz and Test Models
class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='quizzes', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Quiz: {self.title} - {self.lesson.title}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return f"Question: {self.text}"


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer: {self.text} (Correct: {self.is_correct})"


class Test(models.Model):
    course = models.ForeignKey(Product, related_name='tests', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Test: {self.title} - {self.course.name}"


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, related_name='test_questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return f"Test Question: {self.text}"


class TestAnswer(models.Model):
    test_question = models.ForeignKey(TestQuestion, related_name='test_answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Test Answer: {self.text} (Correct: {self.is_correct})"