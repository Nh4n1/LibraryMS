from flask import Flask, jsonify, render_template, request

app =Flask(__name__)

BOOKS=[
    {"id":1,
     "title":"The Great Gatsby",
     "author":"F. Scott Fitzgerald",
     "year":1925,
     "category":"Fiction",
     "available":True},
    {"id":2,
     "title":"To Kill a Mockingbird",
     "author":"Harper Lee",
     "year":1960,
     "category":"Fiction",
     "available":True},
    {"id":3,
     "title":"1984",
     "author":"George Orwell",
     "year":1949,
     "category":"Dystopian",
     "available":True
    },{
        "id":4,
        "title":"Pride and Prejudice",
        "author":"Jane Austen",
        "year":1813,
        "category":"Romance",
        "available":True
    },{
        "id":5,
        "title":"The Catcher in the Rye",
        "author":"J.D. Salinger",
        "year":1951,
        "category":"Fiction",
        "available":False
    },{
        "id":6,
        "title":"The Hobbit",
        "author":"J.R.R. Tolkien",
        "year":1937,
        "category":"Lap trinh",
        "available":True
    }
]

@app.route('/')
def index():
    bookCount = len(BOOKS)
    bookAvailableCount = sum(1 for book in BOOKS if book['available'])
    return f"Total books: {bookCount}<br>Available books: {bookAvailableCount}"

@app.route("/books")
def books():
    category = request.args.get("category")
    if category:
        result = [book for book in BOOKS if book["category"].lower() == category.lower()]
    else:
        result = BOOKS
    return render_template("books.html", books=result)

@app.route("/books/<int:book_id>")
def book_detail(book_id):
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    if book is None:
        return render_template("404.html"), 404
    return render_template("book_detail.html", book=book)

@app.route("/api/books")
def api_books():
    return jsonify({"books": BOOKS})

@app.route("/api/books/<int:book_id>")
def api_book_detail(book_id):
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    if book is None:
        return jsonify({"error": f"Book with id {book_id} not found"}), 404
    return jsonify(book)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404 

if __name__ == '__main__':
    app.run(debug=True)
    
    