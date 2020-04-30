ean_digits = int(input('Enter the first 12 digits of an EAN: '))

digit_12 = ean_digits % 10
digit_11 = (ean_digits // 10) % 10
digit_10 = (ean_digits // 100) % 10
digit_9 = (ean_digits // 1000) % 10
digit_8 = (ean_digits // 10000) % 10
digit_7 = (ean_digits // 100000) % 10
digit_6 = (ean_digits // 1000000) % 10
digit_5 = (ean_digits // 10000000) % 10
digit_4 = (ean_digits // 100000000) % 10
digit_3 = (ean_digits // 1000000000) % 10
digit_2 = (ean_digits // 10000000000) % 10
digit_1 = (ean_digits // 100000000000) % 10

sum_1 = digit_2 + digit_4 + digit_6 + digit_8 + digit_10 + digit_12
sum_2 = digit_1 + digit_3 + digit_5 + digit_7 + digit_9 + digit_11

sum_3 = sum_1 * 3 + sum_2
total = sum_3 - 1
remainder = total % 10
result = 9 - remainder

print('Check digit: {}'.format(result))