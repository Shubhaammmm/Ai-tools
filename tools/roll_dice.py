import random

def run(message, params):
    """
    Simulates rolling a dice with a specified number of sides.

    Args:
        message (str): Message or additional query input (not used in this tool).
        params (dict): Parameters including:
            - sides (int): The number of sides of the dice.

    Returns:
        dict: Result of the dice roll.
    """
    try:
        sides = params.get("sides", 6)  # Default to 6 sides if not specified
        result = random.randint(1, sides)
        return {"status": "success", "message": f"Rolled a {result} on a {sides}-sided dice."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

