from transformers import pipeline
translation=pipeline("translation_en_to_fr",model="t5-base",tokenizer="t5-base")
text="I am an Indian"
output_text=translation(text,max_length=40)[0]["translation_text"]
print(output_text)