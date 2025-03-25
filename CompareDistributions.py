from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import statistics as st


def get_throws_of_cubes(filename):
    with open(filename, 'r') as file:
        throws = [list(map(int, line.split())) for line in file.read().strip().split('\n')]
    return throws

def calculate_sums_of_throws(throws):
    return [sum(x) for x in throws]

def norm_distribution_throws(norm_throws):  # это для нормального распределения
    normal_distribution = []
    for number, count in norm_throws.items():
        normal_distribution.extend([number] * count)
    return normal_distribution

def arrangement(array_of_sums): # функция для расстановки значений в нормальном виде
    general_sum = np.array(array_of_sums) # чтобы работать с numpy
    counter = Counter(general_sum) # подсчёт количества каждой суммы

    sums = np.array(sorted(counter.keys()))
    frequencies = np.array([counter[summa] for summa in sums]) # тут массив количества повторений каждой суммы

    sorted_indices = np.argsort(frequencies) # сортировка по частоте
    middle = len(sorted_indices) // 2 # находим середину

    centered_summs = np.zeros_like(sums)
    centered_freques = np.zeros_like(frequencies)
    for i, idx in enumerate(sorted_indices): # тут размещаем наши суммы так, чтобы часто встречающиеся были посередине, а редкие - по краям
        if i % 2 == 0:
            centered_summs[middle + i // 2] = sums[idx]
            centered_freques[middle + i // 2] = frequencies[idx]
        else:
            centered_summs[middle - (i // 2) - 1] = sums[idx]
            centered_freques[middle - (i // 2) - 1] = frequencies[idx]
    return centered_summs, centered_freques

def create_my_histogram(title, your_color, centered_summs, centered_freques):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_title(title)
    ax.bar(centered_summs, centered_freques, color=your_color)

    min_y = 0
    max_y = max(centered_freques)
    ax.set_yticks(range(min_y, max_y + 1, 1))
    ax.set_xticks(centered_summs)

    ax.set_xlabel("Суммы")
    ax.set_ylabel("Количество сумм")
    plt.grid(True)

def create_norm_histogram(title, your_color, centered_summs, centered_freques):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_title(title)
    ax.bar(centered_summs, centered_freques, color=your_color)

    min_y = 0
    max_y = 16
    ax.set_yticks(range(min_y, max_y + 1, 1))
    ax.set_yticks(centered_freques)
    ax.set_xticks(centered_summs)

    ax.set_xlabel("Суммы")
    ax.set_ylabel("Количество сумм")
    plt.grid(True)


# нахождение выборочных данных
def get_sample_mean(sample): # выборочное среднее значение
    return st.mean(sample)

def get_sample_median(sample): # медиана
    return st.median(sample)

def get_sample_mode(sample): # мода
    return st.mode(sample)

def get_sample_variance(sample): # выборочная дисперсия
    return st.variance(sample)

def get_sample_standard_deviation(sample): # выборочное среднеквадратичное значение
    return st.stdev(sample)


if __name__ == '__main__':

    # гистограмма с моими результатами
    throws_of_cubes = get_throws_of_cubes('БроскиКости.txt') # извлекаем значения бросков
    general_sums = calculate_sums_of_throws(throws_of_cubes) # считаем сумму каждого броска
    my_centered_sums, my_centered_freqs = arrangement(general_sums) # располагаем суммы в виде нормального распределения

    create_my_histogram('Мой эксперимент', 'mediumseagreen', my_centered_sums, my_centered_freqs)

    print('Выборочные данные моего эксперимента')
    print('Выборочное среднее: ', get_sample_mean(general_sums))
    print('Медианное значение: ', get_sample_median(general_sums))
    print('Мода: ', get_sample_mode(general_sums))
    print('Выборочная дисперсия: ', get_sample_variance(general_sums))
    print('Выборочное среднеквадратичное отклонение: ', get_sample_standard_deviation(general_sums), '\n')


    # гистограмма с нормальным идеальным распределением
    numbers = {2: 3, 12: 3, 3: 6, 11: 6, 4: 8, 10: 8, 5: 11, 9: 11, 6: 14, 8: 14, 7: 16}
    norm_distribution = norm_distribution_throws(numbers)

    centered_sums, centered_freqs = arrangement(norm_distribution)
    create_norm_histogram('Идеальный эксперимент', 'steelblue', centered_sums, centered_freqs)

    print('Выборочные данные идеального эксперимента')
    print('Выборочное среднее: ', get_sample_mean(norm_distribution))
    print('Медианное значение: ', get_sample_median(norm_distribution))
    print('Мода: ', get_sample_mode(norm_distribution))
    print('Выборочная дисперсия: ', get_sample_variance(norm_distribution))
    print('Выборочное среднеквадратичное отклонение: ', get_sample_standard_deviation(norm_distribution))

    plt.show()