class UndergroundSystem:
#
# 1 <= id, t <= 106
# 1 <= stationName.length, startStation.length, endStation.length <= 10
# All strings consist of uppercase and lowercase English letters and digits.
# There will be at most 2 * 104 calls in total to checkIn, checkOut, and 
# getAverageTime.
# Answers within 10-5 of the actual value will be accepted.
#
    def __init__(self):
        self._dict = collections.defaultdict(int)
        self._checkIn = collections.defaultdict(list)
        self._sum = collections.defaultdict(list)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._checkIn[id].append(stationName)
        self._checkIn[id].append(t)
        #print("checkIn", self._checkIn)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        tup = (self._checkIn[id][0], stationName)
        if tup in self._sum:
            self._sum[tup][0] += t-self._checkIn[id][1]
            self._sum[tup][1] += 1
        else:
            self._sum[tup].append(t-self._checkIn[id][1])
            self._sum[tup].append(1)
        self._checkIn[id] = []
            
                  
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #print("getAvg", self._sum)
        tup = (startStation, endStation)
        if tup in self._sum:
            return self._sum[tup][0] / self._sum[tup][1]
        return 0.0
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
