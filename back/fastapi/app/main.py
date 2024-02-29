import uvicorn


from fastapi import FastAPI
from routers.sii import router as sii_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sii_router, prefix="/sii", tags=["sii"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)