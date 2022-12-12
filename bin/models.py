from peewee import *
import report_racing as rr

db = SqliteDatabase('report.db')

report = rr.sort_report(rr.error_code_and_zero(rr.build_report('data')), 'asc')


class ReportBase(Model):
    abbreviation = CharField()
    place = CharField()
    name = CharField()
    team = CharField()
    time = DateTimeField()

    class Meta:
        database = db  # model use base - 'report.db'


ReportBase.create_table([ReportBase])

for item in report.items():
    add_report = ReportBase.get_or_create(
        abbreviation=item[0],
        place=item[1]['place'],
        name=item[1]['name'],
        team=item[1]['team'],
        time=item[1]['time']
    )
