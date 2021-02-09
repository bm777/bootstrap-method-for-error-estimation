import time
import random, math
from random import randint

# ++++++++++++++++++++++++++++++++++++++++++++++++++
class Estimator():
    def __init__(self, default=40):
        self.set = self.dataset(samples=default)
        self.mean_median = [[], []]



    def __del__(self):
        del self
    def __str__(self):
        return "Class of error estimator using bootstrap method."


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

    def calculate_SD(self, set):
        # here we calculate standard error like in regression algorithme formula.
        avg = self.calculate_mean(sorted(set))
        N = len(set); tmp = 0
        for i in set:
            tmp += (i - avg)**2
        sd = math.sqrt(tmp/N)
        return sd

    def small_centile(self, l):
        return l[0] +(-1.96) * l[1]

    def big_centile(self, l):
        return l[0] + (1.96) * l[1]

if __name__ == '__main__':
    estim = Estimator()
    counter = 0
    maximum = 10000
    print("+++++++++++++++++++++++++++++++++++++++++")

    print("step [1] := DATASET GENERATION")
    print("-dataset : ",estim.set, "\n-size : ",len(estim.set))
    print("step [5] : REPEAT STEP 2 though 4 10000 times (start of loop)")
    while counter < maximum:
        print("     +++++++++ {} ++++++++".format(counter))
        print("\n   step [2,3] := RANDOM PICK UP FOR ALL SAMPLES(default=40)")
        print("     -picked up : ",estim.pick())

        print("\n   step [4] := CAULCULATE our SAMPLE STATISTIC(mean and median)")
        estim.mean_median[0].append(estim.calculate_mean(estim.pick()))       # mean
        estim.mean_median[1].append(estim.calculate_median(estim.pick()))       # median
        print("-    mean : ", estim.mean_median[0][-1], "\n-median : ", estim.mean_median[1][-1])
        counter += 1

    print("\nstep [6] := CAULCULATE STANDARD DEVIATION of distribution of the 10,000 means and medians")
    print("-SD of mean : ", estim.calculate_SD(estim.mean_median[0]))
    print("-SD of median : ", estim.calculate_SD(estim.mean_median[1]))
    print("\nstep [7] := CAULCULATE 2.5th and 97.5th centiles of the 10,000 means and medians")
    # I done some reseach about The percentile , i found the formula and the general table of Z.
    # formula x = avg + Z * median/ abd we deduce the Z.
    #       1th - 99th : -/+2.326
    #       2th - 97.5th : -/+1.960
    #       5th- 95th :  -/+1.645
    #       10th- 90th :  -/+1.282
    #       25th- 75th :  -/+0.675
    #       50th- 50th :  0
    mean_of_mean = estim.calculate_mean(estim.mean_median[0])
    mean_of_median = estim.calculate_mean(estim.mean_median[1])
    sd_of_mean = estim.calculate_SD(estim.mean_median[0])
    sd_of_median = estim.calculate_SD(estim.mean_median[1])
    print(mean_of_mean, sd_of_mean)
    print(mean_of_median, sd_of_median)
    print("-2.5th and 97.5th centile of 10,000 means : {} and {}".format(estim.small_centile([mean_of_mean, sd_of_mean]), estim.big_centile([mean_of_mean, sd_of_mean])))
    print("-2.5th and 97.5th centile of 10,000 medians : {} and {}".format(estim.small_centile([mean_of_median , sd_of_median]), estim.big_centile([mean_of_median , sd_of_median])))
    print("+++++++++++++++++++++++++++++++++++++++++")
