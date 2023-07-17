from openpyxl import Workbook



class infoS:
    def __init__(self, name, no, address):
        self.name = name
        self.no = no
        self.address = address


    def writeExcel(self,rowNo):

        sheet["A"+str(rowNo)] = self.name
        sheet["B"+str(rowNo)] = self.no
        sheet["C"+str(rowNo)] = self.address


def excelStart():
    global sheet
    global workbook
    workbook = Workbook()
    sheet = workbook.active
    sheet.column_dimensions['A'].width = 60
    sheet.column_dimensions['B'].width = 35
    sheet.column_dimensions['C'].width = 35
    sheet["A1"] = "Firma adı"
    sheet["B1"] = "Telefon Numarası"
    sheet["C1"] = "Adres"

def excelFinish(saveName):
    workbook.save("excels/"+str(saveName)+".xlsx")
    workbook.close()