from llama_cpp import Llama

MODEL_PATH = "./llama-2-7b-chat.Q4_0.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    chat_format="llama-2"
)
