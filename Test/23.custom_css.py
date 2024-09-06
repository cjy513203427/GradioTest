import gradio as gr
#修改blocks的背景颜色
with gr.Blocks(css=".gradio-container {background-color: red}") as demo:
    box1 = gr.Textbox(value="Good Job")
    box2 = gr.Textbox(value="Failure")
demo.launch()