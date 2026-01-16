
# Description: This is a beginner-friendly Python program to generate text
# using a pre-trained GPT-2 AI model from Hugging Face.

#transformers → lets you use pre-trained AI models
#torch → backend library needed for AI
print("Script started")

# Step 1: Import the AI pipeline from transformers
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

# Step 2: Create a text generator using GPT-2 model
generator = pipeline('text-generation', model='gpt2',device=-1)

# Step 3: Define the starting sentence for AI
prompt = input("Enter your prompt: ")

# Step 4: Generate AI text based on the prompt
# max_length = max words/tokens AI can write
# num_return_sequences = how many versions of text you want
results = generator(prompt, max_new_tokens=100)
print("\nGenerated Text:\n")
# Step 5: Print the AI generated text
print(results[0]['generated_text'])