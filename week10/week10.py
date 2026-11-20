# mylist = [76, 92.3, "hello", True, 4, 76]
#
# mylist.append("apple")
# mylist.append(76)
# mylist.insert(3, "cat")
# mylist.insert(0, 99)
# print(mylist)
#
# print(mylist.index("hello"))
#
# print(mylist.count(76))
#
# mylist.remove(76)
# print(mylist)
#
# mylist.pop(mylist.index(True))
# print(mylist)


# def sum_of_squares(xs):
#     sum = 0
#     for x in xs:
#         sum = sum + x**2
#     return sum
#
#
# nums = [3, 4, 5]
# print(sum_of_squares(nums))


# def even_sum(xs):
#     sum = 0
#     for x in xs:
#         if x%2 == 0:
#             sum = sum + x
#     return sum
# nums = [2, 5, 14, 19, 22]
# print(even_sum(nums))

# def letter_counter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
#
# my_list = ["apple", "cat", "lemon", "python", "tiger"]
# print(letter_counter(my_list))


# def sum_untill_even(xs):
#     sum = 0
#     for x in xs:
#         if x % 2 == 0:
#             break
#         else:
#             sum += x
#     return sum
# nums = [3, 5, 7, 12, 9, 11]
# print(sum_untill_even(nums))


# def count_words_untill_sam(words):
#     counter = 0
#     for word in words:
#         if word == "sam":
#             counter += 1
#             break
#         else:
#             counter += 1
#     return counter
# words = ["hello", "cat", "lemon", "sam", "tiger"]
# print(count_words_untill_sam(words))


# def replace(s, old, new):
#     pieces = s.split(old)
#     return new.join(pieces)
# s="Mississippi"
# print(replace(s, "i", "I"))


# def max(nums):
#     largest = nums[0]
#     for num in nums[1:]:
#         if num > largest:
#             largest = num
#     return largest
#
# nums = [2, 5, 11, 6, 27]
# print(max(nums))

