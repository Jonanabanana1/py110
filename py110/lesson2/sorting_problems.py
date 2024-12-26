# 1) Sort the following list of numbers first in ascending numeric order, then in descending numeric order. Do not mutate the list.
# lst = [10, 9, -6, 11, 7, -16, 50, 8]
# print(sorted(lst))
# print(sorted(lst, reverse=True))

# 2) Repeat the previous exercise but, this time, perform the sort by mutating the original list.
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# 3) Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.
# lst = [10, 9, -6, 11, 7, -16, 50, 8]
# lst.sort(key=str)
# print(lst)
# lst.sort(key=str, reverse=True)
# print(lst)

# 4) How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?
books = [
    {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel Garcia Marquez",
        "published": "1967",
    },
    {
        "title": "The Book of Kells",
        "author": "Multiple Authors",
        "published": "800",
    },
    {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "published": "1869",
    },
]


def get_publish_year(book):
    return int(book["published"])


books.sort(key=get_publish_year)
print(books)
