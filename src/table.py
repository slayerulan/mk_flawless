import pygsheets
import retry

TABLE_NAME = "MKX_FLAWLESS"
SHEET_TITLE = "Stats"


@retry.retry(tries=3)
def authorize():
    scope = ["https://www.googleapis.com/auth/drive"]
    client = pygsheets.authorize(outh_file="client_secret.json")
    return client


def get_stats(fighter):
    rows = get_table_rows()
    for row in rows:
        f = row.get('Fighter')
        if f == fighter:
            stat = row.get('Stat')
            return stat

    return ""


@retry.retry(tries=3)
def get_table_rows():
    client = authorize()
    sheet = client.open(TABLE_NAME).worksheet_by_title(SHEET_TITLE)
    while True:
        try:
            rows = sheet.get_all_records()
        except Exception as e:
            continue
        break
    return rows
