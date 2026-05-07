import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://iotbusinessnews.com/page/{}/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

data = []
article_id = 1

for page in range(1, 80):

    url = base_url.format(page)

    try:

        response = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("h2")

        for article in articles:

            a_tag = article.find("a")

            if a_tag:

                title = a_tag.text.strip()
                link = a_tag["href"]

                data.append({
                    "id": article_id,
                    "title": title,
                    "link": link,
                    "topic": "IoT"
                })

                article_id += 1

        print("page scraped:", page)

        time.sleep(1)

    except requests.exceptions.RequestException:
        print("failed page:", page)
        continue


df = pd.DataFrame(data)

df.to_csv("iot_dataset.csv", sep=";", index=False, encoding="utf-8")

print("Total rows:", len(df))