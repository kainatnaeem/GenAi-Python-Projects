from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = input("Enter poetry theme: ")

output = generator(
    f"Write a 4-line poem about {prompt}:",
    max_length=60,
    do_sample=True,
    temperature=0.8,
    top_k=50,
    top_p=0.95
)

print("\nGenerated Poem:\n")
print(output[0]["generated_text"])