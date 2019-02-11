import openpyxl
import sys
from openpyxl import load_workbook
class ExcelTest:
# wb = openpyxl.load_workbook('D:\\PythonWS\\Premise\\resources\\PremiseTestData.xlsx')
# print(wb.sheetnames)
# print(type(wb))
# wb.sheetnames.__getitem__("")


    def getDataInHashMap(self , dataSheetFilePath , sheetName, dataKey):
        testData = {}
        try:
            dataSheetFilePath = ""
            testDataArray = []
            testDataArray = self.readExcelData(dataSheetFilePath, sheetName, dataKey)
            for i in testDataArray.len :
                # testData.update(testDataArray[i][0], testDataArray[i][1])
                testData[testDataArray[i][0]] =  testDataArray[i][1]
        except :
            print(" Failed to read excel data by data key  and store in linked hash map due to :::" + sys.exc_info())
        return testData


    def readExcelData(self, filePath, sheetName, tableName):
        testData = None
        print("Reading file, sheet, table::: " , filePath + ", " , sheetName + ", " , tableName)
        try:
            workbook = openpyxl.load_workbook(filePath)
            sheet = workbook.get_sheet_by_name(sheetName)
            boundaryCells = self.findCell(sheet, tableName)
            startCell = boundaryCells[0]
            endCell = boundaryCells[1]

            startRow = startCell.getRowIndex() + 1

            endRow = endCell.getRowIndex()

            startCol = startCell.getColumnIndex() + 1

            endCol = endCell.getColumnIndex() - 1
            testData = String[endRow - startRow + 1][endCol - startCol + 1]
            for (int i = startRow i < endRow + 1 i++):
                for (int j = startCol j < endCol + 1 j++):
                    if (sheet.getRow(i).getCell(j).getCellType() == HSSFCell.CELL_TYPE_STRING):
                        testData[i - startRow][j - startCol] = sheet.getRow(i).getCell(j).getStringCellValue()
                    elif (sheet.getRow(i).getCell(j).getCellType() == HSSFCell.CELL_TYPE_NUMERIC):
                         temp = sheet.getRow(i).getCell(j).getNumericCellValue()
                         testData[i - startRow][j - startCol] = String.valueOf(temp.intValue())
        except:
            print("EORRRR readExcelData" , sys.exc_info())
        return testData


    def findCell(self, sheet, text):
        pos = "start"
        cells = []
        try:
            for row in sheet.iter_rows(min_row=1, max_col=3, max_row=2):
                for cell in row:
                    print("cell>>>",cell.value)
                    if text == cell.value :
                        print("In Cell val")
                        if pos == "start":
                            cells[0] = cell
                            pos == "end"
                        else:
                            cells[1] = cell

        except:
            print("Erorr in find cell>>>",sys.exc_info())




        cells = HSSFCell[2]
        try:
            for (Row row: sheet):
                for (Cell cell: row):
                    if (cell.getCellType() == HSSFCell.CELL_TYPE_STRING & & text.equals(cell.getStringCellValue())):
                        if (pos.equalsIgnoreCase("start")):
                            cells[0] = (HSSFCell)cell
                            pos = "end"
                        else:
                            cells[1] = (HSSFCell)cell

        except:
              print(" Failed to find cell in excel due to :::" + sys.exc_info())
        return cells

    def roww(self):
        wb = openpyxl.load_workbook('D:\\PythonWS\\Premise\\resources\\PremiseTestData.xlsx')
        print(wb.sheetnames)
        sheet = wb.active
        for row in wb.iter_rows(min_row=1, max_col=3, max_row=2):
            for cell in row:
                print(cell)

    def excel_test(self):
        filepath = "D:\\PythonWS\\Premise\\resources\\PremiseTestData.xlsx"
        # load demo.xlsx
        wb = openpyxl.load_workbook(filepath)
        # select demo.xlsx
        sheet = wb.active
        # get max row count
        max_row = sheet.max_row
        # get max column count
        max_column = sheet.max_column
        # iterate over all cells
        # iterate over all rows
        for i in range(3, max_row + 1):

            # iterate over all columns
            for j in range(1, max_column + 1):
                # get particular cell value
                cell_obj = sheet.cell(row=i, column=j)
                # print("####",type(cell_obj))
                # print cell value
                print(cell_obj.value, end=' | ')
                # print("####", type(cell_obj.value))
            # print new line
            print('\n')


filePath = 'D:\\PythonWS\\Premise\\resources\\PremiseTestData.xlsx'
test = ExcelTest()
# test.getDataInHashMap(filePath,)
test.excel_test()