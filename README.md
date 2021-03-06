# Pyxel Play Gound

いろいろなジャンルのゲームを実装してみよう．

| ジャンル                          | 説明                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| **RPG（ロールプレイングゲーム）** | 勇者などになってイベントが進行．<br />例：ポケモン，風来のシレン，ゼルダ |
| **STG（シューティングゲーム）**   | 攻撃をよけながら敵を打つ．<br />例：R-type，東方，CoD，バイオ |
| **ACT（アクションゲーム）**       | キャラクターをうまく動かす．<br />例：マリオ                 |
| **ADV（アドベンチャーゲーム）**   | 会話パートが中心．<br />例：シュタゲ，逆転裁判               |
| **PZL（パズルゲーム）**           | パズル．<br />例：倉庫番，テトリス，キャンディークラッシュ，Portal |
| **SLG（シミュレーションゲーム）** | 疑似体験や自由度の高さ．<br />例：マイクラ，                 |
| **RCG（レーシングゲーム）**       | 乗り物に乗ってスピードを競う．                               |



# 実装例

## RPG

日本のRPG（JRPG）っぽいもの．以下のコアな機能を実装．一番かんたんな実装．

- 移動する
- 当たり判定
- 話しかける

<img src="README.assets/RPG.gif" alt="RPG" style="zoom:200%;" />

さらに発展として以下の機能を実装．

- [x] スプライトが移動方向に向く
- [ ] 大きなマップの読み込み
- [ ] キャラクターのアニメーション
- [ ] NPC（操作しないキャラクター）の移動



## STG

最もかんたんなインベーダーゲームっぽいもの．以下のコアな機能を実装．

- 移動する
- 弾を発射する
- パーティクルの発生

![STG](README.assets/STG.gif)

さらに発展として以下の機能を実装．

- [x] 背景のスクロール
- [x] ライフポイント
- [ ] アイテムの取得
- [ ] オブジェクトの再利用（オブジェクトプーリング）
- [ ] 効率的な当たり判定



## ADV

単純な脱出ゲーム．

- マウスで動かす
- クリックしてものを調べる
- かぎを見つけたら出られる

![ADV](README.assets/ADV.gif)

さらに発展として

- [ ] 文章を外部ファイルに保存
- [ ] 複数Sceneの遷移
- [ ] 押した回数によってテキストや絵が変わる



## PZL

シンプルなLights Out を実装した．ルールはこんな感じ．

- 5x5のマス目のライトがすべてOFFになっている
- マスを押すと上下左右のライトのON/OFFが反転する
- すべてONにするとクリア

![PZL](README.assets/PZL.gif)

さらに発展として，

- [ ] ハイスコアを外部に保存する
- [ ] N x N の解答のひとつをアルゴリズムで求める
- [ ] 間違えた時に戻ったり進める機能