import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

dice_result = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1 + dice2)

mean_dice = sum(dice_result) / len(dice_result)
stdev_dice = statistics.stdev(dice_result)
median_dice = statistics.median(dice_result)
mode_dice = statistics.mode(dice_result)

first_stdev_start, first_stdev_end = mean_dice - stdev_dice, mean_dice + stdev_dice
second_stdev_start, second_stdev_end = mean_dice - (2 * stdev_dice), mean_dice + (2 * stdev_dice)
third_stdev_start, third_stdev_end = mean_dice - (3 * stdev_dice), mean_dice + (3 * stdev_dice)

dice_graph = ff.create_distplot([dice_result], ['Result'], show_hist=False)

dice_graph.add_trace(go.Scatter(x = [mean_dice, mean_dice], y = [0, 0.17], mode = 'lines', name = 'mean'))

dice_graph.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = 'lines', name = 'standard deviation 1'))
dice_graph.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = 'lines', name = 'standard deviation 1'))

dice_graph.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = 'lines', name = 'standard deviation 2'))
dice_graph.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = 'lines', name = 'standard deviation 2'))

dice_graph.show()

stddev_1_data = [result for result in dice_result if result > first_stdev_start and result < first_stdev_end]
stddev_2_data = [result for result in dice_result if result > second_stdev_start and result < second_stdev_end]
stddev_3_data = [result for result in dice_result if result > third_stdev_start and result < third_stdev_end]

print(mean_dice, median_dice, mode_dice, stdev_dice, stddev_1_data, stddev_2_data, stddev_3_data)

print('{}% of data lies within first standard deviation'.format(len(stddev_1_data) * 100.0 / len(dice_result)))
print('{}% of data lies within second standard deviation'.format(len(stddev_2_data) * 100.0 / len(dice_result)))
print('{}% of data lies within third standard deviation'.format(len(stddev_3_data) * 100.0 / len(dice_result)))