from fastapi import FastAPI


app = FastAPI()


@app.get("/get_method/{param}")
def get_method(param: str):
    return {"param": param}


@app.get("/post_method/{param}")
def post_method(param: str):
    return {"param": param}




