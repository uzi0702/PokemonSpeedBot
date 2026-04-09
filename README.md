# このボットについて 
このボットはポケモンの素早さを素早く参照することを目的として作成しました。
具体的には「ポケモン名、速さ（最速、準速、無振り、下降、最遅の5段階のいずれか）」と入力することでそのポケモンの素早さ実数値およびランク補正後の素早さを返します。
ポケモン名と速さの間の点は全角でも半角でも反応します。また、ポケモン名はひらがなでもカタカナでも、またひらがなとカタカナが混じっていても反応します。

## 追記（2026/4/9）
ポケモンchampions対応のため、最遅に対しても個体値31で計算するように変更いたしました。

# 使い方　
1.「!p」をボットを使いたいチャンネルで打ち込み、ボットを起動状態にする<br>
2.「ポケモン名、速さ（最速、準速、無振り、下降、最遅の5段階のいずれか」の文字列を打ち込むとポケモンの素早さ実数値が返答される。

なお、ポケモン名および速さが間違っている場合は警告文を返します。

例：
```
!p #bot起動
リザードン、最速
オオダイル、準速
ハガネール、最遅
```

# フォルム違いポケモン
1.複数のフォルム（ランドロスの化身、霊獣）、リージョンフォームがあるポケモンはポケモン名と速さの段階の間に区切り文字（、,）を入れて、リージョン名を指定してください。

例1：ランドロス、霊獣、最速 #間にフォルム名を入れて区切り文字

例2：リザードン、X、準速  #メガリザードンXの場合

例3：フシギバナ、通常、無振り #メガフシギバナの場合

対応しているフォルム違い
```
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
```
メガ進化
```
MEGA_MAP = {
    "リザードン": {"X": "charizard-mega-x", "Y": "charizard-mega-y"},
    "ミュウツー": {"X": "mewtwo-mega-x", "Y": "mewtwo-mega-y"},
    "フシギバナ": {"通常": "venusaur-mega"},
    "カメックス": {"通常": "blastoise-mega"},
    "スピアー": {"通常": "beedrill-mega"},
    "ピジョット": {"通常": "pidgeot-mega"},
    "フーディン": {"通常": "alakazam-mega"},
    "ヤドラン": {"通常": "slowbro-mega"},
    "ゲンガー": {"通常": "gengar-mega"},
    "ガルーラ": {"通常": "kangaskhan-mega"},
    "カイロス": {"通常": "pinsir-mega"},
    "ギャラドス": {"通常": "gyarados-mega"},
    "プテラ": {"通常": "aerodactyl-mega"},
    "デンリュウ": {"通常": "ampharos-mega"},
    "ハガネール": {"通常": "steelix-mega"},
    "ハッサム": {"通常": "scizor-mega"},
    "ヘラクロス": {"通常": "heracross-mega"},
    "ヘルガー": {"通常": "houndoom-mega"},
    "バンギラス": {"通常": "tyranitar-mega"},
    "ジュカイン": {"通常": "sceptile-mega"},
    "バシャーモ": {"通常": "blaziken-mega"},
    "ラグラージ": {"通常": "swampert-mega"},
    "サーナイト": {"通常": "gardevoir-mega"},
    "ヤミラミ": {"通常": "sableye-mega"},
    "クチート": {"通常": "mawile-mega"},
    "ボスゴドラ": {"通常": "aggron-mega"},
    "チャーレム": {"通常": "medicham-mega"},
    "ライボルト": {"通常": "manectric-mega"},
    "サメハダー": {"通常": "sharpedo-mega"},
    "バクーダ": {"通常": "camerupt-mega"},
    "チルタリス": {"通常": "altaria-mega"},
    "ジュペッタ": {"通常": "banette-mega"},
    "アブソル": {"通常": "absol-mega"},
    "ボーマンダ": {"通常": "salamence-mega"},
    "メタグロス": {"通常": "metagross-mega"},
    "ラティオス": {"通常": "latios-mega"},
    "ラティアス": {"通常": "latias-mega"},
    "レックウザ": {"通常": "rayquaza-mega"},
    "ミミロップ": {"通常": "lopunny-mega"},
    "ガブリアス": {"通常": "garchomp-mega"},
    "ルカリオ": {"通常": "lucario-mega"},
    "ユキノオー": {"通常": "abomasnow-mega"},
    "エルレイド": {"通常": "gallade-mega"},
    "タブンネ": {"通常": "audino-mega"},
    "ディアンシー": {"通常": "diancie-mega"}
}
```

# 使用させていただいているサイト
・Pokeapi様[https://pokeapi.co/]<br>
素早さ種族値を取得するために使用させていただいております。

