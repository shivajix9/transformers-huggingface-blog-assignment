# Understanding Transformers and Hugging Face

## Project Overview

This repository contains the implementation of NLP tasks using Hugging Face Transformers as part of the curriculum tasks assigned by Innomatics Research Labs.

The project demonstrates:

- Transformer Architecture concepts
- Text Summarization using a pretrained Transformer model
- Language Translation using a pretrained Transformer model
- Practical usage of Hugging Face AutoClasses

---

## Tasks Implemented

### Task 1: Text Summarization

**Model Used:** facebook/bart-large-cnn

This script generates concise summaries from long text passages using a pretrained Transformer model.

File:
```
summarization.py
```

---

### Task 2: Language Translation

**Model Used:** Helsinki-NLP/opus-mt-en-fr

This script translates English text into French using a pretrained Transformer model.

File:
```
translation.py
```

---

## Project Structure

```
transformers-huggingface-blog-assignment/
│
├── summarization.py
├── translation.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/shivajix9/transformers-huggingface-blog-assignment.git
cd transformers-huggingface-blog-assignment
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Text Summarization

```bash
python summarization.py
```

---

## Running Language Translation

```bash
python translation.py
```

---

## Requirements

- Python 3.9+
- transformers
- torch
- sentencepiece
- accelerate

---

## Blog Link

Medium Article:

https://medium.com/@shivajix9/understanding-transformers-and-hugging-face-a-complete-guide-to-modern-nlp-063bcc46dd38

---

## Author

Shivaji

---

## References

1. Attention Is All You Need (Vaswani et al., 2017)
2. Hugging Face Documentation
3. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
4. BART: Denoising Sequence-to-Sequence Pre-training
5. Hugging Face Model Hub
