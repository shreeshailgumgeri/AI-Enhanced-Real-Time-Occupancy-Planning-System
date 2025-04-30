def validate_api_key(api_key):
    if not api_key or len(api_key) != 32:  # Example length for an API key
        raise ValueError("Invalid API key provided.")
    return True

def format_desk_response(desk):
    return {
        "id": desk.id,
        "location": desk.location,
        "features": desk.features,
        "is_available": desk.is_available
    }

def parse_employee_preferences(preference_string):
    preferences = preference_string.split(',')
    return [pref.strip() for pref in preferences if pref.strip()]