from datetime import datetime
from src.__main__ import get_debt_report_by_range_date, format_debt_report


def test_debt_report():
    debt_report_by_range = get_debt_report_by_range_date(
        "tests/fixtures",
        datetime.strptime("2021-10-01", "%Y-%m-%d"),
        datetime.strptime("2021-10-01", "%Y-%m-%d"),
        1,
        "js,jsx",
    )
    assert (
        format_debt_report(debt_report_by_range)
        == "Date;Code Duplication;Coverage;Implementation Lines;"
        "Test Lines;Total Lines\n"
        "2021-10-01;9.43%;66.66%;14;79;93"
    )
