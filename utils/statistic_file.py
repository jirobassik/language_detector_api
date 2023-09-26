from collections import Counter


def calculate_statistic_file(files_list: list, dict_language: dict):
    num_all_files = len(files_list)
    counter_languages = Counter(dict_language.values())
    english_percent = (counter_languages['english'] / num_all_files) * 100
    russian_percent = (counter_languages['russian'] / num_all_files) * 100
    return english_percent, russian_percent
