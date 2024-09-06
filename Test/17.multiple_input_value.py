import gradio as gr

with gr.Blocks() as demo:
    food_box = gr.Number(value=10, label="Food Count")
    status_box = gr.Textbox()


    def eat(food):
        if food > 0:
            return food - 1, "full"
        else:
            return 0, "hungry"


    gr.Button("EAT").click(
        fn=eat,
        inputs=food_box,
        #根据返回值改变输入组件和输出组件
        outputs=[food_box, status_box]
    )
demo.launch()
