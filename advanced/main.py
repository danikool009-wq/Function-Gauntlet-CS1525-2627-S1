def temperature_is_safe_range(celsius, minimjum_f, maximum_f):
    f_temp = celsius*1.8 + 32
    if f_temp >= minimjum_f and f_temp <= maximum_f:
        return True
    else:
        return False
def can_afford_with_tip(balance,cost,
    tip_percent):
        tips = cost*(tip_percent/100)
        if balance >= tips+cost:
            return True
        else:
            return False

def meets_average(score1,score2,score3, required_average):
    average = (score1 + score2 + score3)/3
    if average >= required_average:
        return True
    else:
        return False
def initials_match(first_name, last_name,expected_initials):
        initial = first_name[0].upper() + last_name[0].upper()
        if initial == expected_initials.upper():
            return True
        else:
            return False