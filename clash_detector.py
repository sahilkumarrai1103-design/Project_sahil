# clash_detector.py - Slot collision detection using set operations


def find_slot_conflicts(selected_course_codes, catalog):
  """Checks pairwise combinations of selected courses for overlapping time slots.

  Returns a list of clash dictionaries with the overlapping slot(s).
  """
  conflicts = []
  codes = list(selected_course_codes)

  for i in range(len(codes)):
    for j in range(i + 1, len(codes)):
      code_a = codes[i]
      code_b = codes[j]

      slots_a = catalog.get(code_a, {}).get("slots", set())
      slots_b = catalog.get(code_b, {}).get("slots", set())

      overlap = slots_a & slots_b  # Set intersection to detect clash
      if overlap:
        conflicts.append({
            "course_1": code_a,
            "course_2": code_b,
            "conflicting_slots": sorted(overlap),
        })
  return conflicts


def get_all_occupied_slots(selected_course_codes, catalog):
  """Returns the union set of all time slots occupied by the selected courses."""
  occupied = set()
  for code in selected_course_codes:
    occupied |= catalog.get(code, {}).get("slots", set())
  return occupied