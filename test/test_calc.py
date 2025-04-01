from calc import get_recipe, strip_ingredients

def test_get_recipe_returns_dict():
    test_out = get_recipe("Arrabiata")
    assert type(test_out) == dict
    assert test_out["strMeal"] == "Spicy Arrabiata Penne"

def test_strip_ingredients():
    test_out = strip_ingredients('test_json.json')
    print(test_out)
    assert False
