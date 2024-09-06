import gradio as gr


def increase(num):
    return num + 1


with gr.Blocks() as demo:
    a = gr.Number(label="a")
    b = gr.Number(label="b")
    # 要想b>a，则使得b = a+1
    atob = gr.Button("b > a")
    atob.click(increase, a, b)
    # 要想a>b，则使得a = b+1
    btoa = gr.Button("a > b")
    btoa.click(increase, b, a)
demo.launch()
