from fastapi import FastAPI
import uvicorn

app = FastAPI()



# @app.get('/{name}')
# def user(name: str):
#     return name
@app.get('/')
def user():
    return "name"


if __name__=="__main__":
    uvicorn.run("main:app",reload=True)