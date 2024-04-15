import spacy

# Khởi tạo mô hình spacy cho tiếng Anh
nlp = spacy.load("en_core_web_sm")

# Xử lý văn bản
text = "I have a cat"
doc = nlp(text)

# Hiển thị các token và thông tin liên quan
for token in doc:
    if token.pos_ in ["NOUN", "VERB"]:
        print(token.text)
