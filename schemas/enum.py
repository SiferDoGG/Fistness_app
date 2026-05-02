import enum


class WorkoutStatus(str, enum.Enum):
    scheduled = "scheduled"
    completed = "completed"
    missed = "missed"
