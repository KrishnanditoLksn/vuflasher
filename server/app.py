import uuid
from flask  import Flask,jsonify , request
from flask_cors import CORS
from utils.util import BOOKS

app = Flask(__name__)
app.config.from_object(__name__)


CORS(
    app, 
    resources={r'/*': {'origins': '*'}}
)



@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books' , methods=['GET'])
def getAllBooks():
    return jsonify({
        'status':'Success',
        'books' : BOOKS
    })

@app.route('/books/add' , methods=['POST'])
def postBook():
    book_request =  request.get_json()
    
    BOOKS.append({
        'title':book_request.get('title'),
        'author':book_request.get('author'),
        'read':False
    })
    
    return jsonify({
        'status':'Success',
        'messsage':'Book Successfully Added to List'
    })

@app.route('/books/update/<book_id>' , methods=['PUT'])
def updateBook(book_id):
    
    single_book_data = request.get_json()
    BOOKS.append({
            'id': uuid.uuid4().hex,
            'title':single_book_data.get('title'),
            'author': single_book_data.get('author'),
            'read':single_book_data.get('read')
    })
    return jsonify({
        'status':'Success',
        'messsage':'Book Successfully Updated'
    })


if __name__ == '__main__':
    app.run()
