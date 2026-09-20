from fastapi import FastAPI

from controllers.tools_controller import router as tools_router

app = FastAPI(
    title="Tools Inquiry API",
    version="1.0.0",
)

app.include_router(tools_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "ok"}



