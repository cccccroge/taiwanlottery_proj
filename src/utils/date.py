# format of args: 'YYYY-MM'
def iter_year_month(start_year_month, end_year_month):
    start_year = int(start_year_month[:4])
    start_month = int(start_year_month[-2:])
    end_year = int(end_year_month[:4])
    end_month = int(end_year_month[-2:])

    ym_start = 12 * start_year + start_month - 1
    ym_end = 12 * end_year + end_month - 1
    for ym in range(ym_start, ym_end):
        y, m = divmod( ym, 12 )
        yield y, m + 1
