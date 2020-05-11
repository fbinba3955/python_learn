import pymysql
import xlwt


# 建立数据库连接
def getConn(database='sjt_test'):
    args = dict(
        host='localhost',
        user='root',
        passwd='root123',
        db=database,
        charset='utf8'
    )
    conn = pymysql.connect(**args)
    return conn


def mysql2excel(database='sjt_test', table='employees', excelResult=''):
    conn = getConn(database)
    cursor = conn.cursor()
    cursor.execute("select * from {}".format(table))
    data_list = cursor.fetchall()
    excel = xlwt.Workbook()
    sheet = excel.add_sheet("sheet1")
    row_number = len(data_list)
    column_number = len(cursor.description)
    for i in range(column_number):
        sheet.write(0, i, cursor.description[i][0])
    for i in range(row_number):
        for j in range(column_number):
            sheet.write(i + 1, j, data_list[i][j])
    excelName = "mysql_{}_{}.xls".format(database, table)
    if excelResult != '':
        excelName = excelResult
    excel.save(excelName)


if __name__ == "__main__":
    mysql2excel("sjt_test", "employees")