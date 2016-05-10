## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)
mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()

print(len(weight_lost_a), len(weight_lost_b))

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)

import numpy as np
import matplotlib.pyplot as plt

mean_differences = []
for _ in range(1000):
    group_a = []
    group_b = []
    for i in all_values:
        if(np.random.rand()) >= 0.5:
            group_a.append(i)
        else:
            group_b.append(i)
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)

plt.hist(mean_differences)
plt.show()

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}
for i in mean_differences:
    if sampling_distribution.get(i, False):
        sampling_distribution[i] += 1
    else:
        sampling_distribution[i] = 1
print(sampling_distribution)