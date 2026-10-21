"""PawPal+ core system: Owner, Pet, Task, and Organizer dataclasses."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, time
from typing import Optional


@dataclass
class Task:
    """A single pet care activity (walk, feeding, meds, grooming, etc.)."""

    title: str
    duration_minutes: int
    priority: str = "medium"  # "low" | "medium" | "high"
    category: str = "general"  # e.g. "walk", "feeding", "medical", "grooming"
    scheduled_time: Optional[time] = None  # preferred time of day, if any
    frequency: str = "daily"  # "once" | "daily" | "weekly"
    notes: str = ""
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as done."""
        raise NotImplementedError

    def priority_rank(self) -> int:
        """Return a numeric rank for sorting (higher = more important)."""
        raise NotImplementedError


@dataclass
class Pet:
    """A pet and the care tasks / health info tracked for it."""

    name: str
    species: str
    breed: str = ""
    age: int = 0
    medical_notes: list[str] = field(default_factory=list)
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Attach a care task to this pet."""
        raise NotImplementedError

    def remove_task(self, title: str) -> None:
        """Remove a task by title."""
        raise NotImplementedError

    def add_medical_note(self, note: str) -> None:
        """Record a health or medical note."""
        raise NotImplementedError

    def pending_tasks(self) -> list[Task]:
        """Return tasks that are not yet completed."""
        raise NotImplementedError


@dataclass
class Owner:
    """The pet owner, their pets, and their daily constraints."""

    name: str
    available_minutes: int = 120  # time the owner has for pet care per day
    preferences: dict[str, str] = field(default_factory=dict)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Register a new pet with this owner."""
        raise NotImplementedError

    def get_pet(self, name: str) -> Optional[Pet]:
        """Look up a pet by name."""
        raise NotImplementedError

    def all_tasks(self) -> list[tuple[Pet, Task]]:
        """Return every task across all pets, paired with its pet."""
        raise NotImplementedError


@dataclass
class Organizer:
    """Builds and explains a daily care plan for an owner's pets."""

    owner: Owner
    plan_date: date = field(default_factory=date.today)
    plan: list[tuple[Pet, Task]] = field(default_factory=list)
    skipped: list[tuple[Pet, Task]] = field(default_factory=list)

    def sort_tasks(self, tasks: list[tuple[Pet, Task]]) -> list[tuple[Pet, Task]]:
        """Order tasks by priority, then by scheduled time / duration."""
        raise NotImplementedError

    def generate_plan(self) -> list[tuple[Pet, Task]]:
        """Select tasks that fit the owner's available time and store the plan."""
        raise NotImplementedError

    def explain_plan(self) -> str:
        """Return a human-readable explanation of why tasks were chosen or skipped."""
        raise NotImplementedError

    def summary_by_pet(self) -> dict[str, list[Task]]:
        """Group today's planned tasks by pet name."""
        raise NotImplementedError
