import requests
import pprint
import json

news_sources={'Google':"https://news.google.com/?hl=en-US&gl=US&ceid=US:en",'CNN':"https://www.cnn.com/",'Reuters':"https://www.reuters.com/news/us",'Fox':"https://www.foxnews.com/us",'ABC':"https://abcnews.go.com/",'Forbes':"https://www.forbes.com/news/#2b1705b73690",'Yahoo':"https://news.yahoo.com/",'BBC':"https://www.bbc.com/news//world"}

for key in news_sources.keys(): 
    params = {
        'api_key': "1fc24350-2367-11ea-ba09-0d75f508bf15",
        'url': news_sources[key],
        'model_id': "Kb5ZKF13"
    }
    response = requests.get('https://api.dashblock.io/model/v1', params=params)
    json_data = response.text
    json_parsed = json.loads(json_data)
    if json_parsed['entities']==None:
        continue
    print(f"News by {key}")
    for number, video in enumerate(json_parsed['entities'][:5]):
        if isinstance(video['headline'],list):
            for num, headlines in enumerate(video['headline'][:5]):
                print(f"{num+1}. {headlines}")
        else:
            print(f"{number+1}. {video['headline']}")
    print("\n")