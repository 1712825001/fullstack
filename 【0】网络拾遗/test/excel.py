import xlrd
import xlwt
data = xlrd.open_workbook(r"D:\test.xlsx")
table = data.sheets()[0]

table1 = data.sheets()[0]


row = table1.row_values(0)
col =table1.col_values(2)


cell_a1 =table1.cell_value(0,0)


workbook =xlwt.Workbook(encoding ="utf-8",style_compression=0)
sheet =workbook.add_sheet("2",cell_overwrite_ok=True)

sheet.write(0,0,"english_name111111111111")
workbook.save(r"2")