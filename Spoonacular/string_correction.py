import json
import ast
import enchant
from api_call import spoonacular_api_call

token = "YHvCM9V4j6mshPALYJaOfAvCgZJWp1jiSoOjsn93w0PY8v7ibw"
ingredients = raw_input("Ingredient: ")

def correct_string (ingredients):
    diccionary = enchant.Dict('en_US')


    correct_word = diccionary.check(ingredients)

    if correct_word == True :
            #print 'The ingredient {} is ready to ask for a recipe'.format(ingredients)
        return 
    
    else :
            #print 'We could not find {} as an ingredient in our list. Wait... \n'.format(ingredients)
        #Autocomplete ingredient search
            
        url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/food/ingredients/autocomplete?"
        parameters = {
                    'query':ingredients
                    }
        ingredient_correct = spoonacular_api_call('Get', url, token, parameters)
        ingredient_correct_json = str(ingredient_correct.json())

        ingredient_name = ingredient_correct_json[1:-1]
        ingredient_dicctionari = ast.literal_eval(ingredient_name)
        ingredient_final = ingredient_dicctionari[0]["name"]

        # print 'Do you mean {} ?'.format(ingredient_final)
        # ingredients_correction = raw_input("[Y/N] ")


        # if ingredients_correction == 'Y' :
        #     print 'The ingredient {} is ready to ask for a recipe'.format(ingredient_final)
        # else :
        #     print 'We cound not find any similar ingredient.'

        
        
        
        return ingredient_final

