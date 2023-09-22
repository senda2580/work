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

#作成したファイルを読み込む
wb = openpyxl.load_workbook(filename)

#プロパティのタイトルを設定する
wb.properties.title = "プログラムの起動確認"

#プロパティの件名を設定する
wb.properties.subject = "property.pyの起動確認"

#プロパティのタグを設定する
wb.properties.keywords = "Python"

#プロパティのコメントを設定する
wb.properties.description = "Pythonのプログラムで作成したファイルです"

#プロパティの作成者を設定する
wb.properties.creator = "セント"

#プロパティの前回保存者を設定する
wb.properties.lastModifiedBy = "セント"

wb.save(filename)