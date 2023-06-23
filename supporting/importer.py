import openpyxl

def get_rows():
    file_path = 'E:\Production\internationalconference\supporting\Book1.xlsx'
    workbook = openpyxl.load_workbook(file_path)
    sheet_name = 'Sheet1'
    sheet = workbook[sheet_name]
    rows = []
    for row in sheet.iter_rows(values_only=True):
        rows.append(row)
    return rows


if __name__ == '__main__':

    rows = get_rows()
    for row in rows:
        print('Line read successfully ', row)