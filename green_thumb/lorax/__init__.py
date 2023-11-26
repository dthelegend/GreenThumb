from collections import deque

from sqlalchemy import values
from green_thumb.common.db import get_db_scoped
from green_thumb.common.db import models
from green_thumb.common.db.models import Plant
from green_thumb.lorax.hpi import llm
from green_thumb.lorax.proc import analyze
from green_thumb.common.db.models import Plant
from time import sleep as zzz
import subprocess
import green_thumb.lorax.emotion

prompt = {"role": "system", "content": "You are a sentient plant. The user will tell you how you feel on a scale from 1 to 8, followed by the currrent problems you the plant are facing. Respond with a first-person remark about your care"}

interact_log = deque(maxlen=10) # Remembers te last 10 messages

def add_interaction(next_input: str):
    interact_log.append({"role": "user", "content": next_input})
    dialogs = [prompt, *interact_log]

    print("Generating guy")
    result = llm.create_chat_completion(
        messages = dialogs,
        max_tokens= 512 // (interact_log.maxlen + 1)
    )
    print("Guy generated")

    out = {"role": result['choices'][0]['message']["role"], "content": result['choices'][0]['message']["content"]}
    interact_log.append(out)

    return out['content']

def speak(severity, text):
    print(f"Saying: {text}")
    # subprocess.run(["spd-say", "-w", text])

PLANT_ID = 1
def e2e_interact(should_speak: bool):
    values = green_thumb.lorax.emotion.recv_message()
    if values is None:
        return
    print(values)
    with get_db_scoped() as db:
        x = models.PlantDataPoint(plant_id= PLANT_ID, **values)
        db.add(x)
        db.commit()
        
        severity, problems  = analyze(db.query(Plant).get(PLANT_ID))
    problem_string = ", ".join(problems)

    if should_speak:
        out = add_interaction(f"{severity} {problem_string}")
        speak(severity, out)
        green_thumb.lorax.emotion.send_message(severity, out)

def main():
    print("Running Lorax...")
    i = 0
    while True:
        print("loraxxxxxx")
        i %= 100
        e2e_interact(i == 0)
        zzz(5)
        i += 1
