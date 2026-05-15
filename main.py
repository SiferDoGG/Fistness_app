from fastapi import FastAPI
import uvicorn
from routers import router

app = FastAPI(
    title="Workout Tracker API",
    description="Бэкенд для трекера тренировок.",
    version="1.0.0",
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
