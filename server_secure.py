import http.server
import socketserver
import socket
import threading

PORT = 8000
MAX_CONNECTIONS = 100  # Giới hạn số kết nối đồng thời
TIMEOUT = 5  # Giảm thời gian chờ cho mỗi kết nối (giây)

# Tạo một danh sách để theo dõi các kết nối đang mở
active_connections = []

# Lớp xử lý yêu cầu HTTP có khả năng bảo vệ Slowloris
class SlowlorisProtectedHandler(http.server.SimpleHTTPRequestHandler):

    def setup(self):
        self.request.settimeout(TIMEOUT)
        super().setup()

    def handle_one_request(self):
        # Nếu số lượng kết nối vượt quá MAX_CONNECTIONS, đóng kết nối
        if len(active_connections) > MAX_CONNECTIONS:
            self.send_error(503, "Server quá tải, thử lại sau.")
            self.close_connection = True
            return

        active_connections.append(self.request)
        try:
            super().handle_one_request()
        finally:
            active_connections.remove(self.request)

# Để hỗ trợ đa luồng, mỗi kết nối sẽ được xử lý bởi một luồng riêng biệt
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

# Tạo server
with ThreadedTCPServer(("", PORT), SlowlorisProtectedHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
