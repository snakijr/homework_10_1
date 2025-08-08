from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """обрабатывает информацию как о картах, так и о счетах"""
    list_number = number.split()
    if "Счет" == list_number[0]:
        mask = get_mask_account(list_number[-1])
        return f"Счет {mask}"
    else:
        mask = get_mask_card_number(list_number[-1])
        return f"{' '.join(list_number[:-1])} {mask}"


# print(mask_account_card(input()))


def get_date(date: str) -> str:
    """возвращает дату из формата ISO"""
    # Преобразуем в объект datetime
    dt = datetime.fromisoformat(date)
    # Форматируем в нужный вид
    formatted_date = dt.strftime("%d.%m.%Y")
    return formatted_date  # → 11.03.2024


# print(get_date(input()))
