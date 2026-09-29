# timetable_view.py - Terminal formatting and audit report rendering


def render_course_summary(selected_codes, catalog):
  """Prints a structured table of selected courses with their metadata."""
  print("\n" + "=" * 74)
  print(f"{'COURSE CODE':<14}{'COURSE TITLE':<38}{'CREDITS':<10}{'SLOTS'}")
  print("-" * 74)
  for code in selected_codes:
    course = catalog[code]
    slots_str = ", ".join(sorted(course["slots"]))
    print(
        f"{code:<14}{course['title']:<38}{course['credits']:<10}{slots_str}"
    )
  print("=" * 74)


def render_audit_report(
    total_credits, credit_status, conflicts, unmet_prereqs
):
  """Displays the registration audit outcome."""
  print("\n" + "#" * 22 + " REGISTRATION AUDIT " + "#" * 23)

  # Credit Limit Audit
  status_flag, status_msg = credit_status
  cred_tag = "[PASS]" if status_flag else "[FAIL]"
  print(f"\n{cred_tag} Credit Evaluation:")
  print(f"  - Total Enrolled Credits : {total_credits}")
  print(f"  - Limit Verification     : {status_msg}")

  # Slot Collision Audit
  clash_tag = "[FAIL]" if conflicts else "[PASS]"
  print(f"\n{clash_tag} Slot Collision Audit:")
  if conflicts:
    print("  * Identified slot clashes:")
    for c in conflicts:
      slots_str = ", ".join(c["conflicting_slots"])
      print(f"    - {c['course_1']} clashes with {c['course_2']} on {slots_str}")
  else:
    print("  * Clean schedule: No slot overlaps detected.")

  # Prerequisite Check
  prereq_tag = "[FAIL]" if unmet_prereqs else "[PASS]"
  print(f"\n{prereq_tag} Prerequisite Verification:")
  if unmet_prereqs:
    print("  * Deficit requirements:")
    for code, missing in unmet_prereqs.items():
      missing_str = ", ".join(missing)
      print(f"    - {code} requires: {missing_str}")
  else:
    print("  * All prerequisite conditions satisfied.")

  # Final Registration Decision
  print("\n" + "-" * 74)
  if status_flag and not conflicts and not unmet_prereqs:
    print(
        "RESULT: REGISTRATION CLEARED -> Schedule is ready for submission."
    )
  else:
    print(
        "RESULT: REGISTRATION BLOCKED -> Resolve listed flags to proceed."
    )
  print("-" * 74)