from typing import List


def get_number_array(number: str):
    card_number_array: List[int] = []
    for i in range(len(number)):
        temp: int = number[i]
        card_number_array.append(int(temp))
    return card_number_array


def sum_card_numbers(number: str):
    card_number_n: List[int] = get_number_array(number)
    for i in card_number_n:
        i += 2
        card_number_n.append(get_digit(i))
    return sum(card_number_n)


def get_digit(number):
    number *= 2
    if number > 9:
        number = 1 + number % 10
    return number


def get_size(number: []):
    return len(number)


def get_prefix(number: [], k):
    if get_size(number) > k:
        num = ""
        for i in k:
            i += 1
            num.append(number[i])
            return int(num)
    return int(number)


def get_numeric_size(d):
    num = d + ""
    return len(num)


def get_prefix_matched(number: [], d: int):
    return get_prefix(number, get_numeric_size(d)) == d


def is_valid(number):
    return (13 <= len(get_number_array(number)) <= 16) and (sum_card_numbers(number) % 10 == 0) and (get_prefix_matched(get_number_array(number), 4) or get_prefix_matched(get_number_array(number), 5) or get_prefix_matched(get_number_array(number), 6) or get_prefix_matched(get_number_array(number), 37))


if __name__ == "__main__":
    card_number: str = input("Enter card number: ")
    if is_valid(number=card_number):
        print("card is valid")
    else:
        print("card is invalid")
        print("hello")

#     public CardType getCardType(int[] number, int d) {
#
#         if (!getPrefixMatched(number, d)) {throw new InvalidParameterException("Invalid Card details");}
#         else
#             switch (d){
#                 case 4:
#                     if(number.length == 13 || number.length == 16)
#                         cardType = CardType.VISA;
#                     break;
#                 case 6:
#                     if (number.length == 16)
#                         cardType = CardType.VERVE;
#                     break;
#                 case 5:
#                     if (number.length == 16)
#                         cardType = CardType.MASTER;
#                     break;
#                 case 34:
#                 case 37:
#                     if (number.length == 15)
#                         cardType = CardType.AMERICA;
#                 default:
#             }return cardType;
#     }
# }
