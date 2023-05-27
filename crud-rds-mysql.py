import pymysql
from flask import Flask, jsonify, request

app = Flask(__name__)

connection = pymysql.connect(host='',
                             user='',
                             password='',
                             database='mybooks')

@app.route('/books', methods=['GET'])
def get_books():
    cur = connection.cursor()
    cur.execute("SELECT * FROM mybook")
    books = cur.fetchall()
    cur.close()
    book_list = []
    for book in books:
        book_dict = {
            'id': book[0],
            'author': book[1],
            'title': book[2],
            'isdn': book[3]
        }
        book_list.append(book_dict)
    return jsonify(book_list)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    print(book_id)
    cur = connection.cursor()
    cur.execute("SELECT * FROM mybook WHERE id = %s", (book_id,))
    book = cur.fetchone()
    cur.close()
    if book:
        book_dict = {
            'id': book[0],
            'author': book[1],
            'title': book[2],
            'isdn': book[3]
        }
        return jsonify(book_dict)
    else:
        return jsonify({'message': 'Book not found'}), 404


@app.route('/books', methods=['POST'])
def create_book():
    author = request.json['author']
    title = request.json['title']
    isdn = request.json['isdn']

    cur = connection.cursor()
    cur.execute("INSERT INTO mybook (author, title, isdn) VALUES (%s, %s, %s)", (author, title, isdn))
    connection.commit()
    cur.close()

    return jsonify({'message': 'Book created successfully'}), 201


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    author = request.json['author']
    title = request.json['title']
    isdn = request.json['isdn']

    cur = connection.cursor()
    cur.execute("UPDATE mybook SET author = %s, title = %s, isdn = %s WHERE id = %s",
                (author, title, isdn, book_id))
    connection.commit()
    cur.close()

    return jsonify({'message': 'Book updated successfully'})


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    cur = connection.cursor()
    cur.execute("DELETE FROM mybook WHERE id = %s", (book_id,))
    connection.commit()
    cur.close()

    return jsonify({'message': 'Book deleted successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
