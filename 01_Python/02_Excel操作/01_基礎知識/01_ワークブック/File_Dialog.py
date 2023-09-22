#xlsxファイルを扱うライブラリを読み込む
import openpyxl

#GUIのTkinterモジュールを読み込む
import tkinter as tk

#ファイルダイアログモジュールを読み込む
import tkinter.filedialog

#ルートウインドウを作成する
root = tk.Tk()

#ルートウインドウを非表示にする
root.withdraw()

#ファイルの拡張子を指定する
filetypes = [("Excelブック","*.xlsx"),]

#ファイルダイアログを表示する
filename = tkinter.filedialog.asksaveasfilename(filetypes=filetypes,title="名前を付けて保存",defaultextension = "xlsx")

#ファイルが存在する場合
if filename != "":
    #ワークブックを新規作成する
    wb = openpyxl.Workbook()

    #ワークブックを保存する
    wb.save(filename)