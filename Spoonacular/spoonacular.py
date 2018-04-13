import requests
import json
import ast
from api_call import spoonacular_api_call

def spoonacular_recipe(ingredient_list, num_recipes):
    #ingredient_list =ingredients.split(', ')
    ingredient = '%2C'.join(ingredient_list)
    url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?"
    parameters = {'ingredients': ingredient,
                'fillIngredients': 'false',
                'limitLicense': 'false',
                'number': int(num_recipes),
                #'ranking':1
                }

    recipe = spoonacular_api_call('GET', url, parameters)
    recipe_json = str(recipe.json())
    recipe_detail = recipe_json[1:-1]
    recipe_dicctionari = ast.literal_eval(recipe_detail)

    # recipe_id = recipe_dicctionari[0]["id"]
    recipe_title = recipe_dicctionari [0]["title"]
    print 'La primera recepte diu: '
    print recipe_title

    # recipe_id2 = recipe_dicctionari[1]["id"]
    recipe_title2 = recipe_dicctionari[1]["title"]
    print 'La segona recepte es: '
    print recipe_title2
    # recipe_title = recipe_dicctionari["title"]
    # recipe_url_image = recipe_dicctionari["image"]
    # recipe_usedIngredientCount = recipe_dicctionari["usedIngredientCount"]
    # recipe_missedIngredientCount = recipe_dicctionari["missedIngredientCount"]
    # recipe_likes = recipe_dicctionari["likes"]


    # print 'Recipe information: \n'
    # print '* The recipe id is: {}'.format(recipe_id) 
    # print '* The recipe title is: {}'.format(recipe_title)
    # print '* The recipe image link is: {}'.format(recipe_url_image)
    # print '* The number of ingredient asked that uses this recipe is: {}'.format(recipe_usedIngredientCount)
    # print '* The number of ingredient that missed this recipe is: {}'.format(recipe_missedIngredientCount)
    # print '* The number of people who likes this recipe is: {}'.format(recipe_likes)

    return recipe_dicctionari