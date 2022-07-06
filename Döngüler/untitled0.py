import websocket, json, pprint, talib, numpy
from binance.client import Client
from binance.enums import *

SOCKET ="wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

RSI_PERIOD =14
RSI_OVERBOUGHT =70
RSI_OVERSOLD = 30

TRADE_SYMBOL='ETHUSD'
TRADE_QUANTITY=0.01

closes =[]
in_position = False

def on_open(ws):
    print("oppened connection")
    
def on_close(ws):
    print("closed connection")

def on_message(ws,message):
    print("received message")
    json_message = json.loads(message)
    #print(json_message)
    # pprint.pprint(json_message)
    
    candle = json_message['k']
    close =candle['c']
    is_candle_closed = candle['x']
    
    if is_candle_closed:
        print("candle closed at : ",close)
    
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()