import wikipedia
topic=input("Enter your topic :  \t")
print()
print(wikipedia.summary(topic , sentences=3))