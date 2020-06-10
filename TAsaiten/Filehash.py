# モジュールをインポートします
import hashlib


def File_hash(target_file):
    # ハッシュアルゴリズムを決めます
    algo = 'md5'

    # ハッシュオブジェクトを作ります
    h = hashlib.new(algo)

    # 分割する長さをブロックサイズの整数倍に決めます
    Length = hashlib.new(algo).block_size * 0x800

    # 大きなバイナリデータを用意します
    with open(target_file, 'rb') as f:
        BinaryData = f.read(Length)

        # データがなくなるまでループします
        while BinaryData:

            # ハッシュオブジェクトに追加して計算します。
            h.update(BinaryData)

            # データの続きを読み込む
            BinaryData = f.read(Length)
            
    return h.hexdigest()
    # ハッシュオブジェクトを16進数で出力します
    # print(algo, h.hexdigest())


# testfile1 = 'C:\\Users\\tsukasa\\Documents\\学校\\副手\\18FI009\\test.py'
# testfile2 = 'C:\\Users\\tsukasa\\Documents\\学校\\副手\\saiten\\python\\src\\test.py'

# File_hash(testfile1)
# File_hash(testfile2)