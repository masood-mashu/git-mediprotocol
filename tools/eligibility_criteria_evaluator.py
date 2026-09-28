"""
eligibility_criteria_evaluator.py - Evaluates patient laboratory biomarker values against inclusion and exclusion criteria
"""
import sys
import json


def evaluate_eligibility(patient_data_json: str):
    import json
    data = json.loads(patient_data_json) if isinstance(patient_data_json, str) else patient_data_json
    age = data.get("age", 0)
    egfr = data.get("egfr", 0.0)
    platelets = data.get("platelets", 0)
    anc = data.get("anc", 0)
    
    passed_age = 18 <= age <= 75
    passed_egfr = egfr >= 60.0
    passed_platelets = platelets >= 100000
    passed_anc = anc >= 1500
    
    all_passed = passed_age and passed_egfr and passed_platelets and passed_anc
    return {
        "eligible": all_passed,
        "criteria": {
            "age_check": passed_age,
            "egfr_check": passed_egfr,
            "platelets_check": passed_platelets,
            "anc_check": passed_anc
        },
        "status": "APPROVED" if all_passed else "INELIGIBLE"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "eligibility-criteria-evaluator"}))
