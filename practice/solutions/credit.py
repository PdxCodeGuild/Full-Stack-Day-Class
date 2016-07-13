def validate(card_num_str):
    card_num = [int(d) for d in card_num_str]
    print(card_num)
    check_digit = card_num[-1]
    print(check_digit)
    remainder_num = card_num[:-1]
    print(remainder_num)
    reversed_num = list(reversed(remainder_num))
    print(reversed_num)
    doubled_num = [
        d * 2 if i % 2 == 0 else d
        for i, d
        in enumerate(reversed_num)
    ]
    print(doubled_num)
    subtracted_num = [d - 9 if d > 9 else d for d in doubled_num]
    print(subtracted_num)
    sum_subtracted = sum(subtracted_num)
    print(sum_subtracted)
    ones_sum = sum_subtracted % 10
    print(ones_sum)
    return ones_sum == check_digit
