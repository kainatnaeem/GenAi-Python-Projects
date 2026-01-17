# story_saver_gpt2.py
# MIT License – see LICENSE file

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = input("Enter story prompt: ")

result = generator(
    prompt,
    max_new_tokens=100,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
    do_sample=True
)

story = result[0]["generated_text"]

with open("generated_story.txt", "w", encoding="utf-8") as file:
    file.write(story)

print("\nStory saved to generated_story.txt")
