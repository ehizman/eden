from cardvalidator import luhn
from cardvalidator import formatter


def validate_credit_card(credit_card_number):
    return luhn.is_valid(credit_card_number)


def credit_card_type(credit_card_number):
    return formatter.get_format(credit_card_number)


if __name__ == '__main__':
    print(luhn.generate(16))
    number = input("Enter credit card number")
    if validate_credit_card(number):
        print("valid credit card")
        print("card version", credit_card_type(number))
    else:
        print("invalid credit card")

