import gradio as gr


def greet(name):
    return "Hello " + name + "!"


demo = gr.Interface(
    fn=greet,
    # 自定义输入框
    # 具体设置方法查看官方文档
    inputs=gr.Textbox(lines=3, placeholder="Name Here...", label="my input"),
    outputs="text",
)
demo.launch()
