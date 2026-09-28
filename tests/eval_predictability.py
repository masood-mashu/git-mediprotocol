"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitMediProtocol.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.eligibility_criteria_evaluator import *
from tools.adverse_event_grader import *
from tools.protocol_visit_window_auditor import *

class TestGitMediProtocolPredictability(unittest.TestCase):

    def test_eligibility_criteria_evaluator(self):
        data = '{"age": 45, "egfr": 75.0, "platelets": 150000, "anc": 2000}'
        res = evaluate_eligibility(data)
        self.assertTrue(res["eligible"])
        self.assertEqual(res["status"], "APPROVED")

    def test_adverse_event_grader(self):
        res = grade_adverse_event("severe febrile neutropenia", toxicity_level=3)
        self.assertEqual(res["grade"], 3)
        self.assertEqual(res["action"], "DOSE_REDUCTION_REQUIRED")

    def test_protocol_visit_window_auditor(self):
        res = audit_visit_window(2, allowable_window=3)
        self.assertTrue(res["compliant"])
        self.assertEqual(res["status"], "PROTOCOL_COMPLIANT")


if __name__ == "__main__":
    unittest.main()
