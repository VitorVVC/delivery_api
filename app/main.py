from fastapi import FastAPI

from api.routes.restaurants import router as restaurants_router

app = FastAPI(
    title="Delivery API",
    description="API educacional de uma plataforma de delivery.",
    version="0.1.0",
)

app.include_router(restaurants_router)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}