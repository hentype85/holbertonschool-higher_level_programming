def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    Rstr = roman_string
    res = 0
    for i in range(len(Rstr)):
        if Rstr[i] in d:
            if i < len(Rstr) - 1 and d[Rstr[i]] < d[Rstr[i + 1]]:
                res -= d[Rstr[i]]
            else:
                res += d[Rstr[i]]
    return res
