from flask import Flask, jsonify, request

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
    if  operation == 'add':
        return jsonify({'status': 200, 'result': numberA + numberB}), 200
    
    #Division operation: 
    elif operation == 'divide':
        if numberB == 0:
            return jsonify ({'status':400 , 'error': 'Division by zero is not allowed!'}), 400
        return jsonify({'status': 200, 'result': numberA / numberB}), 200
    
    #multiplication operation:
    elif operation == 'multiply':
        return jsonify({'status': 200, 'result': numberA * numberB}), 200
    
    elif operation =='minus':
        return jsonify({'status':200, 'result':numberA - numberB}), 200
         
    '''
    some information you might need

    You can use different status codes to indicate specific conditions. For instance:
        A status of 200 indicates success.
        A status of 400 can indicate a bad request (like division by zero).
        A status of 500 can be used for server errors.
    '''

    return jsonify({'status': 400, 'result':f"{operation} operation not implemented yet"}), 400

@app.route('/')
def home():
    base_url = request.host_url.rstrip('/')
    return jsonify({
        'status': 400,
        'error': 'Invalid URL format. Please use the format:' + f'{base_url}/operation/numberA/numberB',
        'example': '/add/1/2, /minus/5/3, /multiply/2/4, /divide/8/2'
    })

if __name__ == '__main__':
    app.run(debug=True)
