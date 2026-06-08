from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Input text
text = "Artificial Intelligence is transforming the world."

# Tokenize
inputs = tokenizer(
    text,
    return_tensors="pt"
)

# Generate translation
translated_tokens = model.generate(**inputs)

# Decode translation
translation = tokenizer.decode(
    translated_tokens[0],
    skip_special_tokens=True
)

print("INPUT:")
print(text)

print("\nFRENCH TRANSLATION:")
print(translation)
