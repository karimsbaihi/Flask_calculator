from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<operation>/<numberA>/<numberB>')
def calculate(operation, numberA, numberB):
    try:
        #   convert to float
        numberA = float(numberA)
        numberB = float(numberB)
    except ValueError:
        return jsonify({'status': 400, 'error': 'Invalid input. Please provide numbers.'}), 400

    #here you write the operations using if/else 
    '''
    2. Custom Error Handling:

    You can use different status codes to indicate specific conditions. For instance:
        A status of 200 indicates success.
        A status of 400 can indicate a bad request (like division by zero).
        A status of 500 can be used for server errors.
    '''


    return jsonify({'status': 400, 'result':'code not completed'}), 400
if __name__ == '__main__':
    app.run(debug=True)
