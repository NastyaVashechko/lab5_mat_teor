import numpy as np

p1, p2, p3, p4 = 0.1, 0.5, 0.3, 0.1

profits = {
    'жито': [15, 10, 12, 6],
    'овес': [18, 8, 17, 7],
    'пшениця': [19, 12, 16, 9],
    'гречка': [21, 15, 18, 6]
}

def calculate_variance(profits, probabilities):
    mean_value = sum(p * f for p, f in zip(probabilities, profits))
    variance = sum(p * (f - mean_value) ** 2 for p, f in zip(probabilities, profits))
    return variance

def calculate_coefficient_of_variation(profits, probabilities):
    mean_value = sum(p * f for p, f in zip(probabilities, profits))
    variance = calculate_variance(profits, probabilities)
    std_dev = np.sqrt(variance)
    coefficient_of_variation = std_dev / mean_value if mean_value != 0 else float('inf')
    return coefficient_of_variation

results = {}
for crop, profits in profits.items():
    variance = calculate_variance(profits, [p1, p2, p3, p4])
    coefficient_of_variation = calculate_coefficient_of_variation(profits, [p1, p2, p3, p4])
    results[crop] = {
        'variance': variance,
        'coefficient_of_variation': coefficient_of_variation
    }

min_variance_crop = min(results, key=lambda x: results[x]['variance'])
min_cv_crop = min(results, key=lambda x: results[x]['coefficient_of_variation'])

print("Оптимальний варіант за критерієм мінімальної дисперсії:")
print(f"  Культура: {min_variance_crop}")
print(f"  Дисперсія: {results[min_variance_crop]['variance']}")
print()

print("Оптимальний варіант за критерієм мінімального коефіцієнта варіації:")
print(f"  Культура: {min_cv_crop}")
print(f"  Коефіцієнт варіації: {results[min_cv_crop]['coefficient_of_variation']}")
print()
