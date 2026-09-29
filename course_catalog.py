# course_catalog.py - Course database, slot definitions, and student profile

COURSES = {
    "CSE1021": {
        "title": "Python Essentials",
        "credits": 4,
        "slots": {"A1", "TA1"},
        "prereqs": set(),
    },
    "MAT1011": {
        "title": "Calculus and Differential Equations",
        "credits": 4,
        "slots": {"B1", "TB1"},
        "prereqs": set(),
    },
    "PHY1001": {
        "title": "Engineering Physics",
        "credits": 3,
        "slots": {"C1", "TC1"},
        "prereqs": set(),
    },
    "CSE2001": {
        "title": "Data Structures and Algorithms",
        "credits": 4,
        "slots": {"A1", "TA1"},  # Clashes with CSE1021
        "prereqs": {"CSE1021"},
    },
    "ENG1001": {
        "title": "Technical English",
        "credits": 2,
        "slots": {"D1"},
        "prereqs": set(),
    },
    "HUM1021": {
        "title": "Ethics and Values",
        "credits": 2,
        "slots": {"E1"},
        "prereqs": set(),
    },
    "CHY1001": {
        "title": "Engineering Chemistry",
        "credits": 3,
        "slots": {"F1"},
        "prereqs": set(),
    },
}

STUDENT_PROFILE = {
    "reg_no": "26BAC10021",
    "completed_courses": {"CSE1001", "MAT1001"},
    "min_credits": 16,
    "max_credits": 27,
}