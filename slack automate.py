import os
from datetime import datetime
import openpyxl
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler



BOTTKN  = "xoxb-YOUR-BOT-TOKEN"
SLACKTKN = "xapp-YOUR-APP-TOKEN"
CHNLID = "C0XXXXXX" 
FILEPATH = r"path"


def save_excel(user, text):
    try:
        wb = openpyxl.load_workbook(FILEPATH)
        ws = wb.active
        ws.append([datetime.now(), user, text])
        wb.save(FILEPATH)
        print(f"Guardado correctamente {user}")
        
    except PermissionError:
        print("ERROR: Cierra el archivo de Excel antes de guardar.")
    except Exception as e:
        print(f"ERROR: {e}")


app = App(token=BOTTKN)

@app.event("message")
def handle_message(body, logger):
    event = body.get("event", {})
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text", "")

    
    if channel_id == CHNLID:
        save_excel(user_id, text)
    else:
        return

if __name__ == "__main__":
    print(f"Activo en el canal {CHNLID}")
    SocketModeHandler(app, SLACKTKN).start()
