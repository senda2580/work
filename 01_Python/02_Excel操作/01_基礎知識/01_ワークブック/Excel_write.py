#xlsxファイルを扱うライブラリを読み込む
import openpyxl
import os

#カレントディレクトリの変更
os.chdir('C:\\Users\\empla\\OneDrive\\デスクトップ\\work\\01_Python\\02_Excel操作\\01_基礎知識\\01_ワークブック')

#ワークブックを読み込む
wb = openpyxl.load_workbook("..\99_Excel\Write_Only.xlsx")

#アクティブなワークシートを取得する
ws = wb.active

#セルA2に値を入力する
ws["A2"].value = "TEST"

wb.save("..\99_Excel\Write_Only.xlsx")