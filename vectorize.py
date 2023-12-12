import re
import chromadb
import uuid

# reference : https://github.com/Govind-S-B/pdf-to-text-chroma-search

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

client = chromadb.PersistentClient(path="./db")
collection = client.create_collection(name="faq_data")

file_content = open("faq_test_data.txt").read()
data_list = batch_process_test_data(file_content)

documents_list = []
embeddings_list = []
ids_list = []

for data_chunk in data_list:
    documents_list.append(data_chunk)
    vector = model.encode(data_chunk)
    embeddings_list.append(vector)
    ids_list.append(str(uuid.uuid1()))

collection.add(
    embeddings=embeddings_list,
    documents=documents_list,
    ids=ids_list
)