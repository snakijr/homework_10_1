def get_mask_card_number(card_number):
    """принимает на вход номер карты и возвращает ее маску"""
    try:
        masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return masked_card
    except Exception:
        raise TypeError('Неверный формат аргумента')




def get_mask_account(account_number):
    """принимает на вход номер счета и возвращает его маску"""
    try:
        masked_account = f"**{account_number[-4:]}"
        return masked_account
    except Exception:
        raise TypeError('Неверный формат аргумента')




