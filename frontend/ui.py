import gradio as gr
from constants import *
from backend import get_response
import os

css_file_path = os.path.join(os.path.dirname(__file__), "style.css")
with open(css_file_path, "r") as f:
    css = f.read()


theme = gr.themes.Ocean(primary_hue="yellow", secondary_hue="orange")

with gr.Blocks(title="أبيات", css=css, theme=theme) as demo:

    gr.Markdown("# أبيات", elem_id="header_align")

    model = gr.Dropdown(available_models, label="النموذج اللغوي", value=available_models[1])

    with gr.Tab("التوليد"):
        with gr.Row(elem_id="row"):
            with gr.Column():
                generated_poem = gr.Textbox(label="القصيدة", lines=20, elem_id="label_align", text_align="right", rtl=True, show_copy_button=True)

            with gr.Column():
                with gr.Row():
                    context = gr.Textbox(label="سياق الموضوع", elem_id="label_align", text_align="right", rtl=True)
                    topic = gr.Dropdown(poem_topics, label="النوع", elem_classes="label_align", value=poem_topics[0])
                    

                bahr = gr.Dropdown(poem_bahrs, label="البحر", elem_id="label_align", value=poem_bahrs[0])
                qafia = gr.Dropdown(poem_qafias, label="حرف الروي", elem_id="label_align", value=poem_qafias[0])
                num_abyat = gr.Number(minimum=1, maximum=15, label="عدد الأبيات", elem_id="label_align", value=1)
                era = gr.Dropdown(poem_eras, label="العصر", elem_id="label_align", value=poem_eras[0])

                generate_btn = gr.Button("توليد القصيدة",variant="primary")
        
    with gr.Tab("التحليل"):
        poem_to_analyize = gr.Textbox(label="القصيدة", lines=10, elem_id="label_align", text_align="right", rtl=True)
        analyze_btn = gr.Button("تحليل القصيدة",variant="primary")
        poem_analyises = gr.Textbox(label="التحليل", lines=10, elem_id="label_align", text_align="right", rtl=True, show_copy_button=True)

    with gr.Tab("مواضيع متقدمة"):
        bayte = gr.Textbox(label="البيت", lines=1, elem_id="label_align", text_align="right", rtl=True)
        advanced_topics = ["العروض", "الإجازة"]
        with gr.Row():
            egaza_btn = gr.Button("أجزني", variant="primary")
            orwd_btn = gr.Button("تحليل البيت عروضيا", variant="primary")
        advanced_topic_results = gr.Textbox(label="النتيجة", lines=1, elem_id="label_align", text_align="right", rtl=True, show_copy_button=True)

    curr_choice = gr.State("")

    generate_btn.click(lambda: "generate", None, curr_choice).then(get_response, [context, topic, bahr, qafia, num_abyat, era, model, curr_choice], [generated_poem])
    analyze_btn.click(lambda: "analysis", None, curr_choice).then(get_response, [poem_to_analyize, model, curr_choice], [poem_analyises])
    egaza_btn.click(lambda: "egaza", None, curr_choice).then(get_response, [bayte, model, curr_choice], [advanced_topic_results])
    orwd_btn.click(lambda: "orwd", None, curr_choice).then(get_response, [bayte, model, curr_choice], [advanced_topic_results])
