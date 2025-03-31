from calc import calculate as calc

def test_calculate_returns_dict():
    test_out = calc("Arrabiata")
    print(test_out)
    assert type(test_out) == dict
    assert test_out["meals"][0]["strMeal"] == "Spicy Arrabiata Penne"
