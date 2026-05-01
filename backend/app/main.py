from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, profile, ai, billing

app = FastAPI(title="AI Продюсер", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(profile.router, prefix="/api/profile", tags=["profile"])
app.include_router(ai.router, prefix="/api/ai", tags=["ai"])
app.include_router(billing.router, prefix="/api/billing", tags=["billing"])


@app.get("/health")
async def health():
    return {"status": "ok"}
