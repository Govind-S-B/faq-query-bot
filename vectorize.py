import re
import chromadb

# embeddings = HuggingFaceEmbeddings(model_name="infgrad/stella-base-en-v2")

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('infgrad/stella-base-en-v2')

def vectorize_sentence(string):
    pass

def batch_process_test_data(document):
    # Find all content within the backticks
    content = re.findall(r'```(.*?)```', document, re.DOTALL)
    
    # Remove leading and trailing whitespace from each content block
    content = [block.strip() for block in content]
    
    return content

file_content = open("faq_test_data.txt").read()
elem = (batch_process_test_data(file_content))

for i in elem:
    print("---")
    print(i)
    print("---")

vector = model.encode(elem[0])
print(vector)
print(elem[0])

