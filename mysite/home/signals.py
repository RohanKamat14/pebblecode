from.models import Page, Quiz, Test, ContentCount
from django.dispatch import receiver
from django.db.models.signals import post_save

def create_contentcount_instance(instance, content_type:str):
    if instance.content is not None:
        return
    
    if content_type == "quiz":
        course = instance.lesson.course
        title = instance.title
    elif content_type == "test":
        course = instance.lesson.course
        title = instance.title
    elif content_type == "page":
        course = instance.lesson.course
        title = instance.title
        #when we figoure out how we want videos to be used
    #elif content_type == "video":
       # course = instance.lesson.course
        #title = instance.title
    else:
        raise ValueError("Invaild content type")

    last_order = ContentCount.objects.filter(course=course).order_by('-order').first()
    next_order = last_order.order + 1 if last_order else 1

    content = ContentCount.objects.create(
        course=course,
        title=instance.title,
        content_type=content_type,
        order = next_order,

    )

    instance.content = content
    instance.save(update_fields=["content"])



# todo make it so that pages and videos cand work in the function then make a receiver function

@receiver(post_save, sender=Test)
def create_content_for_test(sender, instance, created, **kwargs):
    if created:
        create_contentcount_instance(instance, 'test')

@receiver(post_save, sender=Quiz)
def create_content_for_quiz(sender, instance, created, **kwargs):
    if created:
        create_contentcount_instance(instance, 'quiz')

@receiver(post_save,sender=Page)
def create_content_for_page(sender, instance, created, **kwargs):
    if created:
        create_contentcount_instance(instance, 'page')        
