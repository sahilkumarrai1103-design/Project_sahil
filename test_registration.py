# test_registration.py - Automated unit tests for registration audit logic
import unittest

from clash_detector import find_slot_conflicts
from credit_auditor import (
    calculate_total_credits,
    evaluate_credit_limits,
    verify_prerequisites,
)
from validator import parse_course_selection


class TestFFCSAuditor(unittest.TestCase):

  def setUp(self):
    self.test_catalog = {
        "CSE1021": {
            "title": "Python Essentials",
            "credits": 4,
            "slots": {"A1", "TA1"},
            "prereqs": set(),
        },
        "CSE2001": {
            "title": "Data Structures",
            "credits": 4,
            "slots": {"A1", "TA1"},
            "prereqs": {"CSE1021"},
        },
        "MAT1011": {
            "title": "Calculus",
            "credits": 4,
            "slots": {"B1", "TB1"},
            "prereqs": set(),
        },
        "ENG1001": {
            "title": "Technical English",
            "credits": 2,
            "slots": {"D1"},
            "prereqs": set(),
        },
    }

  def test_slot_conflict_detection(self):
    # CSE1021 and CSE2001 share A1, TA1 -> should flag conflict
    conflicts = find_slot_conflicts(
        ["CSE1021", "CSE2001"], self.test_catalog
    )
    self.assertEqual(len(conflicts), 1)
    self.assertEqual(conflicts[0]["conflicting_slots"], ["A1", "TA1"])

    # CSE1021 and MAT1011 have non-overlapping slots -> clean
    no_conflict = find_slot_conflicts(
        ["CSE1021", "MAT1011"], self.test_catalog
    )
    self.assertEqual(len(no_conflict), 0)

  def test_credit_limit_boundaries(self):
    # Under-credit condition (< 16 credits)
    valid_low, msg_low = evaluate_credit_limits(10, min_limit=16, max_limit=27)
    self.assertFalse(valid_low)
    self.assertIn("Under-credited", msg_low)

    # Valid credit window (16 to 27 credits)
    valid_mid, _ = evaluate_credit_limits(20, min_limit=16, max_limit=27)
    self.assertTrue(valid_mid)

    # Over-credit condition (> 27 credits)
    valid_high, msg_high = evaluate_credit_limits(
        28, min_limit=16, max_limit=27
    )
    self.assertFalse(valid_high)
    self.assertIn("Over-credited", msg_high)

  def test_prerequisite_verification(self):
    completed = {"CSE1001"}
    # CSE2001 requires CSE1021 which is missing
    unmet = verify_prerequisites(["CSE2001"], self.test_catalog, completed)
    self.assertIn("CSE2001", unmet)
    self.assertEqual(unmet["CSE2001"], ["CSE1021"])

    # When prerequisite is already satisfied
    completed_with_prereq = {"CSE1001", "CSE1021"}
    cleared = verify_prerequisites(
        ["CSE2001"], self.test_catalog, completed_with_prereq
    )
    self.assertEqual(len(cleared), 0)

  def test_input_sanitization_and_parsing(self):
    raw_input = "cse1021 MAT1011 cse1021 INVALID999"
    valid, duplicates, unknown = parse_course_selection(
        raw_input, self.test_catalog
    )
    self.assertEqual(valid, ["CSE1021", "MAT1011"])
    self.assertEqual(duplicates, ["CSE1021"])
    self.assertEqual(unknown, ["INVALID999"])


if __name__ == "__main__":
  unittest.main()