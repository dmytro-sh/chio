# def isometric_strings(str1: str, str2: str) -> bool:
#     if len(str1) != len(srt2):
#         return False
#     return None
# isometric_strings('add', 'egg')
# isometric_strings('foo', 'bar')

def checkio(number: int) -> str:
    if number%3 ==0 and number%5 ==0:
        result = 'Fizz Buzz'
    elif number%3 ==0:
        result = 'Fizz'
    elif number%5 ==0:
        result = 'Buzz'
    else:
        result = number
    return result

checkio(7)

