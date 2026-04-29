import math


def calculate_average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total / len(numbers)


def process_user_data(users):
    result = []
    for user in users:
        if user["age"] >= 18:
            if user["active"] == True:
                result.append(user["name"])
    return result


def generate_report(title, data):
    print("Report Title:", title)
    print("Data Count:", len(data))
    for item in data:
        print("Item:", item)


class DataProcessor:
    def clean_data(self, data):
        cleaned = []
        for item in data:
            if item is not None:
                cleaned.append(item)
        return cleaned

    def normalize_score(self, score):
        return score / 100


def unused_math_function(x):
    return math.sqrt(x) + math.pow(x, 2)