def safety_decision(intent: str) -> bool:
    """
    Returns True if request is allowed to proceed,
    False if it must be blocked.
    """
    if intent == "QUERY":
        return True

    if intent == "TASK":
        # Allowed to respond, not execute
        return True

    # SYSTEM_ACTION and REJECT are blocked
    return False
