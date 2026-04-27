from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/auth/signup", tags=["auth"])
async def signup():
    pass


@app.post("/auth/login", tags=["auth"])
async def login():
    pass


@app.post("/auth/logout", tags=["auth"])
async def logout():
    pass


@app.get("/users/me", tags=["users"])
async def get_current_user():
    pass


@app.get("/exercises", tags=["exercises"])
async def get_exercises():
    pass


@app.post("/exercises", tags=["exercises"])
async def create_exercise():
    pass


@app.get("/exercises/{id}", tags=["exercises"])
async def get_exercise(id: int):
    pass


@app.get("/workouts", tags=["workouts"])
async def get_workouts():
    pass


@app.post("/workouts", tags=["workouts"])
async def create_workout():
    pass


@app.get("/workouts/{id}", tags=["workouts"])
async def get_workout(id: int):
    pass


@app.patch("/workouts/{id}", tags=["workouts"])
async def update_workout(id: int):
    pass


@app.delete("/workouts/{id}", tags=["workouts"])
async def delete_workout(id: int):
    pass


@app.get("/reports/summary", tags=["reports"])
async def get_summary_report():
    pass


@app.get("/reports/progress", tags=["reports"])
async def get_progress_report():
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
