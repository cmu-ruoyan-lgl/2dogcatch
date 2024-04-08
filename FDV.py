import websocket
import json

POOL_ID = 163398893

POOL_MESSAGE = {"command":"subscribe","identifier":"{\"channel\":\"PoolChannel\",\"pool_id\":\"163398893\"}"}
SWAP_MESSAGE = {"command":"subscribe","identifier":"{\"channel\":\"SwapChannel\",\"pool_id\":\"163398893\"}"}

def on_open(ws):
    print("WebSocket连接已打开")
    ws.send(json.dumps(POOL_MESSAGE))
    ws.send(json.dumps(SWAP_MESSAGE))

def on_message(ws, message):
    print("收到消息：", message)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket连接已关闭")
    print(close_status_code)
    printRed(close_msg)

def printRed(s):
    print('\033[31m' + str(s) + '\033[0m')

websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://cables.geckoterminal.com/cable",
                            on_open=on_open,
                            on_message=on_message,
                            on_close=on_close,
                            )

ws.run_forever(origin="https://www.geckoterminal.com")