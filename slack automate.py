import os
from datetime import datetime
import openpyxl
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler



BOTTKN  = "bot token"
APPTKN = "app token"
CHNLID = "codigo" 
FILEPATH = r"el path donde guardaste tu excel"

app = App(token=BOTTKN)



def get_user_name(user_id):
    user_names_cache = getattr(get_user_name, "cache", {})
    if user_id in user_names_cache:
        return user_names_cache[user_id]
    
    try:
        result = app.client.users_info(user=user_id)
        real_name = result["user"]["real_name"]
        
        user_names_cache[user_id] = real_name
        return real_name
    except Exception as e:
        print(f"Nombre no encontrado para {user_id}: {e}")
        return user_id  


def save_excel(user, text):
    try:
        wb = openpyxl.load_workbook(FILEPATH)
        ws = wb.active
        ws.append([datetime.now(), get_user_name(user), text])
        wb.save(FILEPATH)
        print(f"Guardado correctamente {get_user_name(user)}")
        
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
    SocketModeHandler(app, APPTKN).start()
