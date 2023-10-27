import statistics as stats
from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        # skip the dates
        for row in self.data[1:]: 
            valid_prices = [] 
            
            for stock_price in row[1:]:
                # skip any values that are empty strings then convert
                if stock_price != "":
                    # convert the strings to numbers and .append to add into the average
                    price = float(stock_price)
                    valid_prices.append(price) 
            
            # get the average and round it to nearest 3rd decimal
            if valid_prices:
                average = stats.mean(valid_prices)
                rounded_average = round(average, 3)
                
                # append round_average to averages
                averages.append(rounded_average)
            
        return averages
        
    def median02(self):
        """pt2
        """
        # repurpose code from averages but don't round 
        medians = []
        
        for row in self.data:
            valid_prices =[]
            for stock_price in row:
                if stock_price != "":
                    price = float(stock_price)
                    valid_prices.append(price)
                    
            if valid_prices:
                median_row = stats.median(valid_prices)
                medians.append(median_row)
            
        return medians
                    
        ...

    def stddev03(self):
        """pt3
        """
        ...
