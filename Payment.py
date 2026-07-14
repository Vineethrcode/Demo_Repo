def process_payment(amount, card_number):
    if amount <= 0:
        return False

    if len(card_number) != 16:
        return False

    return True