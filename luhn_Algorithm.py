def main():
    # initializes the card number and the translation parameters for our number
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-':'',' ':''})
    translated_card_number = card_number.translate(card_translation)
    # Displays the validity of our translated card number via the luhn algorithm
    if card_number_verification(translated_card_number):
        print('valid')
    else:
        print('invalid')

# This function works through the luhn algorithm process 
def card_number_verification(card_number):
    # the first step; reversal of the card number
    card_number_reversed = card_number[::-1]
    # next we initialize starting sum values and starting index values for our even and odd string translations
    sum_of_odd_digits = 0
    odd_digits = card_number_reversed[::2]

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    # Adds each odd digit to the value of our odd digits.
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    # This next step is more in depth. We multiply each even number by 2, and if that number is larger than 10 we combine the digits.
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
            # We than add it all to the sum of even digits.
        sum_of_even_digits += number
    # After determining the total of our digits we can search for a remainder, and the validity of our card number.
    total = sum_of_even_digits + sum_of_odd_digits

    return total % 10 == 0

main()