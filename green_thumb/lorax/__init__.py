from collections import deque
from green_thumb.common.db import get_db_scoped
from green_thumb.common.db.models import Plant
from green_thumb.lorax.hpi import llm
from green_thumb.lorax.proc import analyze
from green_thumb.common.db.models import Plant
from time import sleep as zzz
import subprocess

prompt = {"role": "system", "content": "You are a sentient plant. The user will tell you how you feel on a scale from 1 to 8, followed by the currrent problems you the plant are facing. Respond with a first-person remark about your care"}

interact_log = deque(maxlen=10) # Remembers te last 10 messages

def add_interaction(next_input: str):
    interact_log.append({"role": "user", "content": next_input})
    dialogs = [prompt, *interact_log]

    result = llm.create_chat_completion(
        messages = dialogs,
        max_tokens= 512 // (interact_log.maxlen + 1)
    )

    out = {"role": result['choices'][0]['message']["role"], "content": result['choices'][0]['message']["content"]}
    interact_log.append(out)

    return out['content']

def speak(text):
    print(f"Saying: {text}")
    subprocess.run(["spd-say", "-w", text])

PLANT_ID = 1
def e2e_interact():
    with get_db_scoped() as db:
        plant = db.query(Plant).get(PLANT_ID)

        p, problems  = analyze(plant)
    problem_string = ", ".join(problems)
    out = add_interaction(f"{p} {problem_string}")
    speak(out)

def main():
    print("Running Lorax...")
    while True:
        print("loraxxxxxx")
        e2e_interact()
        zzz(5)
