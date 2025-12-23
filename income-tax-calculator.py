
# Personal Income Tax Calculator (2009)

def compute_tax(income, brackets):
    tax = 0
    previous = 0

    for upper, rate in brackets:
        if income > upper:
            tax += (upper - previous) * rate
            previous = upper
        else:
            tax += (income - previous) * rate
            return tax

    return tax


single = [
    (8350, 0.10),
    (33950, 0.15),
    (82250, 0.25),
    (171550, 0.28),
    (372950, 0.33),
    (10**12, 0.35)   
]

married_joint = [
    (16700, 0.10),
    (67900, 0.15),
    (137050, 0.25),
    (208850, 0.28),
    (372950, 0.33),
    (10**12, 0.35)
]

married_separate = [
    (8350, 0.10),
    (33950, 0.15),
    (68525, 0.25),
    (104425, 0.28),
    (186475, 0.33),
    (10**12, 0.35)
]

head_house = [
    (11950, 0.10),
    (45500, 0.15),
    (117450, 0.25),
    (190200, 0.28),
    (372950, 0.33),
    (10**12, 0.35)
]


status_map = {
    0: single,
    1: married_joint,
    2: married_separate,
    3: head_house
}

# Input
status = int(input("Enter filing status (0-3): "))
income = float(input("Enter taxable income: "))

# Compute
brackets = status_map.get(status)
if brackets is None:
    print("Invalid filing status")
else:
    tax = compute_tax(income, brackets)
    print("Total tax payable is $", round(tax, 2))
