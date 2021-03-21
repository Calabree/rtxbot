class APICallTimer:
    def timer(self, pageCount):
        x=0
        i=0
        totalAPICallsPerDay = 50000
        totalNumOfRunsPerDay = totalAPICallsPerDay/pageCount
        requestsPerMinute = totalNumOfRunsPerDay/1440 #totlal minutes per day
        requestsPerSecond = requestsPerMinute/60
        while i < 1:
            i+=requestsPerSecond
            x+=1
        return x
