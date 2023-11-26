from collections import deque
from green_thumb.db.models import Plant
from green_thumb.lorax.hpi import llm
from green_thumb.lorax.proc import analyze
from green_thumb import db
from sqlalchemy.orm import scoped_session
import subprocess

prompt = {"role": "system", "content": "You are a sentient plant. The user will tell you how you feel on a scale from 1 to 8, followed by the currrent problems you the plant are facing. Respond with a first-person remark about your care"}

interact_log = deque(maxlen=10) # Remembers te last 10 messages

def add_interaction(next_input: str):
    interact_log.append({"role": "user", "content": next_input})
    dialogs = [prompt, *interact_log]

    [result] = llm.create_chat_completion(
        messages = dialogs
    )
    interact_log.append(result['generation'])

    return result['generation']["content"]

def speak(text):
    subprocess.run(["spd-say", text])

PLANT_ID = 1
def e2e_interact():
    with db.get_db_scoped() as db:
        plant = db.query(Plant).get(PLANT_ID)
    p, problems  = analyze(plant)
    problem_string = ", ".join(problems)
    out = add_interaction(f"{p} {problem_string}")
    add_interaction(out)

