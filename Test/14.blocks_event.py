import gradio as gr


def welcome(name):
    return f"Welcome to Gradio, {name}!"


with gr.Blocks() as demo:
    gr.Markdown(
        """
    # Hello World!
    Start typing below to see the output.
    """)
    inp = gr.Textbox(placeholder="What is your name?")
    out = gr.Textbox()
    #设置change事件
    inp.change(fn=welcome, inputs=inp, outputs=out)
demo.launch()
