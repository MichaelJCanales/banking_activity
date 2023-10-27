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
        for row in self.data: 
            valid_prices = [] 
            
            for stock_price in row:
                # skip any values that are empty strings then convert
                if stock_price != "":
                    # convert the strings to numbers
                    price = float(stock_price) 
            
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
        median = []
        
        for row in self.data:
            valid_prices =[]
            for stock_price in row:
                if stock_price != "":
                    price = float(stock_price)
            
                
                    
        ...

    def stddev03(self):
        """pt3
        """
        ...
