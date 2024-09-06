import gradio as gr
with gr.Blocks() as demo:
    with gr.Row():
        img1 = gr.Image()
        text1 = gr.Text()
    btn1 = gr.Button("button")
demo.launch()