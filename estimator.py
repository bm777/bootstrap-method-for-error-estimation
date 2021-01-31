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
        return sum(resampled) / len(resampled)

    def calculate_median(self, resampled):
        if len(resampled) % 2 == 1:
            return resampled[resampled//2]
        elif len(resampled) % 2 == 0:
            if resampled[len(resampled)//2] != resampled[1+len(resampled)//2]:
                return resampled[len(resampled)//2] * 0.5 + resampled[1+len(resampled)//2] * 0.5
            else:
                return resampled[len(resampled)//2]



if __name__ == '__main__':
    estim = Estimator()
    counter = 0
    print("+++++++++++++++++++++++++++++++++++++++++")

    print("step [1] := DATASET GENERATION")
    print("-dataset : ",estim.set, "\n-size : ",len(estim.set))
    print("step [5] : REPEATSTEP 2 though 4 10000 times (start of loop)")
    while counter < 10000:
        print("+++++++++ {} ++++++++".format(counter))
        print("\nstep [2,3] := RANDOM PICK UP FOR ALL SAMPLES(default=40)")
        print("-picked up : ",estim.pick())

        print("\nstep [4] := CAULCULATE our SAMPLE STATISTIC(mean and median)")
        estim.mean_median[0].append(estim.calculate_mean(estim.pick()))       # mean
        estim.mean_median[1].append(estim.calculate_median(estim.pick()))       # median
        print("-mean : ", estim.mean_median[0][-1], "\n-median : ", estim.mean_median[1][-1])
        print("+++++++++++++++++++++++++++++++++++++++++")
        counter += 1

    print("+++++++++++++++++++++++++++++++++++++++++")
