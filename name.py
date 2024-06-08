#Приклад Валідації
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError, field_validator
from typing import Any
from fastapi.responses import JSONResponse

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float

    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, value: Any):
        if value <= 0:
            raise ValueError("Ціна повинна бути більшою за нуль")
        return value


@app.post("/items/")
def create_item(item: Item):
    try:
        return JSONResponse(status_code=201, content=item.dict())
    except ValidationError as exc:
        errors = exc.errors()
        for error in errors:
            if error['type'] == 'value_error':
                error['msg'] = "Check your datas on validation"
        raise HTTPException(status_code=422, detail=errors)
