from forum.models import Category


def category_processor(request):
    return {"categories" : Category.objects.all()}