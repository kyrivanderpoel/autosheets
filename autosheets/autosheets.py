import arrow
import attr
import pygsheets


@attr.s
class Autosheets(object):
    client_secret_filename = attr.ib(default="./client_secrets.json")
    client = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.client = pygsheets.authorize(client_secret=self.client_secret_filename)

    def update(self):
        for title in self.client.spreadsheet_titles():
            if "habit" in title.lower():
                sheet = self.client.open(title)
                self.update_daily(sheet)

    def update_daily(self, sheet):
        try:
            worksheet = sheet.worksheet_by_title("Daily")
        except pygsheets.exceptions.WorksheetNotFound:
            print(f"Skipping {sheet.title} because there is no Daily worksheet.")
        else:
            dt_string = arrow.get(arrow.now("US/Pacific")).format("YYYY-MM-DD")
            value = worksheet.get_value("B1")
            if value == dt_string:
                print(f"Skipping {sheet.title} because it already has a column for {dt_string}.")
            else:
                worksheet.insert_cols(1)
                worksheet.update_value("B1", dt_string)
                print(f"Updated {sheet.title} with {dt_string}")
