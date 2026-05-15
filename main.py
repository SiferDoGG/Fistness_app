from fastapi import FastAPI
import uvicorn
from routers import auth, users, exercises, workouts, reports

app = FastAPI(
    title="Workout Tracker API",
    description="Бэкенд для трекера тренировок.",
    version="1.0.0",
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(exercises.router)
app.include_router(workouts.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
