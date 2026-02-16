class FrequencyTracker:

    def __init__(self):
        self.dic1 = Counter()
        self.dic2 = Counter()
        
    def add(self, number: int) -> None:
        key = self.dic1[number]

        if key > 0:
            self.dic2[key] -= 1
            if self.dic2[key] == 0:
                del self.dic2[key]

        self.dic2[key+1] += 1
        self.dic1[number] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.dic1:
            key = self.dic1[number]
            self.dic2[key] -= 1

            if self.dic2[key] == 0:
                del self.dic2[key]

            if key - 1 > 0:
                self.dic2[key - 1] += 1
            
            self.dic1[number] -= 1 
            if self.dic1[number] == 0:
                del self.dic1[number]
                
            return True

        return False

    def hasFrequency(self, frequency: int) -> bool:
        return self.dic2[frequency] > 0
            
            
    
  