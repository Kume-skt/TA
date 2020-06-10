import glob
import os

"""ファイルを探してきて結果を返す"""


def get_file_path(file_path, target_file='**'):
    """ファイルパスを受け取りファイルを探します

        例：C:\\Users\\dendai\\Documents\\  
            target_fileはどのファイルを探すか決めます
            デフォルトはすべてのファイルを探してきます
    """
    # fileを探索しリスト化する
    file_list = [p for p in glob.glob(file_path + target_file,
                                      recursive=True)
                 if os.path.isfile(p)]
    return file_list


def get_file_name(file_path, target_file):
    """指定フォルダーのファイル名をすべて取得"""
    file_list = [os.path.basename(p) for p in glob.glob(file_path + target_file,
                                                        recursive=True)
                 if os.path.isfile(p)]
    return file_list


def get_file_directory(file_path):
    """指定フォルダーのディレクトリをすべて取得"""
    file_list = glob.glob(os.path.join(file_path, '**' + os.sep), recursive=True)
    return file_list
