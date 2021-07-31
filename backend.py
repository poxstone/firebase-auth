from flask import Flask, request, send_from_directory

app = Flask(__name__)

# FIRE BASE
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# ROUTES

@app.route('/')
def index_path():
    return send_from_directory('.', 'index.html')


@app.route('/validate', methods=['GET'])
def form_path():
        
    recive_email = request.args.get('user')
    recive_token = request.args.get('token')

    try:
        decoded_token = auth.verify_id_token(recive_token)
        uid = decoded_token['uid']
        token_email = decoded_token['email']
        print(uid)
        if uid and token_email == recive_email:
            return "Valid token"
        else:
            raise "error"
    except Exception as e:
        return "Invalid token"




        


if __name__ == "__main__":
    app.run()
