# RAG
Deep concept of RAG with projects
## What is RAG ? 
### You feed data to your llm wihtout retrain it 
## Example : 
If your company has over 5000 PDF and user just want to know about your refund policy so normal llm doesnt know about your refund policy in case How will RAG solve this problem 
### RAG will find relevant text from PDF and give to LLM and LLM will generate answer 
## Lets see how will it work : 

Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retrieval
    ↓
Re-ranking
    ↓
Prompt Construction
    ↓
   LLM
    ↓
  Answer

  ### Now lets understand each step and come to know how it work and what its uses ? 
  ## Chunking 
  Break the document into small pieces 
  ### Examples PDF : 

Page 1:
Company Refund Policy

Page 2:
Customer can return product within 30 days

Page 3:
Refund will be processed in 7 days
### Lets see how it will be chunked 
```
chunk1 = "Company Refund Policy"
chunk2 = "Customer can return product within 30 days"
chunk3 = "Refund will be processed in 7 days"
```
### Semantic Chunking 
Split on the basis of sentence meaning 
### Pros ...
It will separate each and every topic and it is used in production system 

## Embeddings 
Before start learning this topic you should know about something 
LLM does'nt understand text it understand numbers so the Embedding convert the text into Vectors(numbers) and then LLM understand it 
### Example : If i text the word Cat to the LLM so how will be the process 

