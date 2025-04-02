import requests
import json
from pprint import pprint


recipes_url = "https://www.themealdb.com/api/json/v1/1/search.php?s="

def strip_ingredients(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        ingredients_json = json.load(f)
        ingredients = ingredients_json["FoundationFoods"]
        
    stripped_ingredients = { ingredient["description"] : 
                            {"portions": 
                            {portion["measureUnit"]["name"]: portion["gramWeight"] for portion in ingredient["foodPortions"]},
                            "nutrients" : 
                            {nutrient["nutrient"]["name"]: [nutrient["amount"],nutrient["nutrient"]["unitName"]] for nutrient in ingredient["foodNutrients"] if "amount" in nutrient.keys()}}
                            for ingredient in ingredients }
   
    return stripped_ingredients
    
        
def get_recipe(recipe):
    recipe_json = requests.get(recipes_url+recipe)
    recipe_dict = json.loads(recipe_json.content)["meals"][0]
    return recipe_dict
