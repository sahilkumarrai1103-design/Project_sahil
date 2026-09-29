# FFCS Course Slot Conflict & Credit Limit Auditor

A modular Python 3 CLI system designed to validate course registrations against academic rules, timetable conflicts, and prerequisite constraints.

---

## Features
- **Pairwise Clash Detection:** Identifies overlapping lecture and lab slots across selected courses using set intersection operations.
- **Credit Boundary Auditing:** Verifies that enrolled credits fall strictly within the permissible window (16 to 27 credits).
- **Prerequisite Checking:** Uses set subtraction to flag missing prerequisite dependencies.
- **Input Sanitization:** Converts tokens to uppercase, strips whitespace, ignores duplicate entries, and filters unrecognized course codes.
- **Formatted Terminal Reports:** Outputs structured ASCII course tables and clear audit statuses.
- **Automated Test Suite:** Built-in unit test verification covering edge cases via Python's standard `unittest` framework.

---

## Project Structure
- `course_catalog.py`: Defines available courses, credit weights, assigned slots, and student baseline profile.
- `clash_detector.py`: Contains set-based slot collision logic.
- `credit_auditor.py`: Evaluates credit limits and prerequisite conditions.
- `validator.py`: Normalizes and sanitizes user input tokens.
- `timetable_view.py`: Renders tabular summaries and audit reports in the terminal.
- `main.py`: Driver script managing interactive CLI workflow.
- `test_registration.py`: Automated unit tests testing core validation logic.
- `statement.md`: Problem statement and project scope document.

---

## How to Run

### Interactive Application
```bash
python main.py