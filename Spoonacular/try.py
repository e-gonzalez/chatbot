
from spoonacular import spoonacular_recipe

ingredient_list = ['egg', 'potato']
num_recipes = 2


holis = spoonacular_recipe(ingredient_list, num_recipes)

print 'Receptes finals sera:'
print holis[0]
print '\n'

print holis[1]