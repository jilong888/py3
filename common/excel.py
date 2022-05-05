import xlrd,xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import xlsxwriter
class excel:
    def __init__(self, sheetname):
        global _excelname
        _excelname=sheetname
        self.r_excel=xlrd.open_workbook(sheetname)
    def read_excel(self,x,y):
        data = self.r_excel
        table = data.sheets()[0]
        # print(table.nrows, table.ncols)
        return table.cell(x-1, y-1).value
    def add_excel(self,x,y,value,sheetname):
        workbook=xlwt.Workbook(encoding = 'ascii')
        worksheet=workbook.add_sheet('sheet1')
        # print(worksheet)
        worksheet.write(x-1, y-1, label = value)
        workbook.save(sheetname)
    def write_excel(self,x,y,value,excelname=None):
        # rb = open_workbook(excelname)
        # rs = rb.sheet_by_index(0)
        # wb = copy(rb)
        # ws = wb.get_sheet(0)
        if not excelname: excelname=_excelname
        rb = xlrd.open_workbook(excelname)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        ws.write(x-1, y-1, value)
        wb.save(excelname)
    def write_excel2(self,xy,value,excelname):
        workbook = xlsxwriter.Workbook(excelname)  # 创建一个excel文件
        worksheet = workbook.add_worksheet(u'')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1
        # worksheet.set_column('A:A', 20)  # 设置第一列宽度为20像素
        worksheet.write(xy,value)
        # worksheet.write('A4', 2)
        # worksheet.write('A5', '=A3+A4')
        workbook.close()
excel_path='/Users/jilong/py/middleware/excel.xls'
t=excel('/Users/jilong/py/middleware/excel.xls')


# print(t.read_excel(1,1))
# excel.add_excel(1, 1, 'hello,excel2!', 'test2.xls')
# t.write_excel(1,1,100,excel_path)
# excel.write_excel(2,5,200,'excel.xls')
# excel.write_excel(3,5,'=A5+B5','excel.xls')
# excel.write_excel2('A1',123,'test.xlsx')