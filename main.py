from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sms", methods=["POST"]) 
def sms_reply():  
    incoming_msg = request.form.get('Body')  
    from_number = request.form.get('From')
  
    print(f"Message from {from_number}: {incoming_msg}")
  
    response = f"Hello. This is Æther. You said: {incoming_msg}"
  
    return f"""<?xml version="1.0" encoding="UTF-8"?> 
    <Response> 
        <Message>{response}</Message>
</Response>""", 200, {'Content-Type': 'application/xml'} 

if __name__ == "__main__":
    app.run()
