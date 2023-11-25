
def compare_rows(row_1, row_2) -> int | None:
    if not isinstance(row_1, str) or not isinstance(row_2, str):
        return 0
    if row_1 == row_2:
        return 1
    if len(row_1) > len(row_2):
        return 2
    if row_2 == 'learn':
        return 3
    raise ValueError('No expected value provided')
