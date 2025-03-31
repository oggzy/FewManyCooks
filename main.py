from fastapi import FastAPI

app = FastAPI()

recipes = "www.themealdb.com/api/json/v1/1/search.php?s="

nutrition = "https://ancient-lowlands-31543.herokuapp.com/api/json/v0.1/seach?name="

@app.get("/")
def root():
    return {"message":"This is FewManyCooks"}

