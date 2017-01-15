#! python3
# grocery-planner - generate a grocery list for a week & text it to myself

from textMe import textme
import random

recipes = {}
groceries = {}
plan = ""

# read recipes.txt to fill recipes
with open('recipes.txt','r') as recipeFile:
    recipeList = recipeFile.read().splitlines()
    for recipe in recipeList:
        rString = recipe.split(':')
        name = rString[0]
        ingredients = rString[1].split(',')
        recipes[name] = ingredients

# generate list of groceries by randomly picking a recipe
recipeNames = list(recipes.keys())
for i in range(1,8):
    recipe = random.choice(recipeNames)
    plan += "Day " + str(i) + ": " + recipe + "\n"
    ingrs = recipes[recipe]
    for ingr in ingrs:
        try:
            groceries[ingr] += 1
        except KeyError:
            groceries[ingr] = 1

msg = ""
for ingr in list(groceries.keys()):
    msg += str(groceries[ingr]) + " " + ingr + "\n"

textme(plan)
textme(msg)    
