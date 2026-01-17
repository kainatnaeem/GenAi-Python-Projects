# temperature_experiment.py

from transformers import pipeline
print("started")
generator = pipeline("text-generation", model="gpt2")

prompt = "Once upon a time in a quiet village"

temperatures = [0.2, 0.7, 1.0]

for temp in temperatures:
    print(f"\n--- Temperature: {temp} ---\n")
    result = generator(
        prompt,
        max_new_tokens=60,
        temperature=temp,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )
    print(result[0]["generated_text"])
