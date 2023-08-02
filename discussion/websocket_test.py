import websocket

def on_message(ws, message):
    print(f"Received message: {message}")

def on_open(ws):
    print("WebSocket connection established")
    ws.send("Hello, WebSocket!")

def on_close(ws):
    print("WebSocket connection closed")

# WebSocket URL
websocket_url = "ws://65.0.94.158:8000/ws/chat/room1/"

# Create WebSocket instance
ws = websocket.WebSocketApp(websocket_url,
                            on_message=on_message,
                            on_open=on_open,
                            on_close=on_close)

# Start WebSocket connection
ws.run_forever()

