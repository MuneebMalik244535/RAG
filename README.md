# RAG

Deep concept of RAG with projects

## What is RAG?

### You feed data to your LLM without retraining it

## Example:

If your company has over 5000 PDFs and the user just wants to know about your refund policy, a normal LLM doesn't know about your refund policy. In that case, how will RAG solve this problem?

### RAG will find relevant text from PDFs and give it to the LLM, and the LLM will generate an answer.

## Let's see how it works:

```text
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
```

### Now let's understand each step and come to know how it works and what its uses are.

# 1.Chunking

Break the document into small pieces.

### Example PDF:

```text
Page 1:
Company Refund Policy

Page 2:
Customer can return product within 30 days

Page 3:
Refund will be processed in 7 days
```

### Let's see how it will be chunked

```python
chunk1 = "Company Refund Policy"
chunk2 = "Customer can return product within 30 days"
chunk3 = "Refund will be processed in 7 days"
```

### Semantic Chunking

Split on the basis of sentence meaning.

### Pros...

It will separate each and every topic and it is used in production systems.

# 2.Embeddings

Before starting this topic, you should know something.

LLMs don't understand text; they understand numbers. So embeddings convert the text into vectors (numbers), and then the LLM understands it.

### Example:

If I send the word "Cat" to the LLM, how will the process work?

The word "Cat" will be converted into vectors (numbers). It will look like this:

```python
[0.23, -0.91, 0.44, ...]
```

# Similar Meaning

**Cat**
**Kitten**

Their vectors will be close to each other because they have similar meanings.

---

**Cat**
**Airplane**

Their vectors will be far apart because their meanings are very different.

---

This is the reason why semantic search is possible. Similar concepts have nearby vector representations, while unrelated concepts are located farther away in the vector space.

## Embedding Models

### Popular:

* BGE
* E5
* GTE
* OpenAI text-embedding-3-large
* Voyage AI

Nowadays BGE and E5 are used a lot.

### Now we have got understand about Vector and Embedding and how its work 
Lets Deep dive where will embedding be the stored ? 

## Database vs Vector Database

### Normal Database

```sql
SELECT *
FROM users
```

A normal database finds exact matches based on structured data such as IDs, names, emails, dates, and other predefined fields.

# 3.Vector Database

```text
Find similar vectors
```

A vector database does not search for exact text matches. Instead, it searches for vectors that are semantically similar to the query vector.

### Example

Query:

```text
What is your return policy?
```

Even if the document contains:

```text
Customers can return products within 30 days.
```

A vector database can retrieve it because the meanings are similar, even though the words are different.

### Key Difference

| Normal Database        | Vector Database        |
| ---------------------- | ---------------------- |
| Exact matching         | Semantic similarity    |
| Structured data        | Embeddings (vectors)   |
| SQL queries            | Similarity search      |
| Finds identical values | Finds related meanings |

### Popular Vector DBs:

* Pinecone
* Qdrant
* Weaviate
* Milvus
* Chroma

## Similarity Search

### User Query

```text
How can I get a refund?
```

The query will first be converted into an embedding (vector).

```text
How can I get a refund?
        ↓
    Embedding
        ↓
[0.12, -0.45, 0.88, ...]
```

The Vector Database will then search for the most similar vectors.

### Nearest Chunks Retrieved

1. Refund Policy
2. Return Policy
3. Cancellation Policy

Even if the exact words **"How can I get a refund?"** are not present in the documents, the Vector Database can still retrieve relevant chunks because it searches based on semantic similarity rather than exact keyword matching.

# 4. Retrieval

Now we need to retrieve the relevant chunks from the Vector Database.

### Example

```python
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)
```

### User Query

```text
How to request a refund?
```

### Retriever Output

```text
Top 5 relevant chunks
```

The retriever searches the Vector Database and returns the most relevant chunks based on the user's query.

---

## Retrieval Strategies

### 1. Dense Retrieval

Uses embeddings (vectors) for searching.

```text
Query
   ↓
Embedding
   ↓
Vector Search
   ↓
Relevant Chunks
```

### Pros

* Understands semantic meaning
* Can find related information even when exact words are different
* Most commonly used in RAG systems

---

### 2. Sparse Retrieval

Uses keyword-based search.

### Example

```text
refund
```

The system searches for the exact word **"refund"** inside the documents.

### Popular Algorithm

```text
BM25
```

### Pros

* Fast
* Works well when exact keywords are important

---

### 3. Hybrid Retrieval

Combines Dense Retrieval and Sparse Retrieval.

```text
Vector Search
      +
BM25 Search
      ↓
Better Results
```

### Why Use Hybrid Retrieval?

Dense Retrieval understands meaning, while Sparse Retrieval captures exact keywords.

By combining both approaches, the system achieves better accuracy and recall.

### Industry Usage

Hybrid Retrieval is widely used in production RAG systems because it often provides the best balance between semantic understanding and keyword matching.
  
# 5. Re-ranking

This is something that many beginners miss.

Vector search is not perfect. It retrieves relevant chunks, but sometimes the ranking is not optimal.

### Example

#### User Query

```text
How to request a refund?
```

#### Retrieved Chunks

```text
1. Refund Policy
2. Company History
3. Refund Processing
4. CEO Message
```

Although all retrieved chunks may be somewhat related, the order is not ideal.

### After Re-ranking

```text
1. Refund Policy
2. Refund Processing
3. Company History
4. CEO Message
```

The most relevant chunks are moved to the top.

---

## Cross Encoder

The most common re-ranking technique.

### Example

```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder(
    "BAAI/bge-reranker-base"
)
```

A Cross Encoder evaluates each:

```text
(Query, Chunk)
```

pair and assigns a relevance score.

### Example

#### Query

```text
How to request a refund?
```

#### Chunk

```text
Refund requests can be submitted through the support portal.
```

#### Score

```text
0.98
```

A higher score indicates higher relevance.

---

## Why Re-ranking Matters

Without re-ranking:

```text
Vector Search
     ↓
Top K Chunks
```

With re-ranking:

```text
Vector Search
     ↓
Top K Chunks
     ↓
Re-ranker
     ↓
Best Chunks First
```

This significantly improves answer quality because the LLM receives the most relevant context at the top.

---

# Production RAG Architecture

Expert-level companies usually follow a pipeline like this:

```text
Documents
    ↓
Cleaning
    ↓
Chunking
    ↓
Embedding
    ↓
Qdrant
    ↓
Hybrid Search
    ↓
Re-ranking
    ↓
Context Compression
    ↓
Prompt Construction
    ↓
GPT / Claude
    ↓
Final Answer
```

## Explanation

### Cleaning

Removes unnecessary content such as headers, footers, duplicate text, and formatting noise.

### Chunking

Splits documents into smaller, meaningful sections.

### Embedding

Converts text into vectors for semantic search.

### Qdrant

Stores vectors and enables efficient similarity search.

### Hybrid Search

Combines:

```text
Dense Retrieval
      +
Sparse Retrieval (BM25)
```

to improve retrieval quality.

### Re-ranking

Reorders retrieved chunks based on relevance.

### Context Compression

Removes redundant or low-value information so that only the most useful context is sent to the LLM.

### Prompt Construction

Builds the final prompt by combining:

* User Query
* Retrieved Context
* Instructions

### GPT / Claude

The LLM generates the final answer using the provided context.
  
