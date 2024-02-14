from summarizer import Summarizer
model=Summarizer()


text = "a lion running through a field of grass. a lion running in a field with a zebra. a lion and a zebra in a field. a lion running in the grass with a dog. a lion running in a field with zebras in the background. a lion and a zebra in a field with a blurry background. a lion walking through a field with zebras in the background. a lion running across a field of grass. a lion running in a field with a zebra in the background. a lion running in the grass with a zebra in the background.a lion and a zebra running in a field. a lion chasing a zebra in a field. a zebra chasing a lion in a field. a lion and a zebra are running in the grass. a zebra and a lion running in a field. a red background with a green dot and the words nature's great events. a red background with a clock and the words nature's great events. a red background with a red clock and the words nature's great events."
summary=model(text)
print(summary)