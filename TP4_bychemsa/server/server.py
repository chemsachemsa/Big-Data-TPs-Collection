import socket

# إنشاء socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ربطه بالمنفذ
server.bind(("0.0.0.0", 5000))

# الاستماع لاتصال واحد
server.listen(1)

print("Server is waiting for connection...")

# قبول الاتصال
conn, addr = server.accept()
print("Connected from:", addr)

# استقبال البيانات
data = conn.recv(1024)
print("Received:", data.decode())

# إغلاق الاتصال
conn.close()
server.close()