# `my_slide_config.py`

c.TagRemovePreprocessor.remove_input_tags.add("to_remove")
c.SlidesExporter.reveal_theme="simple"

# the following does the equivalent of --to slides
app_settings = {
    "export_format": "slides"
}
c.NbConvertApp.update(app_settings)

# the following does the equivalent of --no-prompt
exporter_settings = {
    'exclude_input_prompt' : True,
    'exclude_output_prompt' : True,
}
c.TemplateExporter.update(exporter_settings)