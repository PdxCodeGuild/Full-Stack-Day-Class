"""Reformat an all-digits phone number into XXX-XXX-XXX and (XXX) XXX-XXX."""
# 1. Setup
# No setup for this problem.

# 2. Input
phone = input('Phone number? All digits. ')

# 3. Transform
# Work on the dependent steps first.
has_area_code = len(phone) < 10

# Then slowly build up the output you want.
if has_area_code:
    phone_parts = [phone[:4], phone[4:7], phone[7:]]
else:
    phone_parts = [phone[:4], phone[4:]]

dashed_phone = '-'.join(phone_parts)
if has_area_code:
    fancy_phone = '({}) {}-{}'.format(
        phone_parts[0], phone_parts[1], phone_parts[2])
else:
    fancy_phone = dashed_phone

# 4. Output
print(dashed_phone)
print(fancy_phone)
