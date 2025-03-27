from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials = True,
    allow_methods = ['GET'],
    allow_headers = ['*']
)

@app.get('/')
async def root():
    return {'message': 'Hello World! This is from the first api I built! And thanks for visiting my website!'}

