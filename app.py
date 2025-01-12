from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="http://127.0.0.1:5000")

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para evitar error 404 por favicon
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Responde con un "No Content" para evitar el error 404

@socketio.on('message')
def handle_message(data):
    print(f'Mensaje recibido: {data}')
    # Emitir el mensaje a todos los clientes conectados
    socketio.emit('message', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
