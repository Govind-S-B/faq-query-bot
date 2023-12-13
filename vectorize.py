from uuid import uuid1
import re
import chromadb
from chromadb.utils import embedding_functions

def batch_process_test_data(document):
    # Find all content within the backticks
    content = re.findall(r'```(.*?)```', document, re.DOTALL)
    
    # Remove leading and trailing whitespace from each content block
    content = [block.strip() for block in content]
    
    return content

# DB INIT

client = chromadb.EphemeralClient()
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="infgrad/stella-base-en-v2",)
collection = client.get_or_create_collection(name="faq", embedding_function=embedding_func)

# WRITE SECTION

file_content = open("faq_test_data.txt").read()
data_list = batch_process_test_data(file_content)

documents_list = data_list
ids_list = [str(uuid1()) for i in range(0,len(data_list))]

collection.add(
            ids=ids_list,
            documents=documents_list,
        )


# READ SECTION

query_qn = "i am stuck in my level"

fetched_doc = collection.query(
     query_texts=query_qn,
     n_results=1,
     include=["documents"]
 )["documents"][0][0]

print(fetched_doc)