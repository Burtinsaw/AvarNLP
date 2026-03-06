"""Gradio demo for AvarNLP translation."""

import gradio as gr


def translate(text: str, direction: str) -> str:
    """Translate text. Placeholder until model is trained."""
    if not text.strip():
        return ""
    # Will load real model here
    return f"[AvarNLP v0.1 — model training in progress]\nInput: {text}\nDirection: {direction}"


demo = gr.Interface(
    fn=translate,
    inputs=[
        gr.Textbox(label="Metin / Text", placeholder="Салам алейкум!", lines=3),
        gr.Radio(
            choices=["Avarca -> Turkce", "Turkce -> Avarca"],
            label="Ceviri Yonu / Direction",
            value="Avarca -> Turkce",
        ),
    ],
    outputs=gr.Textbox(label="Ceviri / Translation", lines=3),
    title="AvarNLP — Avarca Ceviri",
    description="Dunyada ilk Avarca AI ceviri motoru. Genetik algoritma ile kendini evrimlestiren model.",
    examples=[
        ["Салам алейкум!", "Avarca -> Turkce"],
        ["Дир эбел цIуяб нуж йиго", "Avarca -> Turkce"],
        ["Merhaba, nasilsin?", "Turkce -> Avarca"],
    ],
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch()
