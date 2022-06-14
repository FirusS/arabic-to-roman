def roman_to_arabic(roman):
    roman_value_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    for i in range(len(roman)):
        if i > 0 and roman_value_list[roman[i]] > roman_value_list[roman[i - 1]]:
            int_value += roman_value_list[roman[i]] - 2 * roman_value_list[roman[i - 1]]
        else:
            int_value += roman_value_list[roman[i]]
    return int_value


def arabic_to_roman(number):
    m = ["", "M", "MM", "MMM", "MMMM", "MMMMM", "MMMMMM", "MMMMMMM", "MMMMMMMM", "MMMMMMMMM", "MMMMMMMMMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    tukstanciai = m[number // 1000]
    simtai = c[(number % 1000) // 100]
    desimtis = x[(number % 100) // 10]
    vienetai = i[number % 10]

    ats = (tukstanciai + simtai +
           desimtis + vienetai)

    return ats
