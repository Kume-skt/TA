import subprocess
import os
import shutil


def java_compile(file_path):
    # 実行コマンド
    print(file_path)
    command = ["javac", "-encoding", "UTF-8", file_path]
    # javaなどの実行をする
    subprocess.run(command, shell=True)


def java_run(wfile, file_path, file_name):
    print(file_path)
    print(file_name)
    # 実行コマンド
    command = ["java", file_name[:-6]]
    print(command)
    # javaなどの実行をする
    with open(wfile, 'w', encoding='utf-8') as f:
        subprocess.run(command, shell=True, stdout=f)


# subprocess.run(["java", "ex2/SampleYen"], shell=True)


def java_packageCreate(file_full_name, file_name):
    """実行に必要なフォルダを作成します

    Javaのファイルには、package部分が含まれているはず

    なので、コンパイル後そのpackageの構造道理に配置しないとエラーが起こる"""
    createP = []
    try:
        with open(file_full_name, 'r', encoding="utf8", errors='ignore') as target:
            file_path = target.readlines()[0]
            # package部分削除
            file_path = file_path[8:]
            # package構造
            file_path = file_path.strip(";\n")
            file_path = file_path.split('.')
            createP = file_path

            folderpaht = file_full_name.replace(file_name, "")
            for fo in file_path:
                folderpaht += fo
                # folder作成
                os.mkdir(folderpaht)
                folderpaht += "/"
            return "{}\\{}".format(file_full_name[:file_full_name.rfind("\\")], folderpaht[:-1])
    except FileExistsError:
        print('存在しています:{}'.format(file_name))
        folderpaht = file_full_name.replace(file_name, "")
        for fo in createP:
            folderpaht += fo
            folderpaht += "/"
        return "{}".format(folderpaht[:-1])


def Java_movePackage(target_folder, target_file):
    """javaファイルを作成したフォルダ（package）に移動します

    実行例 : Java_movePackage(target_folder="test/fol", target_file="Text.txt")
    """
    try:
        print('確認')
        print(target_file)
        # shutil.move(target_file, target_folder + '\\')
        shutil.copyfile(target_file, target_folder)
    except FileNotFoundError:
        print("{}ファイルは移動済みです".format(target_file))
