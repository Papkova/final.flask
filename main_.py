from fastapi import FastAPI


app = FastAPI()

d_values = {"key": "values"}


@app.get("/get_method/{key}")
def get_method(key: str):
    value = d_values.get(key, "default_value")
    return {"values": value}


@app.post("/post_method/")
async def post_method(data: dict[str, str]):
    key = data.get("key")
    value = data.get("value")
    return {"key": key, "value": value}


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