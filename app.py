from bs4 import BeautifulSoup
import requests
import json

ozbargain_url = "https://www.ozbargain.com.au"
soup = BeautifulSoup(requests.get(ozbargain_url + "/freebies").text, "html.parser")

for item_node in soup.find_all("div", class_="node-ozbdeal"):
    json_dict = {
            "title": item_node.find("h2", class_="title").text,
            "submitted": item_node.find("div", class_="submitted").text,
            "url": ozbargain_url + item_node.find("h2", class_="title").find("a", href=True)["href"],
            "description": item_node.find("div", class_="content").text.strip("\n ")
    }

    print(json.dumps(json_dict))

