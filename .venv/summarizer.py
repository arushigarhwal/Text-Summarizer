# summarizer.py
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def summarize_text(text, max_input_len=1024, max_output_len=200):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=max_input_len, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_output_len, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
`