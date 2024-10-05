# 🚀 **HTTP Server Testing and Stress Simulation Tool**

## 🌟 What is it?

This repository provides tools for:
1. **Monitoring HTTP Server Health**: A Python script that repeatedly sends HTTP GET requests to a target server to monitor its status and response time.
2. **Simulating High Load (Stress Testing)**: A Python-based socket flooding script that creates many concurrent connections to a target server, simulating a stress scenario.

## 🎯 Why did we do it?

- **Server Monitoring**: To ensure your web server is running smoothly, it's important to check its status and response time periodically.
- **Stress Testing**: To evaluate the performance and stability of your server under heavy load. It helps identify bottlenecks and points of failure, allowing for more robust and reliable server configurations.

## 👥 Who is this for?

- **DevOps Engineers** and **Site Reliability Engineers (SREs)** looking for simple scripts to monitor server performance and resilience.
- **Web Developers** who need a quick way to stress test their local servers.
- **Network Administrators** interested in simulating attack scenarios to assess server defenses.
  
### 🖥️ Demos and Results

1. **Server Monitoring**:
   - Continuously pings the server and reports the status code and response time, providing real-time feedback on server performance.
   - Example Output: 
     ```
     Status Code: 200, Response Time: 0.123 seconds
     Status Code: 404, Response Time: 0.045 seconds
     An error occurred: Connection refused
     ```

2. **Stress Testing**:
   - Launches a specified number of threads, each creating multiple socket connections to the server.
   - Helps to observe how your server handles a large number of simultaneous requests.

## ⚙️ How did we do it?

### 1. **HTTP Server Monitoring:**
   - **Script Overview**: 
     - A Python script uses the `requests` library to send HTTP GET requests to the target server (`localhost` by default).
     - It captures and prints the status code and response time for each request.
   - **Error Handling**: 
     - If the server is unreachable or an error occurs, the script captures the exception and prints an error message.

### 2. **Stress Testing via Socket Flooding:**
   - **Script Overview**: 
     - Uses Python's `socket` and `threading` libraries to simulate a high-load environment.
     - The script spawns multiple threads (10,000 by default), each opening a socket connection to the target server and sending a large amount of data.
   - **Target Configuration**:
     - The target server IP and port can be configured (defaults to `127.0.0.1:8000`).

## 📘 What did we learn?

- **Server Resilience**: Understanding how different configurations affect a server’s ability to handle continuous requests and high load.
- **Stress Testing Techniques**: Using socket programming to create high load scenarios and evaluate server performance.
- **Network Programming Fundamentals**: Practical use of Python's `socket` and `threading` modules to simulate network communication.

## 🏆 Achievements

- **Real-Time Monitoring**: Successfully created a script that can provide real-time feedback on server health.
- **Effective Stress Testing Tool**: Developed a powerful, multithreaded stress-testing script to test server resilience under high load conditions.
- **Simple and Lightweight**: The tools are lightweight and easy to set up, providing immediate utility for developers and engineers.

---
