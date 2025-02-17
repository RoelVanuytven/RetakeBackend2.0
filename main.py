from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
from routes import rv_endpoints

app = FastAPI(docs_url=config.documentation_url)

# Alle endpoints worden nu toegevoegd met .app
app.include_router(router=rv_endpoints.app)

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
