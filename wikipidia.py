import wikipedia
topic=input("Enter topic: \t\t")
print("="*34)
print("searching for your topic.......")
print("="*34)
print(f"\n The summary of your topic {topic} is : \t\t{wikipedia.summary(topic,sentences=5)}")