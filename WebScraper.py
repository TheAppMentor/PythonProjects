from bs4 import BeautifulSoup
import requests
import time
import lxml
import json
import CSVWriter

class Scraper():

    fileWriter = CSVWriter.CSVWriter()

    def scrapeWebsite(self):
        r = requests.get("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=ITC")
        data = r.text

        soup = BeautifulSoup(data, "lxml")

        for eachDiv in soup.find_all('div'):
            if 'id' in eachDiv.attrs:
                if eachDiv.attrs["id"] == 'responseDiv':

                    outputList = {}

                    theJSON = json.loads(eachDiv.string)
                    lastUpdatedTime = theJSON['lastUpdateTime']
                    allValues = theJSON['data'][0]

                    outputList['symbol'] = allValues['symbol']
                    outputList['companyName'] = allValues['companyName']
                    outputList['lastUpdatedTime'] = lastUpdatedTime
                    outputList['lastPrice'] = allValues['lastPrice']
                    outputList['previousClose'] = allValues['previousClose']
                    outputList['open'] = allValues['open']
                    outputList['totalTradedVolume'] = allValues['totalTradedVolume']
                    outputList['dayLow'] = allValues['dayLow']
                    outputList['dayHigh'] = allValues['dayHigh']
                    outputList['totalBuyQuantity'] = allValues['totalBuyQuantity']
                    outputList['totalSellQuantity'] = allValues['totalSellQuantity']

                    self.fileWriter.writeToCSV("stockValues.csv",outputList.values())

        print '============= Done Ka Baccha Done ============='


#item__flex-column

#https://www.trivago.in/?aDateRange%5Barr%5D=2018-01-04&aDateRange%5Bdep%5D=2018-01-05&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iPathId=265&aGeoCode%5Blat%5D=2.5&aGeoCode%5Blng%5D=112.5&iGeoDistanceItem=0&aCategoryRange=0%2C1%2C2%2C3%2C4%2C5&aOverallLiking=1%2C2%2C3%2C4%2C5&sOrderBy=relevance%20desc&bTopDealsOnly=false&iRoomType=7&cpt=26503&iIncludeAll=0&iViewType=0&bIsSeoPage=false&bIsSitemap=false&

    def scrapeTrivago(self):
        r = requests.get("https://www.myntra.com/tshirts/being-human/being-human-clothing-men-charcoal-grey-printed-round-neck-t-shirt/2179892/buy")
        data = r.text

        soup = BeautifulSoup(data, "lxml")

        print soup.text

        for eachDiv in soup.find_all('p'):
            # print  eachDiv
            if 'class' in eachDiv.attrs:
                # print 'Found some class ->' + str(eachDiv.attrs["class"])
                # print eachDiv.attrs
                for eachAttribute in eachDiv.attrs:
                    if eachAttribute == 'pdp-selling-price':
                        print eachDiv.attrs["class"]
                        print '======================='
                        print 'Found the fellow I want'



if __name__ == '__main__':
    try:
        theScraper = Scraper()
        theScraper.scrapeTrivago()
        # while True:
        #     #theScraper.scrapeWebsite()
        #     theScraper.scrapeTrivago()
        #     #time.sleep(2)
    except KeyboardInterrupt:
        ws.close()