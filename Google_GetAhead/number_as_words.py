
_DIGITS_AND_TEENS = [
    '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'nineteen'
]
_TENS = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
'ninety'
]
_MULTIPLIERS = [
    '', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
    'quintillion'
]


def get_amount_less_than_thousand(amount: int) -> str:
    """Computes string representation for positive integers < 1000."""
    result_components = []
    hundreds, tens_units = divmod(amount, 100)
    if hundreds > 0:
        result_components.append(f'{_DIGITS_AND_TEENS[hundreds]} hundred')
    if tens_units >= 20:
        result_components.append(_TENS[tens_units // 10])
        result_components.append(_DIGITS_AND_TEENS[tens_units % 10])
    else:
        result_components.append(_DIGITS_AND_TEENS[tens_units])
    return ' '.join(result_components).rstrip()


def get_amount_in_words(amount: int) -> str:
    """Returns the string representation for a positive integer of at most 12
    digits."""
    if amount == 0:
        return "zero"
    amount_segments = []
    multiplier_counter = 0
    while amount > 0:
        segment = amount % 1000
        if segment > 0:
            segment_in_words = get_amount_less_than_thousand(segment)
            multiplier = _MULTIPLIERS[multiplier_counter]
            amount_segments.append(f'{segment_in_words} {multiplier}')
        amount = amount // 1000
        multiplier_counter += 1
    amount_segments.reverse()
    return ' '.join(amount_segments).rstrip()