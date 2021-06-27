from Python_Web_Basic_Exam_prep.common.models import Recipe


def get_recipe():
    recipe = Recipe.objects.all
    return recipe