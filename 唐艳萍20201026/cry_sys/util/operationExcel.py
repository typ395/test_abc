import xlrd
class OperationExcel:
    def __init__(self,path,sheet_name):
        self.workbook=xlrd.open_workbook(path)
        self.sheet=self.workbook.sheet_by_name(sheet_name)
    def get_nows(self):
        return self.sheet.nrows
    def get_ncols(self):
        return self.sheet.ncols
    def get_cell(self,row,col):
        cell_v=self.sheet.cell_value(row, col)
        if cell_v=='null':
            cell_v=''
        return cell_v
# if __name__ == '__main__':
#     op=OperationExcel('D:\\测试\\test_case.xlsx','用例参数')
#     print(op.get_cell(7,2))
#     print(op.get_cell(7, 3))
#     print(op.get_cell(7, 4))