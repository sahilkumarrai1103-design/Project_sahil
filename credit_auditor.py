# credit_auditor.py - Credit boundaries and prerequisite verification


def calculate_total_credits(selected_codes, catalog):
  """Calculates the sum of credits for all selected course codes."""
  return sum(
      catalog[code]["credits"] for code in selected_codes if code in catalog
  )


def evaluate_credit_limits(total_credits, min_limit=16, max_limit=27):
  """Evaluates whether the total credits fall within the allowed window."""
  if total_credits < min_limit:
    deficit = min_limit - total_credits
    return (
        False,
        f"Under-credited: Needs {deficit} more credit(s) to meet minimum"
        f" {min_limit}.",
    )
  if total_credits > max_limit:
    excess = total_credits - max_limit
    return (
        False,
        f"Over-credited: Exceeds maximum limit of {max_limit} by {excess}"
        " credit(s).",
    )
  return True, f"Within permissible credit limits ({min_limit} - {max_limit})."


def verify_prerequisites(selected_codes, catalog, completed_courses):
  """Checks if the student meets all prerequisite requirements for chosen courses.

  Uses set difference: (prereqs - completed_courses).
  """
  unmet = {}
  for code in selected_codes:
    course = catalog.get(code, {})
    prereqs = course.get("prereqs", set())
    missing = prereqs - completed_courses
    if missing:
      unmet[code] = sorted(missing)
  return unmet