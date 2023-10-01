import datetime
import random
import math
import matplotlib.pyplot as plt

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def calculate_standard_deviation(numbers, mean):
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def generate_gaussian_distribution(mean, std_dev, n):
    random_numbers = []
    for _ in range(n):
        u1 = random.uniform(0, 1)
        u2 = random.uniform(0, 1)
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        random_numbers.append(mean + std_dev * z)
    return random_numbers

# Parameters for the normal distribution
desired_mean = 10
desired_std_dev = 0.5
num_samples = 500

# Generate random numbers with the desired mean and standard deviation
random_numbers = generate_gaussian_distribution(desired_mean, desired_std_dev, num_samples)

# Calculate mean, median, and standard deviation
mean_value = calculate_mean(random_numbers)
median_value = calculate_median(random_numbers)
standard_deviation_value = calculate_standard_deviation(random_numbers, mean_value)
print("random numbers are" , random_numbers)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", standard_deviation_value)

# Plot the histogram with 10 bins
plt.hist(random_numbers, bins=10, edgecolor='black', color='yellow', alpha=0.7)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Histogram of 500 Random Numbers (gaussian Distribution)', fontsize=14)
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_value:.2f}')
plt.axvline(median_value, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_value:.2f}')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Current date and time: {current_datetime}")