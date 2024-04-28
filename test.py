import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab(" "):
        gr.Image(label="Image for img2img", elem_id="img2img_image", show_label=False, source="webcam", interactive=True, type="pil", tool="editor", image_mode="RGBA").style(height=1000, width=1000)

demo.launch()