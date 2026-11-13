# def is_odd(n):
#     if n % 2 == 0:
#         return False
#     return True
#
# n=int(input("Enter a number: "))
# print(is_odd(n))
#
#
# def leap_year(n):
#     if n % 400 == 0:
#         return True
#     elif n % 100 == 0:
#         return False
#     elif n % 4 == 0:
#         return True
# n=int(input("Enter a year: "))
# print(leap_year(n))


# def print_triangular_numbers(n):
#     total = 0
#     for i in range (1,n+1):
#         total += i
#         print(i, total)
# print_triangular_numbers(5)


# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2, n):
#         if n%i==0:
#             return False
#     return True
# print(is_prime(10))


# def reverse(s):
#     result = ""
#     for char in s:
#         result = char + result
#     return result
# print(reverse("hello world"))
#
# def reverse_slice(s):
#     return s[::-1]
# print(reverse_slice("hello world"))


# def remove_all_occurrences(sub, s):
#     return s.replace(sub, "")
# print(remove_all_occurrences("ll", "hello world"))


# def substitude(message, key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch)
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "tfzjebilümuıcrçğvşöpnkgshadyo"
# print(substitude("hello world", key))


# def remove_dups(s):
#      result = ""
#      for ch in s:
#          if ch.lower() not in result.lower():
#              result = result + ch
#      return result
# print(remove_dups("hello world"))

