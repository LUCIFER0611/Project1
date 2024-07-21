import openai

openai.api_key = sk-proj-erYzibAcRw0eWXSfsuJET3BlbkFJbwlfsEwRWNVHxX0sZvAi

def get_answer_from_llm(context, question):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Context: {context}\n\nQuestion: {question}\n\nAnswer:",
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    return answer

# Example Usage
context = " ".join([doc for score, doc in ranked_docs[:5]])  # Combine top 5 documents
question = "What is machine learning?"
answer = get_answer_from_llm(context, question)
