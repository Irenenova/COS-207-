scores = {62, 75, 48, 90, 71}
course = "WSU-COS 207"
mean = sum(scores) / len(scores)
passed = mean >= 50
for value in (scores, course, mean, passed):
 print(f"{type(value)._name_:<6} {value}")
print(f"{course}: n = {len(scores)}, mean = {mean:.2f}")