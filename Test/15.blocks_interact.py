import gradio as gr
def greet(name):
    return 'Hello ' + name + "!"
with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    # 不可交互
    # output = gr.Textbox(label="Output Box")
    # 可交互
    output = gr.Textbox(label="Output", interactive=True)
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output)
demo.launch()