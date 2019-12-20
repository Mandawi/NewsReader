import requests
import json

def headline_print(sources):
    """ go through every news source, apply model, get json, parse json, extract headlines and print them

    Arguments:
        sources {dictionary} -- includes the websites as keys and the links to their US news pages as values
    """
    for key in sources.keys():
        # RFE: Stop model from occasionally returning headline image links instead of texts 
        params = {
            'api_key': "1fc24350-2367-11ea-ba09-0d75f508bf15",
            'url': sources[key],
            'model_id': "Kb5ZKF13"
        }
        # CRED: https://dashblock.com/
        response = requests.get(
            'https://api.dashblock.io/model/v1', params=params)
        json_data = response.text
        json_parsed = json.loads(json_data)
        if json_parsed['entities'] == None:
            continue
        print(f"News by {key}")
        # FIXME: Prints number of headline incorrectly when there are different types of headlines for the same source
        for number, video in enumerate(json_parsed['entities'][:5]):
            if isinstance(video['headline'], list):
                for num, headlines in enumerate(video['headline'][:5]):
                    print(f"{num+1}. {headlines}")
            else:
                print(f"{number+1}. {video['headline']}")
        print("\n")

if __name__ == "__main__":
    news_sources = {'Google': "https://news.google.com/?hl=en-US&gl=US&ceid=US:en", 'CNN': "https://www.cnn.com/", 'Reuters': "https://www.reuters.com/news/us", 'Fox': "https://www.foxnews.com/us",
                    'ABC': "https://abcnews.go.com/", 'Forbes': "https://www.forbes.com/news/#2b1705b73690", 'Yahoo': "https://news.yahoo.com/", 'BBC': "https://www.bbc.com/news//world"}
    print("Please wait...")
    headline_print(news_sources)
