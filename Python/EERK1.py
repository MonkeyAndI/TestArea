def square_digits(num):
    print(''.join(str(int(d)**2) for d in str(num)))

square_digits(7899)