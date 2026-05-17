raw = "   0712 345 678   "
# Remove leading and trailing whitespace
step1 = raw.strip()
print(step1)
step2 = step1.replace(" ", "")
print(step2)
if step2.startswith("0"):
    step3 = "+254" + step2[1:]
    print(step3)