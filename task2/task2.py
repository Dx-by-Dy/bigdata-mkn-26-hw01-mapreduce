# task2.py
from mrjob.job import MRJob
from mrjob.step import MRStep

class EnrichEventsWithDeviceInfo(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]
    
    def mapper(self, _, line):
        # TODO: реализовать
        pass
    
    def reducer(self, key, values):
        # TODO: реализовать
        pass

if __name__ == '__main__':
    EnrichEventsWithDeviceInfo.run()

