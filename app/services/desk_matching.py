from typing import List, Dict, Any
from app.db.models import Desk, Employee, OccupancyData

def match_desks(user_preferences: Dict[str, Any], occupancy_data: List[OccupancyData], desks: List[Desk]) -> List[Desk]:
    suitable_desks = []

    for desk in desks:
        if is_desk_suitable(desk, user_preferences, occupancy_data):
            suitable_desks.append(desk)

    return suitable_desks

def is_desk_suitable(desk: Desk, user_preferences: Dict[str, Any], occupancy_data: List[OccupancyData]) -> bool:
    if desk.is_occupied(occupancy_data):
        return False

    if user_preferences.get("location") and desk.location != user_preferences["location"]:
        return False

    if user_preferences.get("features"):
        for feature in user_preferences["features"]:
            if feature not in desk.features:
                return False

    return True

def rank_desks(suitable_desks: List[Desk], user_preferences: Dict[str, Any]) -> List[Desk]:
    ranked_desks = sorted(suitable_desks, key=lambda desk: calculate_rank(desk, user_preferences))
    return ranked_desks

def calculate_rank(desk: Desk, user_preferences: Dict[str, Any]) -> int:
    rank = 0

    if desk.location == user_preferences.get("location"):
        rank += 10

    for feature in user_preferences.get("features", []):
        if feature in desk.features:
            rank += 5

    return rank