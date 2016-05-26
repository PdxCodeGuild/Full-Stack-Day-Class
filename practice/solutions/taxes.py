"""Calculate Oregon income tax."""
taxable_income = int(input('Enter your income: '))

tax_burdon = 0

if taxable_income > 3350:
    tax_burdon += 3350 * 0.05
    taxable_income -= 3350
else:
    tax_burdon += taxable_income * 0.05
    taxable_income = 0

if taxable_income > 5050:
    tax_burdon += 5050 * 0.07
    taxable_income -= 5050
else:
    tax_burdon += taxable_income * 0.07
    taxable_income = 0

if taxable_income > 116600:
    tax_burdon += 116600 * 0.07
    taxable_income -= 116600
else:
    tax_burdon += taxable_income * 0.09
    taxable_income = 0

if taxable_income > 0:
    tax_burdon += taxable_income * 0.099
    taxable_income = 0

print(tax_burdon)
