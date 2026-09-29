# validator.py - Input parsing and course verification


def parse_course_selection(raw_input_string, available_catalog):
  """Parses a space-separated string of course codes.

  Returns a tuple of:
  - valid_courses: list of recognized uppercase course codes (order preserved, no duplicates)
  - duplicates: list of duplicated codes entered
  - unknown_courses: list of codes not present in the catalog
  """
  tokens = raw_input_string.strip().split()
  valid_courses = []
  seen = set()
  duplicates = []
  unknown_courses = []

  for token in tokens:
    code = token.upper()

    if code in seen:
      duplicates.append(code)
      continue
    seen.add(code)

    if code in available_catalog:
      valid_courses.append(code)
    else:
      unknown_courses.append(code)

  return valid_courses, duplicates, unknown_courses