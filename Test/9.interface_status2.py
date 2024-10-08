import random
import gradio as gr


def chat(message, history):
    history = history or []
    message = message.lower()
    if message.startswith("how many"):
        response = random.choice(["1", "10"])
    elif message.startswith("how"):
        response = random.choice(["Great", "Good", "Okay", "Bad"])
    elif message.startswith("where"):
        response = random.choice(["Here", "There", "Somewhere"])
    else:
        response = "I don't know"
    history.append((message, response))
    return history, history


#设置一个对话窗
chatbot = gr.Chatbot()
demo = gr.Interface(
    chat,
    # 添加state组件
    ["text", "state"],
    [chatbot, "state"],
    # 设置没有保存数据的按钮
    allow_flagging="never",
)
demo.launch()
