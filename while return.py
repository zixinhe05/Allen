def  make_book(artist,title):
    book = f"{artist} {title}"
    return book.title()
while True:
    print("please tell me the artist and the title of the book")
    print("(enter 'q' at any time to quit)")
    artist = input("type the author:")
    if artist == 'q':
     break
    title = input("type the title:")
    if title == "q":
     break
    book1 = make_book(artist, title)
    print(book1)


