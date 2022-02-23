import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def main():
    url = 'https://news.ycombinator.com/item?id=30164271'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="ind", indent=0)
    comments = [e.find_next(class_="comment") for e in elements]  # iterate through each element that has indent=0 or
    # in other words the top level comments
    keywords = {"python": 0,
                "c++": 0,
                "azure": 0,
                "aws": 0,
                "javascript": 0,
                "typescript": 0,
                "react": 0.,
                "c#": 0,
                "mongodb": 0,
                "express": 0,
                "angular" :0,
                "vue": 0,
                "ruby": 0
                }

    for comment in comments:
        comment_text = comment.get_text().lower()
        words = comment_text.split(" ")  # split comments into words
        words = {w.strip(".,/:!@()|-=$%") for w in words}

        for k in keywords:
            if k in words:
                keywords[k] += 1
    print(keywords)
    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel("Language/Technology")
    plt.ylabel("Number of Mentions")


if __name__ == "__main__":
    main()
