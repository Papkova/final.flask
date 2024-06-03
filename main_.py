from fastapi import FastAPI


app = FastAPI()

d_values = {"key": "values"}


@app.get("/")
async def hello():
    return {"value": d_values}


@app.post('/add')
async def add_to_post(key: str, value: str):
    d_values[key] = value
    return {'message': 'Елемент успішно додано до словника'}


@app.put("/change_dict/{key3}/{value1}")
def test(key: str, value: str):
    if key in d_values:
        d_values[key] = value
        return d_values
    else:
        return {"message": "Key not found"}


@app.delete("/delete/{key}")
def delete_item(key: str):
    if key in d_values:
        del d_values[key]
        return {"message": "Item deleted successfully"}
    else:
        return {"message": "Key not found"}