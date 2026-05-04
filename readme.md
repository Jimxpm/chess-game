# Python 西洋棋 

以基礎 Python 語法實作西洋棋邏輯, 搭配 Pygame 函式庫建立 UI, 將遊戲規則與 UI 分離設計

## 目前進度

* **基本西洋棋規則**：棋盤設置和各兵種走法，王車易位、升變待補
* **圖形化互動介面**：透過 Pygame 實作滑鼠點選、棋子拖曳等基本互動。

## 架構
```text
chess-game/
├── main.py          
├── board.py         # 棋盤資料與狀態
├── rules.py         # 棋子移動規則判定
├── ui/
│   └── gui.py       # Pygame 介面設置
├── icon/          # 存放棋子圖片
└── requirements.txt 
```

## 使用方式

```bash
pip install -r requirements.txt
python main.py