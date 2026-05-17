phone = "0712345678"
first_char = phone[0]
print(first_char)
last_char = phone[-1]
print(last_char)
n = len(phone)
print(n)
prefix = phone[0:4]
print(prefix)
suffix = phone[4:8]
print(suffix)
international_format = "+254" + phone[1:]
print(international_format)
masked = phone[0:4] + "****" + phone[6:10]
print(masked)
full_number = phone[:]
print(full_number)


