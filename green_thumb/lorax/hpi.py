from llama import Llama, Dialog

CKPT_DIR = "./llama/llama-2-13b-chat"
TOKENIZER_PATH = "./llama"

generator = Llama.build(
    ckpt_dir=CKPT_DIR,
    tokenizer_path=TOKENIZER_PATH,
    max_seq_len=512,
    max_batch_size=4,
)

def generate():
    results = generator.chat_completion(
        dialogs,  # type: ignore
        max_gen_len=None,
        temperature=0.6,
        top_p=0.9,
    )

    return results[0]['generation']['content']
