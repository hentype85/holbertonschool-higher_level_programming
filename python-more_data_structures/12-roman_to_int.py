def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    Rs = roman_string
    res = 0

    for i in range(len(Rs)):
        if i == len(Rs) - 1 or d.get(Rs[i]) >= d.get(Rs[i + 1]):
            res += d.get(Rs[i])
        else:
            res -= d.get(Rs[i])
    return res
