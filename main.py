import math
import scipy.stats as st
import matplotlib.pyplot as plt
# import statistics
# import numpy


# def calculation_of_accumulative_relative_frequency(relative_frequency):
#     accumulative_relative_frequency = []
#     temp = 0
#     for x in relative_frequency:
#         temp += x
#         accumulative_relative_frequency.append(temp)
#     return accumulative_relative_frequency


# def print_accumulative_relative_frequency(accumulative_relative_frequency):
#     print('Accumulative Relative Frequency:')
#     for x in accumulative_relative_frequency:
#         print(x)
#     print()


# def print_accumulative_frequency(accumulative_frequency):
#     print('Accumulative Frequency:')
#     for x in accumulative_frequency:
#         print(x)
#     print()


# def calculation_of_accumulative_frequency(frequency):
#     accumulative_frequency = []
#     temp = 0
#     for x in frequency:
#         temp += x
#         accumulative_frequency.append(temp)
#     return accumulative_frequency


# def calculation_of_relative_frequency(frequency, sorted_nums):
#     relative_frequency = []
#     for x in frequency:
#         relative_frequency.append(x / len(sorted_nums))
#     return relative_frequency


# def print_relative_frequency(intervals, relative_frequency):
#     print('Relative frequency:')
#     for i, f in zip(intervals, relative_frequency):
#         print('{}-{}: {}'.format(i[0], i[1], f))
#     print()


# def calculation_of_frequency(intervals, sorted_nums):
#     frequency = []
#     counter = 0
#     for x in range(len(intervals)):
#         for number in sorted_nums:
#             if number in range(int(intervals[x][0]), int(intervals[x][1])) or (
#                     x + 1 == len(intervals) and number == int(intervals[x][1])):
#                 counter += 1
#         frequency.append(counter)
#         counter = 0
#     return frequency


# def print_frequency(frequency, intervals):
#     print('Frequency:')
#     for i, f in zip(intervals, frequency):
#         print('{}-{}: {}'.format(i[0], i[1], f))
#     print()


# def calculation_of_intervals(x_min, k, h):
#     intervals = []
#     interval = []
#     for i in range(k):
#         interval.append(x_min + h * i)
#         interval.append(x_min + h * (i + 1))
#         intervals.append(interval)
#         interval = []
#     return intervals


# def print_intervals(intervals):
#     print('Intervals:')
#     for x in intervals:
#         print('{}-{}'.format(x[0], x[1]))
#     print()


# def main():

#     a = []
#     for x in nums:
#     if x in range(int(intervals[1][0]), int(intervals[1][1])):
#         a.append(x)

#     print(statistics.median(sorted_nums))
#     print(statistics.mean(sorted_nums))
#     print(statistics.mode(sorted_nums))
#     print(numpy.var(sorted_nums))
#     print(pow(numpy.var(sorted_nums), 0.5))
def caluclation_of_skewness_and_kurtosis():
	return 0


def calculation_of_sample_mean(length, intervals, frequency):
	# Calculating sample mean
	sample_mean = 0
	interval_average = []
	for x in intervals:
		interval_average.append((x[0] + x[1])/2)
	for x in range(len(intervals)):
		sample_mean += interval_average[x] * frequency[x]
	sample_mean /= length

	# Calculating variance
	variance = 0
	for x in range(len(intervals)):
		variance += (interval_average[x] - sample_mean)**2 * frequency[x]
	variance /= length

	# Calculating standard deviation
	standard_deviation = variance ** 0.5

	return sample_mean, variance, standard_deviation

def calculation_of_stats(length, intervals, frequency, accumulative_frequency):
	# Calculating modal interval
	mode_interval = intervals[frequency.index(max(frequency))]
	# Calculating mode
	mode = mode_interval[0] + (mode_interval[1]-mode_interval[0]) * (frequency[frequency.index(max(frequency))] - frequency[frequency.index(max(frequency))-1])/((frequency[frequency.index(max(frequency))] - frequency[frequency.index(max(frequency))-1]) + (frequency[frequency.index(max(frequency))] - frequency[frequency.index(max(frequency))+1]))
	# Calculating median interval
	median_interval = intervals[int(len(intervals)/2)-1]
	# Calculting median
	median = median_interval[0] + (median_interval[1]-median_interval[0]) * (length - accumulative_frequency[int(len(intervals)/2)-1])/frequency[int(len(intervals)/2)-1]
	
	return mode, mode_interval, median, median_interval

def calculation_of_frequency(intervals, sorted_nums):
	# Calculating frequency
	frequency = []
	counter = 0
	for x in range(len(intervals)):
		for number in sorted_nums:
			if number in range(int(intervals[x][0]), int(intervals[x][1])) or \
			(x + 1 == len(intervals) and number == int(intervals[x][1])):
				counter += 1
		frequency.append(counter)
		counter = 0

	# Calculating accumulative frequency
	accumulative_frequency = []
	temp = 0
	for x in frequency:
		temp += x
		accumulative_frequency.append(temp)

	# Calculating relative frequency
	relative_frequency = []
	for x in frequency:
		relative_frequency.append(x / len(sorted_nums))
    
	# Calculating relative accumulative frequency
	accumulative_relative_frequency = []
	temp = 0
	for x in relative_frequency:
		temp += x
		accumulative_relative_frequency.append(temp)
    
	return frequency, accumulative_frequency, relative_frequency, accumulative_relative_frequency

def calculation_of_intervals(numbers):
    # The biggest and the smallest numbers
	x_max = max(numbers)
	x_min = min(numbers)
  	# Optimal number of intervals
	k =  int(1 + 1.44 * math.log(len(numbers), math.e) + 0.5)
    # Interval size
	h = (x_max - x_min) / k
	description = [x_max, x_min, k, h]
	# Calculating intervals
	intervals = []
	interval = []
	for i in range(k):
		interval.append(x_min + h * i)
		interval.append(x_min + h * (i + 1))
		intervals.append(interval)
		interval = []
	return intervals, description

if __name__ == '__main__':
    # Variational series
	numbers = [
		156, 161, 166, 162, 170, 167, 174, 160, 168, 165,
		169, 171, 154, 166, 158, 162, 175, 167, 164, 161,
		163, 159, 169, 156, 172, 168, 178, 176, 165, 167,
		157, 166, 162, 173, 161, 169, 177, 179, 167, 164,
		163, 160, 166, 170, 168, 174, 156, 165, 180, 169,
		167, 164, 171, 168, 170, 159, 175, 166, 155, 162,
		168, 172, 163, 160, 166, 176, 181, 167, 165, 157,
		162, 154, 169, 173, 167, 161, 172, 177, 168, 165,
		160, 163, 167, 170, 186, 166, 165, 158, 169, 166,
		163, 166, 171, 169, 160, 167, 164, 168, 161, 184,
    ]
    # Sorted numbers
	sorted_numbers = sorted(numbers)
	intervals, description = calculation_of_intervals(numbers)
	frequency, accumulative_frequency, relative_frequency, accumulative_relative_frequency = calculation_of_frequency(intervals, numbers)
	mode, mode_interval, median, median_interval = calculation_of_stats(len(numbers), intervals, frequency, accumulative_frequency)
	print(intervals, description, frequency, accumulative_frequency, relative_frequency, accumulative_relative_frequency, sep='\n\n')
	
	print(calculation_of_sample_mean(len(numbers), intervals, frequency))
	print(mode, mode_interval, median, median_interval)
	print(st.skew(sorted_numbers))
	print(st.kurtosis(sorted_numbers))

	fig = plt.figure()
	plt.plot(intervals, frequency)
	plt.show()
#     print('Maximal element: {}\nMinimal element: {}\nOptimal number of intervals: {}\nInterval size: {}\n'
#           .format(x_max, x_min, k, h))


#     # Calculation of frequency
#     frequency = calculation_of_frequency(intervals, sorted_nums)
#     # Output of intervals frequency
#     print_frequency(frequency, intervals)

#     # Calculation of relative frequency
#     relative_frequency = calculation_of_relative_frequency(
#         frequency, sorted_nums)
#     # Output of intervals relative frequency
#     print_relative_frequency(intervals, relative_frequency)

#     # Calculation of accumulative frequency
#     accumulative_frequency = calculation_of_accumulative_frequency(frequency)
#     # Output of accumulative frequency
#     print_accumulative_frequency(accumulative_frequency)

#     # Calculation of accumulative relative frequency
#         accumulative_relative_frequency = calculation_of_accumulative_relative_frequency(
#             relative_frequency)
#     # Output of accumulative relative frequency
#         print_accumulative_relative_frequency(accumulative_relative_frequency)
