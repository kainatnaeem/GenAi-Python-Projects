from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = input("Enter theme for naat lyrics: ")

output = generator(
    f"Write a short naat about {prompt}:",
    max_length=100,
    do_sample=True,
    temperature=0.8,
    top_k=50,
    top_p=0.95
)

print("\nGenerated Song Lyrics:\n")
print(output[0]["generated_text"])
