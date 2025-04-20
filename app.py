from fastapi import FastAPI
from api.airquality import router

app = FastAPI()

app.include_router(router)
