from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Create a character name and description:"

output = generator(
    prompt,
    max_length=40,
    do_sample=True,
    temperature=0.9,
    top_k=50
)

print("\nGenerated Character:\n")
print(output[0]["generated_text"])
