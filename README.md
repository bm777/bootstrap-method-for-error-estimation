# bootstrap-method-for-error-estimation
#### Tools used:
Python 3 on Ubuntu 18.04 and Core i7-9750 (CPU @2.60GHz x 12).

#### Type of data
The main dataset is made up by IQ. list of 40 sample and each between 30 and 170.

#### Result of computing
![alt](assets/top.png)
![alt](assets/new.gif)

### How to use the Class
Tasks you have TO DO.
- [x] Step [1] : DATASET GENERATION
```
estim = Estimator(default=40) # 40 is the default lenght of the set
counter = 0         # important for the next step
maximum = 10000     # you have to set your max number for iteration
```
- [x] Step [5] : REPEAT STEP 2 though 4 10000 times (start of loop)
```
while counter < maximum
    # step [2,3] := RANDOM PICK UP FOR ALL SAMPLES(default=40)
    estim.pick()
    # step [4] := CAULCULATE our SAMPLE STATISTIC(mean and median)
    estim.mean_median[0].append(estim.calculate_mean(estim.pick()))
    estim.mean_median[1].append(estim.calculate_median(estim.pick()))
```
- [x] Step [6] := CAULCULATE STANDARD DEVIATION of distribution of the 10,000 means and medians
```
estim.calculate_SD(estim.mean_median[0]) # SD of mean
estim.calculate_SD(estim.mean_median[1]) # SD of median
```
- [x] Step [7] := CAULCULATE 2.5th and 97.5th centiles of the 10,000 means and medians
```
mean_of_mean = estim.calculate_mean(estim.mean_median[0])
mean_of_median = estim.calculate_mean(estim.mean_median[1])
sd_of_mean = estim.calculate_SD(estim.mean_median[0])
sd_of_median = estim.calculate_SD(estim.mean_median[1])

estim.small_centile([mean_of_mean, sd_of_mean])       # 2.5th centile of 10000 means
estim.big_centile([mean_of_mean, sd_of_mean])         # 97.5th centile of 10000 means
estim.small_centile([mean_of_median , sd_of_median])  # 2.5th centile of 10000 medians
estim.big_centile([mean_of_median , sd_of_median])    # 97.5th centile of 10000 medians
```


#### Credit to this.
This [LINK](https://www.dummies.com/education/science/biology/the-bootstrap-method-for-standard-errors-and-confidence-intervals/) help me to understand the fundamental notion of bootstrap method.
