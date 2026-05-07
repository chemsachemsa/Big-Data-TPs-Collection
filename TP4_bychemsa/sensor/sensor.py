import socket
import time

# ننتظر شوي باش السيرفر يكون جاهز
time.sleep(3)

# إنشاء socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# الاتصال بالسيرفر (اسم الخدمة server داخل Docker network)
client.connect(("server", 5000))

# إرسال البيانات
client.send("Temperature: 25°C".encode())

print("Data sent!")

# إغلاق الاتصال
client.close()