from flask import Flask, request, session
from alexbot import ask, append_interaction_to_chat_log

app = Flask(__name__)
# if for some reason your conversation with the bot gets weird, change the secret key 
app.config['SECRET_KEY'] = '89djhff9lhkd93'

@app.route('/alexbot', methods=['POST'])
def jabe():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)
    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)