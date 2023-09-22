#import xlsxを扱うライブラリを読み込む
import openpyxl

#ワークブックを読み込む
wb = openpyxl.load_workbook(".\Excel\Read_Only.xlsx")

#アクティブなワークシート情報を取得する
ws = wb.active

#セルA2に値を入力する
ws["A2"].value = "TEST"

wb.save(".\Excel\Read_Only.xlsx")

