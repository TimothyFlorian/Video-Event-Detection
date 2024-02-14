import openai

openai.api_key = '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'

def generate_summary(sentences):
    unique_sentences = list(set(sentences))
    
    prompt = "Generate a summary based on the following sentences:\n" + "\n".join(unique_sentences) + "\nSummary:"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()

sentences = [
    "a lion running through a field of grass",
    "a lion running in a field with a zebra",
    "a lion and a zebra in a field",
    "a lion running in the grass with a dog",
    "a lion running in a field with zebras in the background",
    "a lion and a zebra in a field with a blurry background",
    "a lion walking through a field with zebras in the background",
    "a lion running across a field of grass",
    "a lion running in a field with a zebra in the background",
    "a lion running in the grass with a zebra in the background",
    "a lion and a zebra running in a field",
    "a lion chasing a zebra in a field",
    "a zebra chasing a lion in a field",
    "a lion and a zebra are running in the grass",
    "a zebra and a lion running in a field",
    "a bear in a field with a red circle",
    "a red background with a green dot and the words nature's great events",
    "a red background with a clock and the words nature's great events",
    "a red background with a red clock and the words nature's great events",
    "a red background with a white text that says nature's great events",
    "a red background with a white text that says nature's great events alone",
    "a red background with a white text that says nature's great events bbc one",
    "a red background with a white text that says nature's great events radio one",
    "a red background with a white text that says nature's great events radio one",
    "a red background with a white text that says nature's great events bbc one"
]

summary = generate_summary(sentences)
print(summary)
