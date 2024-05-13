from flask import Flask, render_template, request
import pywhatkit as kit

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/schedule', methods=['POST'])
def schedule_message():
    phone_number = request.form['phone_number']
    message = request.form['message']
    datetime = request.form['datetime']

    # Placeholder function for sending message (replace with actual WhatsApp API integration)
    kit.sendwhatmsg_instantly(phone_number, message, tab_close=True)

    return render_template('success.html')


if __name__ == '__main__':
    print('started')
    app.run(debug=True, host='127.0.0.1', port=5001)
