import makeExcelfile
# 採点対象者
menberList = "C:\\Users\\tsukasa\\Documents\\学校\\副手\\saiten\\studentList.txt"
# 課題ファイル名のリスト作成
TestFile_List = ["Car.dia",
                 "Car.png",
                 "SampleYen.java",
                 "Yen.java"]
# 採点ファイルがある場所
# ex2
# ┗20fi010
# ┗20fi011
# ┗20fi012
# ┗20fi013
# ┗  ・
# ┗  ・
# ┗  ・
saiten_path = "C:\\Users\\tsukasa\\Documents\\学校\\副手\\OOP\\ex2"
# 結果出力ファイル
output_FileName = "oopEx2"

# 採点ファイル作成
makeExcelfile.createExcelFile(menberList, TestFile_List, output_FileName)

# 採点開始
makeExcelfile.openExcellFile(saiten_path, output_FileName)
