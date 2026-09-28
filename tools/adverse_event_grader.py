"""
adverse_event_grader.py - Maps clinical toxicity and symptom reports to CTCAE v5.0 severity grades
"""
import sys
import json


def grade_adverse_event(event_description: str, toxicity_level: int = 1):
    desc = event_description.lower()
    if toxicity_level >= 4 or "life-threatening" in desc or "icu" in desc:
        grade = 4
        action = "URGENT_TRIAL_HOLD"
    elif toxicity_level == 3 or "severe" in desc or "hospitalization" in desc:
        grade = 3
        action = "DOSE_REDUCTION_REQUIRED"
    elif toxicity_level == 2 or "moderate" in desc:
        grade = 2
        action = "SUPPORTIVE_CARE_MONITORING"
    else:
        grade = 1
        action = "OBSERVE_CONTINUE"
    return {"grade": grade, "standard": "CTCAE_v5.0", "action": action, "status": "GRADED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "adverse-event-grader"}))
