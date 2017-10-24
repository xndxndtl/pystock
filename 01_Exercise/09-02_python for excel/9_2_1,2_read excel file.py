import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\Kim\\Desktop\\test.xlsx')
ws = wb.ActiveSheet
print(ws.Cells(1,2).Value)
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10
""" excel.Quit() """