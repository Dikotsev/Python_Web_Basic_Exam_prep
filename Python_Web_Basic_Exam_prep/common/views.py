from django.shortcuts import render, redirect


# Create your views here.

from Python_Web_Basic_Exam_prep.common.core.create_recipe import get_recipe
from Python_Web_Basic_Exam_prep.common.forms import EditRecipeForm, CreateRecipeForm, DeleteRecipeForm
from Python_Web_Basic_Exam_prep.common.models import Recipe


def home(request):
    recipe = get_recipe()
    if not recipe:
        return redirect('create recipe')
    recipe = Recipe.objects.all

    context = {
          'recipe': recipe
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateRecipeForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditRecipeForm(instance=recipe)

    context = {
        'form': form
    }
    return render(request, 'edit.html', context)



def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe.delete()
        form = DeleteRecipeForm(request.POST, instance=recipe)

    else:
        form = DeleteRecipeForm(instance=recipe)

    context = {
        'form': form
    }
    return render(request, 'delete.html', context)


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if not recipe:
        return redirect('home')
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe,
    }
    return render(request, 'details.html', context)
