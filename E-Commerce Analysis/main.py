import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_Name = []
Price = []
Description = []
Product_Rating = []




for i in range(2,20):

    url = "https://www.flipkart.com/search?q=Mobiles+Under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+ str(i)


    r = requests.get(url)
    #print(r)
    soup = BeautifulSoup(r.text, "lxml")
    #print(soup)
    box = soup.find("div", class_="DOjaWF gdgoEp")

    Names = box.find_all("div",class_="KzDlHZ")

    for i in Names:
        name = i.text
        Product_Name.append(name)

    prices = box.find_all("div",class_= "Nx9bqj _4b5DiR")

    for i in prices:
        name = i.text
        Price.append(name)

    desc = box.find_all("div", class_= "_6NESgJ")

    for i in desc:
        name = i.text
        Description.append(name)

    rating = box.find_all("div",class_ = "XQDdHH")

    for i in rating:
        name =i.text
        Product_Rating.append(name)

    
    
#df = pd.DataFrame({"Product_Name":Product_Name,"Price":Price,"Description":Description,"Product_Rating":Product_Rating,"Reviews":Reviews})

a = {"Product_Name":Product_Name,"Price":Price,"Description":Description,"Product_Rating":Product_Rating}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()


df.to_csv("Flipkart_50.csv")























    
    # np = soup.find("a",class_ = "_9QVEpD").get("href")
    # C = "https://www.flipkart.com" + np
    # print(C)

    # url = C
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text, "lxml")
