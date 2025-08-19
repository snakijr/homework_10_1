from datetime import datetime

def filter_by_state(list_dict: list, state_value: str = "EXECUTED") -> list:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param list_dict: список словарей
    :param state_value: значение для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список словарей, где 'state' == state_value
    """
    return [item for item in list_dict if item.get("state") == state_value]




def sort_by_date(list_dict: list, date_key: str = "date", reverse: bool = False) -> list:
    '''Функция должна возвращать новый список, отсортированный по дате '''

    return sorted(
        list_dict,
        key=lambda item: datetime.strptime(item[date_key], "%Y-%m-%d"),
        reverse=reverse
    )
