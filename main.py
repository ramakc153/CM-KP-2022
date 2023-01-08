from cctv_login import create_app
import socket

app = create_app()

hostname = socket.gethostname()
iphost = socket.gethostbyname(hostname)


#start program
if __name__ == '__main__':
    app.run(debug=True, host=(iphost), port=5000)