from food_data import get_recipe, strip_ingredients

def test_get_recipe_returns_dict():
    test_out = get_recipe("Arrabiata")
    assert type(test_out) == dict
    assert test_out["strMeal"] == "Spicy Arrabiata Penne"

def test_strip_ingredients_reads_file():
    test_out = strip_ingredients('test/test_json.json')
    assert type(test_out) == dict
    test_data = {"Hummus, commercial": "test","Tomatoes, grape, raw": "test"}
    assert test_out.keys() == test_data.keys()
