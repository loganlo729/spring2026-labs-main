## Problem 3: Student Averages from CSV

Write:
```python
def compute_student_averages(input_csv_path: str, output_csv_path: str) -> None:
    ...
```

Input CSV header: student_id,score
Output CSV header: student_id,average_score

Output requirements:
- average_score formatted to exactly 2 decimals
- sorted by average_score desc, tie-break student_id asc
