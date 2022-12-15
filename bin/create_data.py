import report_racing as rr
from models import *


report = rr.sort_report(rr.error_code_and_zero(rr.build_report('data')), 'asc')
create_tables()

for item in report.items():
    add_report = Report.get_or_create(
        abbreviation=item[0],
        place=item[1]['place'],
        name=item[1]['name'],
        team=item[1]['team'],
        time=item[1]['time']
    )


