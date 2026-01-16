# gpt2_story_pro.py
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

print("=== GPT-2 Story Pro ===")

# Create the generator
generator = pipeline('text-generation', model='gpt2', device=-1)  # CPU

# User prompt
prompt = input("Enter the beginning of your story: ")

# User temperature
try:
    temperature = float(input("Enter creativity (0.0–1.0, default 0.7): "))
except:
    temperature = 0.7

# User max tokens
try:
    max_tokens = int(input("Enter max words to generate (default 100): "))
except:
    max_tokens = 100

# Generate story with top_k and top_p to reduce repetition
results = generator(
   prompt,
    max_new_tokens=100,   # slightly longer
    temperature=0.7,      # more creative
    top_k=50,
    top_p=0.95,
    do_sample=True
)

print("\n=== Generated Story ===\n")
print(results[0]['generated_text'])
print("\n=== End of Story ===")
