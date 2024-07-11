from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe_view(request, dish_name):
    recipe = DATA.get(dish_name)
    if not recipe:
        raise Http404("Рецепт не найден")

    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError
    except ValueError:
        raise Http404("Invalid number of servings")

    scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe': scaled_recipe
    }

    return render(request, 'calculator/index.html', context)







# def pasta(request)
#
#
# def buter(request)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
