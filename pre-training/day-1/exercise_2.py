def grade_classifier(score):
  if score >= 90:
    return 'Distinction'
  elif score >= 60:
    return 'Pass'
  else:
    return 'Fail'

# 1. Testing with 5 specific values
print("--- Manual Results ---")
print(f"Test 1 (95): {grade_classifier(95)}")
print(f"Test 2 (80): {grade_classifier(80)}")
print(f"Test 3 (60): {grade_classifier(60)}")
print(f"Test 4 (59): {grade_classifier(59)}")
print(f"Test 5 (20): {grade_classifier(20)}")
print("-" * 30)

# 2. Testing through the provided list
scores = [45, 72, 91, 60, 38, 85]

print("--- Loop Results ---")
for s in scores:
  result = grade_classifier(s)
  print(f"Score: {s} | Classification: {result}")