class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        self.heap.append(num)

    def findMedian(self) -> float:
        self.heap.sort()
        length = len(self.heap)
        if(length & 1):
            return self.heap[length//2]
        else:
            return (self.heap[length//2] + self.heap[length//2-1]) / 2