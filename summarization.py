from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer
model_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Sample input text
text = """
Transformers have revolutionized natural language processing by introducing
attention mechanisms that allow models to understand relationships between
words regardless of distance. Unlike traditional RNNs and LSTMs, Transformers
process tokens in parallel, making training faster and more efficient.
"""

# Tokenize input
inputs = tokenizer(
    text,
    return_tensors="pt",
    max_length=512,
    truncation=True
)

# Generate summary
summary_ids = model.generate(
    inputs["input_ids"],
    max_length=50,
    min_length=10,
    num_beams=4,
    early_stopping=True
)

# Decode summary
summary = tokenizer.decode(
    summary_ids[0],
    skip_special_tokens=True
)

print("INPUT TEXT:")
print(text)

print("\nGENERATED SUMMARY:")
print(summary)
