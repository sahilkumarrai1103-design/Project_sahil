# main.py - Interactive CLI driver for FFCS Course Slot Conflict & Credit Limit Auditor
import sys

from clash_detector import find_slot_conflicts
from course_catalog import COURSES, STUDENT_PROFILE
from credit_auditor import (
    calculate_total_credits,
    evaluate_credit_limits,
    verify_prerequisites,
)
from timetable_view import render_audit_report, render_course_summary
from validator import parse_course_selection


def display_catalog():
  print("\n" + "=" * 65)
  print(f"{'COURSE':<10}{'TITLE':<32}{'CR':<6}{'SLOTS':<12}{'PREREQS'}")
  print("-" * 65)
  for code, info in COURSES.items():
    slots = ", ".join(sorted(info["slots"]))
    prereqs = ", ".join(sorted(info["prereqs"])) if info["prereqs"] else "None"
    print(
        f"{code:<10}{info['title']:<32}{info['credits']:<6}{slots:<12}{prereqs}"
    )
  print("=" * 65)


def run_auditor():
  print("\n" + "*" * 65)
  print(" " * 12 + "FFCS COURSE REGISTRATION & AUDIT SYSTEM")
  print("*" * 65)
  print(f"Student Reg No       : {STUDENT_PROFILE['reg_no']}")
  print(
      "Completed Courses    :"
      f" {', '.join(sorted(STUDENT_PROFILE['completed_courses']))}"
  )
  print(
      f"Credit Boundaries    : Min {STUDENT_PROFILE['min_credits']} | Max"
      f" {STUDENT_PROFILE['max_credits']}"
  )

  display_catalog()

  print("\nEnter course codes separated by space (or type 'EXIT' to quit):")
  print("Example: CSE1021 MAT1011 PHY1001 ENG1001 HUM1021 CHY1001\n")

  user_input = input("Selected Courses > ").strip()

  if not user_input or user_input.upper() == "EXIT":
    print("Registration session cancelled.")
    sys.exit(0)

  valid_courses, duplicates, unknown = parse_course_selection(
      user_input, COURSES
  )

  if duplicates:
    print(f"\n[Notice] Ignored duplicate entries: {', '.join(duplicates)}")

  if unknown:
    print(
        f"[Warning] Unknown course codes omitted from audit: {', '.join(unknown)}"
    )

  if not valid_courses:
    print("\n[Error] No valid course codes were recognized. Aborting audit.")
    sys.exit(1)

  # Display enrolled course overview
  render_course_summary(valid_courses, COURSES)

  # Run core audit checks
  total_credits = calculate_total_credits(valid_courses, COURSES)
  credit_status = evaluate_credit_limits(
      total_credits,
      min_limit=STUDENT_PROFILE["min_credits"],
      max_limit=STUDENT_PROFILE["max_credits"],
  )
  conflicts = find_slot_conflicts(valid_courses, COURSES)
  unmet_prereqs = verify_prerequisites(
      valid_courses, COURSES, STUDENT_PROFILE["completed_courses"]
  )

  # Render comprehensive audit report
  render_audit_report(total_credits, credit_status, conflicts, unmet_prereqs)


if __name__ == "__main__":
  run_auditor()