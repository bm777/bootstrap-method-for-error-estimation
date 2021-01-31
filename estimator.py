import time
import random
from random import randint

# ++++++++++++++++++++++++++++++++++++++++++++++++++
class Estimator():
    def __init__(self):
        self.set = self.dataset()
        self.mean_median = [[], []]



    def __del__(self):
        del self
    def __str__(self):
        return "CLass of error estimator using bootstrap method."


    def dataset(self, samples=40):
        return [randint(30, 170) for s in range(samples)]

    # step 2
    def pick(self, samples=40):
        return sorted([self.set[randint(0,s)] for s in range(samples)])

    def calculate_mean(self, resampled):
        return mean(resampled)

    def calculate_median(self, resampled):
        if len(resampled) % 2 == 1:
            return resampled[resampled//2]
        elif len(resampled) % 2 == 0:
            if resampled[resampled//2] != resampled[1+resampled//2]:
                return resampled[resampled//2] * 0.5 + resampled[1+resampled//2] * 0.5
            else:
                return resampled[resampled//2]

if __name__ == '__main__':
    estim = Estimator()

    print("+++++++++++++++++++++++++++++++++++++++++")

    print("step [1] := DATASET GENERATION")
    print("-dataset : ",estim.set, "\n-size : ",len(estim.set))

    print("\nstep [2,3] := ")
    print("-picked up : ",estim.pick())
    print("+++++++++++++++++++++++++++++++++++++++++")
