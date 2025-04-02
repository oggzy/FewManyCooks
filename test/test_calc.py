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

def test_strip_ingredients_contains_only_necessary_data():
    test_out = strip_ingredients('test/test_json.json')
    test_data = {"food" : {"portions":{"portion":"test"},"nutrients" : {"nutrient" : ["amount","unit"]}}}
    for out_l1 in test_out.values():
        assert type(out_l1) == type(test_data["food"])
        assert len(out_l1) == len(test_data["food"])
        for out_l2 in out_l1:
            assert out_l2 in test_data["food"].keys()
            if out_l2 == "portions":
                assert type(out_l1[out_l2]) ==  dict
            elif out_l2 == "nutrients":
                for out_l3 in out_l1[out_l2].values():
                    assert type(out_l3) ==  list
                    assert len(out_l3) == 2
            else:
                assert False
