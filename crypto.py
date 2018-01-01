import urllib.request 
import json
import locale

locale.setlocale( locale.LC_ALL, '' )
locale.currency( 1234.50, grouping = True )

def printResults(data):
  print('\nLocale from environment:', locale.getlocale())
  theJSON = json.loads(data)
  print("Last Price: " + theJSON["last"]
    + "\nLast 24 hours price high: " + theJSON["high"]
    + "\nast 24 hours price low " + theJSON["low"]
    + "\nLast 24 hours volume weighted average price: " + theJSON["vwap"]
    + "\nLast 24 hours volume: " + theJSON["volume"]
    + "\nHighest buy order " + theJSON["bid"]
    + "\nLowest sell order: " + theJSON["ask"]
    + "\nUnix timestamp date and time: " + theJSON["timestamp"]
    + "\nFirst price of the day: " + theJSON["open"])
  print('\nLocale from environment:', locale.getlocale())
  


def main():
  currency_pair = "xrpusd"
  urlData = "https://www.bitstamp.net/api/v2/ticker/" + currency_pair

    # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print (webUrl.getcode())
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    data = data.decode("utf-8") # in Python 3.x we need to explicitly decode the response to a string
    # print out our customized results
    printResults(data)
  else:
    print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))
  

if __name__ == "__main__":
  main()