# !/usr/bin/env python #
# -*- coding: utf-8 -*-

"""
フォルム違いのマップデータ
"""

FORM_MAP = {
    "ロトム": {
        "通常": "rotom",
        "ウォッシュ": "rotom-wash",
        "ヒート": "rotom-heat",
        "フロスト": "rotom-frost",
        "スピン": "rotom-fan",
        "カット": "rotom-mow"
    },
    "ランドロス": {
        "霊獣": "landorus-therian",
        "化身": "landorus-incarnate"
    },
    "ボルトロス": {
        "霊獣": "thundurus-therian",
        "化身": "thundurus-incarnate"
    },
    "トルネロス": {
        "霊獣": "tornadus-therian",
        "化身": "tornadus-incarnate"
    },
    "ヒヒダルマ": {
        "通常": "darmanitan-standard",
        "ダルマ": "darmanitan-zen"
    },
    "ギルガルド": {
        "シールド": "aegislash-shield",
        "ブレード": "aegislash-blade"
    },
    "バスラオ": {
        "あかすじ": "basculin-red-striped",
        "あおすじ": "basculin-blue-striped",
        "しろすじ": "basculin-white-striped"
    },
    "イエッサン": {
        "オス": "indeedee-male",
        "メス": "indeedee-female"
    },
    "ニャオニクス": {
        "オス": "meowstic-male",
        "メス": "meowstic-female"
    },
    "ウーラオス": {
        "いちげき": "urshifu-single-strike",
        "れんげき": "urshifu-rapid-strike"
    },
    "ザシアン": {
        "王": "zacian-crowned",
        "通常": "zacian"
    },
    "ザマゼンタ": {
        "王": "zamazenta-crowned",
        "通常": "zamazenta"
    },
    "ネクロズマ": {
        "日食": "necrozma-dusk",
        "月食": "necrozma-dawn",
        "ウルトラ": "necrozma-ultra"
    },
    "キュレム": {
        "ホワイト": "kyurem-white",
        "ブラック": "kyurem-black"
    },
    "シェイミ": {
        "スカイ": "shaymin-sky",
        "通常": "shaymin"
    },
    "ケルディオ": {
        "かくご": "keldeo-resolute",
        "通常": "keldeo"
    },
    "メロエッタ": {
        "ステップ": "meloetta-pirouette",
        "通常": "meloetta-aria"
    },
    "デオキシス": {
        "アタック": "deoxys-attack",
        "ディフェンス": "deoxys-defense",
        "スピード": "deoxys-speed",
        "通常": "deoxys-normal"
    },
    "パルデアケンタロス": {
        "コンバット": "tauros-paldea-combat-breed",
        "ブレイズ": "tauros-paldea-blaze-breed",
        "ウォーター": "tauros-paldea-aqua-breed"
    }
}
MEGA_MAP = {
    "フシギバナ": {"通常": "venusaur-mega"},
    "リザードン": {"X": "charizard-mega-x", "Y": "charizard-mega-y"},
    "カメックス": {"通常": "blastoise-mega"},
    "フーディン": {"通常": "alakazam-mega"},
    "ゲンガー": {"通常": "gengar-mega"},
    "ガルーラ": {"通常": "kangaskhan-mega"},
    "カイロス": {"通常": "pinsir-mega"},
    "ギャラドス": {"通常": "gyarados-mega"},
    "プテラ": {"通常": "aerodactyl-mega"},
    "ミュウツー": {"X": "mewtwo-mega-x", "Y": "mewtwo-mega-y"},
    "デンリュウ": {"通常": "ampharos-mega"},
    "ハッサム": {"通常": "scizor-mega"},
    "ヘラクロス": {"通常": "heracross-mega"},
    "ヘルガー": {"通常": "houndoom-mega"},
    "バンギラス": {"通常": "tyranitar-mega"},
    "バシャーモ": {"通常": "blaziken-mega"},
    "サーナイト": {"通常": "gardevoir-mega"},
    "クチート": {"通常": "mawile-mega"},
    "ボスゴドラ": {"通常": "aggron-mega"},
    "チャーレム": {"通常": "medicham-mega"},
    "ライボルト": {"通常": "manectric-mega"},
    "ジュペッタ": {"通常": "banette-mega"},
    "アブソル": {"通常": "absol-mega", "Z": "absol-mega-z"},
    "ガブリアス": {"通常": "garchomp-mega", "Z": "garchomp-mega-z"},
    "ルカリオ": {"通常": "lucario-mega", "Z": "lucario-mega-z"},
    "ユキノオー": {"通常": "abomasnow-mega"},
    "ラティアス": {"通常": "latias-mega"},
    "ラティオス": {"通常": "latios-mega"},
    "ラグラージ": {"通常": "swampert-mega"},
    "ジュカイン": {"通常": "sceptile-mega"},
    "ヤミラミ": {"通常": "sableye-mega"},
    "チルタリス": {"通常": "altaria-mega"},
    "エルレイド": {"通常": "gallade-mega"},
    "タブンネ": {"通常": "audino-mega"},
    "サメハダー": {"通常": "sharpedo-mega"},
    "ヤドラン": {"通常": "slowbro-mega"},
    "ハガネール": {"通常": "steelix-mega"},
    "ピジョット": {"通常": "pidgeot-mega"},
    "オニゴーリ": {"通常": "glalie-mega"},
    "ディアンシー": {"通常": "diancie-mega"},
    "メタグロス": {"通常": "metagross-mega"},
    "カイオーガ": {"通常": "kyogre-primal"},
    "グラードン": {"通常": "groudon-primal"},
    "レックウザ": {"通常": "rayquaza-mega"},
    "バクーダ": {"通常": "camerupt-mega"},
    "ミミロップ": {"通常": "lopunny-mega"},
    "ボーマンダ": {"通常": "salamence-mega"},
    "スピアー": {"通常": "beedrill-mega"},
    "ピクシー": {"通常": "clefable-mega"},
    "ウツボット": {"通常": "victreebel-mega"},
    "スターミー": {"通常": "starmie-mega"},
    "カイリュー": {"通常": "dragonite-mega"},
    "メガニウム": {"通常": "meganium-mega"},
    "オーダイル": {"通常": "feraligatr-mega"},
    "エアームド": {"通常": "skarmory-mega"},
    "ユキメノコ": {"通常": "froslass-mega"},
    "エンブオー": {"通常": "emboar-mega"},
    "ドリュウズ": {"通常": "excadrill-mega"},
    "ペンドラー": {"通常": "scolipede-mega"},
    "ズルズキン": {"通常": "scrafty-mega"},
    "シビルドン": {"通常": "eelektross-mega"},
    "シャンデラ": {"通常": "chandelure-mega"},
    "ブリガロン": {"通常": "chesnaught-mega"},
    "マフォクシー": {"通常": "delphox-mega"},
    "ゲッコウガ": {"通常": "greninja-mega"},
    "カエンジシ": {"通常": "pyroar-mega"},
    "フラエッテ": {"通常": "floette-mega"},
    "カラマネロ": {"通常": "malamar-mega"},
    "ガメノデス": {"通常": "barbaracle-mega"},
    "ドラミドロ": {"通常": "dragalge-mega"},
    "ルチャブル": {"通常": "hawlucha-mega"},
    "ジガルデ": {"通常": "zygarde-mega"},
    "ジジーロン": {"通常": "drampa-mega"},
    "タイレーツ": {"通常": "falinks-mega"},
    "ライチュウ": {"X": "raichu-mega-x", "Y": "raichu-mega-y"},
    "チリーン": {"通常": "chimecho-mega"},
    "ムクホーク": {"通常": "staraptor-mega"},
    "ヒードラン": {"通常": "heatran-mega"},
    "ダークライ": {"通常": "darkrai-mega"},
    "ゴルーグ": {"通常": "golurk-mega"},
    "ニャオニクス": {"通常": "meowstic-mega"},
    "ケケンカニ": {"通常": "crabominable-mega"},
    "グソクムシャ": {"通常": "golisopod-mega"},
    "マギアナ": {"通常": "magearna-mega", "オリジナル": "magearna-original-mega"},
    "ゼラオラ": {"通常": "zeraora-mega"},
    "スコヴィラン": {"通常": "scovillain-mega"},
    "キラフロル": {"通常": "glimmora-mega"},
    "シャリタツ": {"そった": "tatsugiri-curly-mega", "たれた": "tatsugiri-droopy-mega", "のびた": "tatsugiri-stretchy-mega"},
    "セグレイブ": {"通常": "baxcalibur-mega"}
}