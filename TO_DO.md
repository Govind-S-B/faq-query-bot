- persistent storage
- write db and read db , modularized to seperate functions
- setup seperate file with functions for test write and read operation in bulk
- setup api server with read and write endpoints

reference : https://realpython.com/chromadb-vector-database/

Mock data generation prompt :

You are a mock data generation specialized model. 
I have a set of FAQs as examples given below
Make different distinct question answer pairs

== START ==

<insert faq_test_data 5 entries here>

== END ==

Generate 10 Such FAQs , each contained within ```