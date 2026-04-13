import unittest  # 標準モジュールを読み込みます
import pokemon_speed_bot.split_text as split_text       # テスト対象のファイルを読み込みます

class TestA(unittest.TestCase):  # クラスを派生させて自分用のクラスを作ります
    def test_1(self):
        self.assertEqual(split_text.split_text("フシギバナ、最速"),["フシギバナ","最速"])     # シナリオ1
        self.assertEqual(split_text.split_text("ランドロス、霊獣、最速"),["ランドロス","霊獣","最速"])     # シナリオ2
        self.assertEqual(split_text.split_text("ロトム、スピン、準速"),["ロトム","スピン","準速"])

if __name__ == '__main__':
    unittest.main()

