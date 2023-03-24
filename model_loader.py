from transformers import AutoTokenizer, AutoModel

model_name = "sentence-transformers/paraphrase-MiniLM-L6-v2"

# provider = "openai"
provider  = None

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
