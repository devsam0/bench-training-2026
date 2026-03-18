students = [
  {"name": "Usama", "scores": [85, 92, 88], "subject": "ML"},
  {"name": "Ali", "scores": [70, 65, 80], "subject": "Python"},
  {"name": "Ahsan", "scores": [95, 98, 92], "subject": "Math"},
  {"name": "Taha", "scores": [60, 55, 62], "subject": "DL"},
  {"name": "Mateen", "scores": [88, 84, 90], "subject": "AI"}
]
def calculate_average(scores):
  return sum(scores) / len(scores) if scores else 0

def get_grade(avg):
  if avg >= 90: return 'A'
  if avg >= 80: return 'B'
  if avg >= 70: return 'C'
  return 'F'

def class_topper(students):
  return max(students, key=lambda s: calculate_average(s['scores']))


topper = class_topper(students)

sorted_report = sorted(students, key=lambda s: calculate_average(s['scores']), reverse=True)

print(f"{'Name':<10} | {'Avg':<5} | {'Grade':<5}")

for s in sorted_report:
  avg = calculate_average(s['scores'])
  grade = get_grade(avg)
  row = f"{s['name']:<10} | {avg:<5.1f} | {grade:<5}"
    
  if s == topper:
    print(f"{row} *** TOP ***")
  else:
    print(row)