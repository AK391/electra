import gradio as gr

description = "demo for Electra. To use it, simply add your text, or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2003.10555'>ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators</a> | <a href='https://github.com/google-research/electra'>Github Repo</a></p>"



gr.Interface.load("huggingface/google/electra-small-generator", description=description, article=article, examples=[
["Paris is the [MASK] of France."]] ).launch()
