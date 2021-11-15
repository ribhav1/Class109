import statistics
import csv
import pandas as pd

with open('height-weight.csv') as f:
    file_data = pd.read_csv(f)

height_list = file_data['Height(Inches)'].to_list()
weight_list = file_data['Weight(Pounds)'].to_list()

height_mean, height_median, height_mode, height_stdev = statistics.mean(height_list), statistics.median(height_list), statistics.mode(height_list), statistics.stdev(height_list)
weight_mean, weight_median, weight_mode, weight_stdev = statistics.mean(weight_list), statistics.median(weight_list), statistics.mode(weight_list), statistics.stdev(weight_list)

print(height_mean, height_median, height_mode)
print(weight_mean, weight_median, weight_mode)

height_1stdev_start, height_1stdev_end = height_mean - height_stdev, height_mean + height_stdev
height_2stdev_start, height_2stdev_end = height_mean - (2 * height_stdev), height_mean + (2 * height_stdev)
height_3stdev_start, height_3stdev_end = height_mean - (3 * height_stdev), height_mean + (3 * height_stdev)

weight_1stdev_start, weight_1stdev_end = weight_mean - weight_stdev, weight_mean + weight_stdev
weight_2stdev_start, weight_2stdev_end = weight_mean - (2 * weight_stdev), weight_mean + (2 * weight_stdev)
weight_3stdev_start, weight_3stdev_end = weight_mean - (3 * weight_stdev), weight_mean + (3 * weight_stdev)

stddev_height_1_data = [result for result in height_list if result > height_1stdev_start and result < height_1stdev_end]
stddev_height_2_data = [result for result in height_list if result > height_2stdev_start and result < height_2stdev_end]
stddev_height_3_data = [result for result in height_list if result > height_3stdev_start and result < height_3stdev_end]

stddev_weight_1_data = [result for result in weight_list if result > weight_1stdev_start and result < weight_1stdev_end]
stddev_weight_2_data = [result for result in weight_list if result > weight_2stdev_start and result < weight_2stdev_end]
stddev_weight_3_data = [result for result in weight_list if result > weight_3stdev_start and result < weight_3stdev_end]

print('{}% of data lies within first standard deviation'.format(len(stddev_height_1_data) * 100.0 / len(height_list)))
print('{}% of data lies within second standard deviation'.format(len(stddev_height_2_data) * 100.0 / len(height_list)))
print('{}% of data lies within third standard deviation'.format(len(stddev_height_3_data) * 100.0 / len(height_list)))

print('{}% of data lies within first standard deviation'.format(len(stddev_weight_1_data) * 100.0 / len(weight_list)))
print('{}% of data lies within second standard deviation'.format(len(stddev_weight_2_data) * 100.0 / len(weight_list)))
print('{}% of data lies within third standard deviation'.format(len(stddev_weight_3_data) * 100.0 / len(weight_list)))