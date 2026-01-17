from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

generator = pipeline('text-generation', model='gpt2', device=-1)  
prompt = input("Enter story prompt: ")

for i in range(3):
    result = generator(
    prompt,
    max_new_tokens=100,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
    do_sample=True
)
    print(f"\nStory {i+1}:\n")
    print(result[0]["generated_text"])
