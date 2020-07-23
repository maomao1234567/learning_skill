import socket
import sys

# 创建 socket 对象
server_socket = socket.socket()

# 获取本地主机名
host = socket.gethostname()
port = 9999

# 绑定端口号
server_socket.bind(('127.0.0.1', port))

# 设置最大链接数，超过后排队
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    print(f"链接地址：{str(addr)}")

    msg = '欢迎访问我的socket server!'
    client_socket.send(msg.encode('utf-8'))
    client_socket.close()
