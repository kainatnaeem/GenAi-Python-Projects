from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

topic = input("Enter topic for joke or fun fact: ")

prompt = f"Tell a funny joke about {topic}:"

output = generator(
    prompt,
    max_length=50,
    do_sample=True,
    temperature=0.9,
    top_k=40
)

print("\nGenerated Joke/Fun Fact:\n")
print(output[0]["generated_text"])
