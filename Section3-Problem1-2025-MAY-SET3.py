def average_rating(data):
    return round(sum(b["rating"] for b in data) / len(data), 2)

def average_pages(data):
    return round(sum(b["pages"] for b in data) / len(data), 2)

def longest_book(data):
    best = max(data, key=lambda b: (b['pages'],b["rating"]))
    return best["book_id"]

def above_average_books(data):
    avg_rating = average_rating(data)
    avg_pages = average_pages(data)
    return {
        b["book_id"]
        for b in data
        if b["rating"] > avg_rating and b["pages"] > avg_pages
    }

def book_analysis(data: list, request: str):
    """
    Perform the operation specified by ``request`` on the list of book dictionaries ``data``.

    Supported requests:
    - "average_rating"
    - "average_pages"
    - "longest_book"
    - "above_average_books"
    """
    
    
    if request == "average_rating":
        return average_rating(data)
    if request == "average_pages":
        return average_pages(data)
    if request == "longest_book":
        return longest_book(data)
    if request == "above_average_books":
        return above_average_books(data)
    raise ValueError("Unsupported request")

# #Another Method:


# def book_analysis(data: list, request: str):
#     """
#     Perform the operation specified by ``request`` on the list of book dictionaries ``data``.

#     Supported requests:
#     - "average_rating"
#     - "average_pages"
#     - "longest_book"
#     - "above_average_books"
#     """
#     sum=0
#     count=len(data)
#     if request=='average_rating':
#         for i in data:
#             sum +=i["rating"]
#         return round((sum/count),2)
#     if request=='average_pages':
#         for i in data:
#             sum +=i["pages"]
#         return round((sum/count),2)
#     if request=='longest_book':
#         max_pages=0
#         for i in data:
#             if i["pages"] >max_pages:
#                 max_id=i["book_id"]
#                 max_rating=i["rating"]
#                 max_pages=i["pages"]
#             elif i["pages"] == max_pages:
#                 if i["rating"] > max_rating:
#                     max_id=i["book_id"]
#                     max_rating=i["rating"]
#                     max_pages=i["pages"]
#         return max_id
#     if request=='above_average_books':
#         l=[]
#         for i in data:
#             if i["rating"] > book_analysis(data,'average_rating'):
#                 if i["pages"] > book_analysis(data,'average_pages'):
#                     l.append(i["book_id"])
#         return set(l)
        
#     Book Reading List Data Analysis
# You are given a list of dictionaries, each representing a book in a reading list.
# Every dictionary contains the following keys:

# book_id (str) a unique identifier for the book
# pages (int) the number of pages of the book
# rating (float) the rating of the book (05)
# Implement a function book_analysis(data, request) that performs the operation specified by request on the list data.

# Supported requests:

# average_rating - Return the average rating of all books, rounded to two decimal places.
# average_pages - Return the average number of pages of all books, rounded to two decimal places.
# longest_book - Return the book_id of the book with the maximum number of pages.
# If several books share the same maximum page count, return the one among them with the highest rating.
# above_average_books Return a set of book_ids of books that satisfy both conditions:
# rating strictly greater than the average rating of all books, and
# pages strictly greater than the average number of pages.
# NOTE: This is a function type question, you don't have to take input or print the output, you just have to complete the required function definition.    
        
            
    

    
