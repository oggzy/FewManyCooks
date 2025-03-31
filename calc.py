import requests
import json

recipes = "https://www.themealdb.com/api/json/v1/1/search.php?s="

nutrition = "https://ancient-lowlands-31543.herokuapp.com/api/json/v0.1/seach?name="

def calculate(recipe):
    recipe_json = requests.get(recipes+recipe)
    recipe_json.content
    recipe_dict = json.loads(recipe_json.content)
    return recipe_dict