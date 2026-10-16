# task3.py
from mrjob.job import MRJob
from mrjob.step import MRStep

class SuspiciousTransactions(MRJob):
    
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
    SuspiciousTransactions.run()

