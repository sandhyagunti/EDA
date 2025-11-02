import gradio as gr

def square_numbers(x):
    return x ** 2

interface = gr.Interface(
    fn=square_numbers,
    inputs="number",   # ✅ use "number" not "numbers"
    outputs="number"
)

interface.launch()
