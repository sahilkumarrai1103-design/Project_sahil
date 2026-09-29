# Problem Statement: Fully Flexible Credit System (FFCS) Auditor

## 1. Problem Description
Under the university's Fully Flexible Credit System (FFCS), students construct personalized course timetables each semester. However, manual course registration frequently causes administrative rejections due to:
- Time slot clashes (e.g., registering for two courses assigned to the same slot, such as A1 or TA1).
- Credit boundary violations (falling below the minimum 16 credits or exceeding the maximum 27 credits).
- Unmet prerequisite chains (registering for advanced courses without clearing foundational prerequisites).

## 2. Objective & Scope
The objective is to implement a robust, lightweight command-line audit system using core Python 3 data structures. The tool allows students to test course combinations prior to official portal submission, eliminating registration failures.

## 3. Algorithmic Approach
- **Slot Collision Detection:** Implements pairwise set intersection ($A \cap B$) to identify overlapping slot codes in $O(1)$ to $O(N)$ time.
- **Credit Compliance:** Calculates cumulative credits and verifies against minimum and maximum boundaries.
- **Prerequisite Validation:** Evaluates set difference ($Prerequisites \setminus Completed$) to verify whether mandatory prerequisites have been satisfied.
- **Input Sanitization:** Strips irregular spacing, standardizes uppercase tokens, and eliminates duplicate course codes.