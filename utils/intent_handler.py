# INTENT DETECTION MODULE
# This module detects high-level user intent based on selected skills
# and provides explanations if there's a mismatch with model predictions.

def detect_user_intent(level_map, selected_levels):
    """
    Detect high-level user intent based on selected skills.
    """

    intents = {
        "ml_track": (
            level_map[selected_levels["ml"]] > 0 or
            level_map[selected_levels["dl"]] > 0 or
            level_map[selected_levels["nlp"]] > 0
        ),

        "backend_track": (
            level_map[selected_levels["python"]] > 0 and
            level_map[selected_levels["sql"]] > 0
        ),

        "data_track": (
            level_map[selected_levels["sql"]] > 0 and
            level_map[selected_levels["statistics"]] > 0
        )
    }

    return intents


# INTENT vs MODEL OUTPUT EXPLAINER
# Intent detection is used to understand the user's high-level career interests (e.g., ML track, backend track).
# Model output is the final career recommendation from the trained model.
# Intent detection helps in providing more personalized guidance and roadmap suggestions.

def get_intent_message(predicted_role, intents):
    """
    Return explanation message if intent and prediction mismatch.
    """

    if predicted_role == "Backend Developer" and intents["ml_track"]:
        return (
            "You show interest in Machine Learning, but core prerequisites "
            "like Statistics and ML depth are currently weak. "
            "Strengthen them to move towards ML Engineer."
        )

    if predicted_role in ["Data Analyst", "Business Analyst"] and intents["backend_track"]:
        return (
            "You have backend development potential. "
            "With stronger programming and system design skills, "
            "you can move into Backend Developer roles."
        )

    if predicted_role == "Backend Developer" and intents["data_track"]:
        return (
            "You show interest in data-oriented roles. "
            "Improving Statistics and analytical thinking can help you "
            "transition towards Data Analyst or Data Scientist."
        )

    return None
