# import uvicorn
# from starlette.middleware.cors import CORSMiddleware
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# # 请求主体类
# class Item(BaseModel):
#     name: str = "武汉加油 ！！"
#     description: str = None
#     price: float = 233
#     tax: float = None
#
#
# app = FastAPI()
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return item


from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") # 挂载静态文件，指定目录


templates = Jinja2Templates(directory="templates") # 模板目录


@app.get("/data/{data}")
async def read_data(request: Request, data: str):
    return templates.TemplateResponse("index.html", {"request": request, "data": data})


if __name__ == "__main__":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    uvicorn.run(app, host="localhost", port=8000, reload=False)

