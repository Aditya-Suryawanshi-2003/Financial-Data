import yfinance # type: ignore
import datetime
def on_message(data):
    time = datetime.datetime.fromtimestamp(data['time']).strftime("%Y-%m-%d %H:%M:%S")
    print(f"Time: {time}, Data: {data}")

ws = yfinance.WebSocket()

ws.subscribe("ITC.NS")
ws.listen(on_message)

