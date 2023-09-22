#xlsxファイルを扱うライブラリを読み込む
import openpyxl

#ワークブックを読み込む
wb = openpyxl.load_workbook("Excel\Write_Only.xlsx")

#アクティブなワークシートを取得する
ws = wb.active

#セルA2に値を入力する
ws["A2"].value = "TEST"

wb.save("Excel\Write_Only.xlsx")