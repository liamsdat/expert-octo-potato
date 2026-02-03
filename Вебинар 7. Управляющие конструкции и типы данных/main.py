data = []

#[
#     [
#         "TV",
#         [
#             ('DNS', 11_999),
#             ('Eldorado', 13_000),
#             ('Y.Market', 12_000)
#         ],
#     ],
#
#     [
#         "Laptop",
#         [
#             ('DNS', 12_999),
#             ('Eldorado', 15_000),
#             ('Y.Market', 11_000)
#         ]
#     ],
#
#     [
#         "Phone",
#         [
#             ('DNS', 15_999),
#             ('Eldorado', 16_000),
#             ('Y.Market', 16_199)
#         ]
#     ]
# ]
while True:
    title = input("Enter any product name, or 'end' to quit => ")
    if title == "end":
        break
    good = [title]
    while True:
        shop = input("Enter any shops, or 'end' to quit => ")
        if shop == "end":
            break
        price = int(input("Enter price product name => "))


