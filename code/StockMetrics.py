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
            # convert to float first and skip empty strings
            valid_prices = [float(price) for price in row[1:] if price != "" and price != " "]  
            
            # get the average and round it to nearest 3rd decimal 
            average = stats.mean(valid_prices)                
            rounded_average = round(average, 3)                
            # append rounded_average to averages
            averages.append(rounded_average)
            
        return averages
        
    def median02(self):
        """pt2
        """
        # repurpose code from averages, don't round 
        medians = []
        
        for row in self.data:
            valid_prices =[float(price) for price in row[1:] if price != "" and price != " "]

            # get the median
            median_row = stats.median(valid_prices)
            medians.append(median_row)
            
        return medians

    def stddev03(self):
        """pt3
        """
        # now get the standard deviation
        # same as averages and round
        stand_dev = [] 
        
        for row in self.data:
            valid_prices = [float(price) for price in row[1:] if price != "" and price != " "]

            standeviation = stats.stdev(valid_prices)
            rounded_deviation = round(standeviation, 3)
            stand_dev.append(rounded_deviation)
                
        return stand_dev
