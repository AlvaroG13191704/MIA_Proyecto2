# API imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# local imports
from app.routes import routeHT4

# fastapi
app = FastAPI ()

origins=[
  "http://localhost:5173",
  "http://localhost:5173/",
  # add the domain of your frontend app here
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


# Routes
app.include_router(routeHT4.router)