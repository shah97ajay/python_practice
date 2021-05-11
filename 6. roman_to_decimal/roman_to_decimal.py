numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
romanNumeral = input("Enter the Roman numeral : ")
def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if numbers[left] < numbers[right]:
            sum -= numbers[left]
        else:
            sum += numbers[left]
    sum += numbers[romanNumeral[-1]]
    return sum
print ("Your decimal number is : ",RomanNumeralToDecimal(romanNumeral))