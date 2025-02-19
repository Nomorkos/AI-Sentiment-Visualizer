import matplotlib.pyplot as plt
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

if __name__ == "__main__":
    texts = []
    sentiments = []
    n = int(input("How many texts do you want to analyze? "))
    for i in range(n):
        text = input(f"Enter text {i+1}: ")
        texts.append(text)
        sentiments.append(analyze_sentiment(text))
    
    plt.bar(range(n), sentiments, color='skyblue')
    plt.xticks(range(n), [f"Text {i+1}" for i in range(n)])
    plt.ylabel("Sentiment Polarity")
    plt.title("Sentiment Analysis Visualization")
    plt.show()
