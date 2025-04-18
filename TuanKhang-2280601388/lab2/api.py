from flask import Flask, request, jsonify
from cipher.ceasar import CeasarCipher
app = Flask(__name__)
ceasar_cipher = CeasarCipher()
@app.route("/api/ceasar/encrypt", methods=['POST'])
def ceasar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    text = data['text']
    key = int(data['key'])
    encrypted_text = ceasar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})
@app.route("/api/ceasar/decrypt", methods=['POST']) 
def ceasar_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = int(data['key'])
    decrypted_text = ceasar_cipher.decrypt_text(encrypted_text, key)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 5000, debug=True)

