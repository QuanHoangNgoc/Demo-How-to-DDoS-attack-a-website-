# import requests
# import time

# url = "http://localhost:8000"

# while True:
#     try:
#         response = requests.get(url)
#         print(f"Status Code: {response.status_code}, Response Time: {response.elapsed.total_seconds()} seconds")
#     except requests.RequestException as e:
#         print(f"An error occurred: {e}")
#     # time.sleep()  # Sleep for 1 second to avoid overwhelming the server

import socket
import threading

NUM_THREAD = 10**4
POW_LEN_DATA = 20


def flood(target_ip, target_port):
    while True:
        try:
            # Create a socket and send data
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(b'X'*(2**POW_LEN_DATA), (target_ip, target_port))
            # s.close()
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Localhost IP
    target_port = 8000
    for _ in range(NUM_THREAD):  # Number of threads
        t = threading.Thread(target=flood, args=(target_ip, target_port))
        t.start()
