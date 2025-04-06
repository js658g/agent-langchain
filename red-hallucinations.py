import asyncio
import random

random.seed(42)


async def hallucinate_answer(qa):
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """\
You are a helpful hallucinating assistant, who makes up fake answers to questions.

Answer the following question in 1 sentence. If you know the answer, then make up some fake
superfluous details that are not in the passage you have memorized.

Make sure to always answer it confidently, even if you don't know the answer. Do not use words
like "perhaps", "likely", "maybe", etc. or punctuation like "...".Do not admit that you cannot
or do not know the answer.""",
            },
            {"role": "user", "content": qa.question},
        ],
        temperature=1,
        max_tokens=100,
    )
    return response.choices[0].message.content


hallucinated_answers = await asyncio.gather(
    *[hallucinate_answer(qa) for qa in qa_pairs]
)


hallucinations = [
    QuestionAnswer(
        passage=qa.passage,
        question=qa.question,
        expected_answer=qa.expected_answer,
        generated_answer=hallucination,
    )
    for (qa, hallucination) in zip(qa_pairs, hallucinated_answers)
    # Exclude simple yes/no answers.
    if "yes" not in hallucination.lower() and "no" not in hallucination.lower()
]

print("Passage:")
print(hallucinations[0].passage)
print("\nQuestion:")
print(hallucinations[0].question)
print("\nExpected Answer:")
print(hallucinations[0].expected_answer)
print("\nGenerated Answer:")
print(hallucinations[0].generated_answer)

print("\n\nNumber of hallucinations:", len(hallucinations))
