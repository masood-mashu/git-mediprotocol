"""
protocol_visit_window_auditor.py - Audits patient visit completion dates against scheduled trial protocol windows
"""
import sys
import json


def audit_visit_window(visit_offset_days: int, allowable_window: int = 3):
    in_window = abs(visit_offset_days) <= allowable_window
    return {
        "offset_days": visit_offset_days,
        "allowable_window": allowable_window,
        "compliant": in_window,
        "deviation_flag": not in_window,
        "status": "PROTOCOL_COMPLIANT" if in_window else "PROTOCOL_DEVIATION"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "protocol-visit-window-auditor"}))
