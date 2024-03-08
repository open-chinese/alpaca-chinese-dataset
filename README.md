# Alpaca Chinese Dataset 中文指令微调数据集【持续更新】

### 当前状态

目前整体翻译已经完成，质量大概为85/100左右，可以用来做中文fine tuning了，但后续希望可以持续更新到98分/100分质量的数据集。欢迎更多更多朋友可以参与到此项目中来。


### 数据集说明
本数据集包括中文和英文的混合数据集，方便双语微调，以及后续做持续的数据修正。

原始的Alpaca英文数据集也存在不少的问题，个别的数学类的sample是错的，有少部分output字段需要修正，一些<noinput>的标签没有对齐等。本数据集会对原始的数据集进行修改和修正。再此基础上，翻译出对应的中文版本，中文版基本是原始sample的翻译，但是对于一些比如押韵类、时态类的一些instruction，直接翻译导致韵脚丢失，时态不一致等。需要对应的进行人工改写。主要分为以下几个方面：

- 1. 修改原始英文数据集的一些问题

- 2. 翻译为中文数据集

- 3. 调整直译导致的一些sample

- 4. code等一些特殊的输出不进行翻译

- 5. 对齐一些特殊的标签<noinput> 或者拒绝生成等输出



### 格式说明
数据集为json dump的json文件，一个sample包括6个字段，en_instruction, en_input, en_output是英文对应的三个字段，instruction, input, output是中文对应的三个字段。
```json
{
    "en_instruction": "Conver the temperature from Fahrenheit to Celsius.",
    "instruction": "将温度从华氏度调到摄氏度。",
    "en_input": "94F",
    "input": "94F",
    "en_output": "34.4C",
    "output": "34.4摄氏度"
}
```


### 文件说明


| Dataset   |      file      |  notes |
|:----------:|:-------------:|:------:|
| alpaca-chinese |  alpaca-chinese-52k.json | 包含了52k英文和中文的数据全集 |
| alpaca-chinese |  ./data/alpaca_chinese_part*.json | 分拆数据文件 |



### 一些修改说明

**Case1** 成语：有一些sample，直译后需要进行二次改写，例如成语类的
```json
{
    "en_instruction": "What is the meaning of the following idiom?",
    "instruction": "以下成语是什么意思？",
    "en_input": "It’s raining cats and dogs",
    "input": "倾盆大雨",
    "en_output": "The idiom \"it’s raining cats and dogs\" means that it is raining heavily.",
    "output": "成语“倾盆大雨”的意思是雨下得像盆里得水往下倒，形容雨大势急。"
}
```

**Case2** 数学题，一些英文的sample是错误的，我们需要先修改后，再翻译。

原始如下，解是一个无理数，我们直接把题目改一下：
```json
{
    "en_instruction": "Find the solution to the quadratic equation.",
    "instruction": "求二次方程的解。",
    "en_input": "3x² + 7x - 4 = 0",
    "input": "3x² + 7x - 4 = 0",
    "en_output": "The solution of the quadratic equation is x = -4 and x = 1/3.",
    "output": "二次方程的解是 x = -4 和 x = 1/3。"
}
```
修改后如下：
```json
{
    "en_instruction": "Find the solution to the quadratic equation.",
    "instruction": "求二次方程的解。",
    "en_input": "2x² - x - 10 = 0",
    "input": "2x² - x - 10 = 0",
    "en_output": "The solution of the quadratic equation is x = -2 and x = 5/2.",
    "output": "二次方程的解是 x = -2 和 x = 5/2。"
}
```

**Case3** 字数限定
原始
```json
{
    "en_instruction": "Compose a five word sentence describing your day.",
    "instruction": "写一个五个字的句子来描述你的一天。",
    "en_input": "",
    "input": "",
    "en_output": "Today was an amazing day.",
    "output": "今天是令人惊喜的一天"
}
```

修改后：
```json
{
    "en_instruction": "Compose a five word sentence describing your day.",
    "instruction": "写一个五个字的句子来描述你的一天。",
    "en_input": "",
    "input": "",
    "en_output": "Today was an amazing day.",
    "output": "今天真美好"
}
```

**Case4** 拆字
原始：
```json
{
    "en_instruction": "Find a five-letter word that begins with 'd' and ends with 's'.",
    "instruction": "找到一个以“d”开头并以“s”结尾的五个字母的单词。",
    "en_input": "",
    "input": "",
    "en_output": "davis.",
    "output": "戴维斯。"
}
```
修改后：
```json
{
    "en_instruction": "Find a five-letter word that begins with 'd' and ends with 's'.",
    "instruction": "一个木字一个羽毛的羽是什么字。",
    "en_input": "",
    "input": "",
    "en_output": "davis.",
    "output": "栩栩如生的栩(xǔ)"
}
```

**Case5** 本地化
```json
{
    "en_instruction": "Name one social networking website",
    "instruction": "说出一个社交网站",
    "en_input": "",
    "input": "",
    "en_output": "Facebook.",
    "output": "微博"
}
```


### 维护成员列表

在上述【数据集说明】中提到，数据集的英文和中文内容仍然存在一些问题，为了提升数据集质量，将52002个sample数据集拆分为53个split的json文件，感兴趣的朋友可以认领部分文件的维护，并接受pull request来更新数据文件。
目标是希望将英文和中文两个数据集都提高到人工生成的数据集质量水平。


|       编号       |       文件        |                维护成员                 |     进度      |
|:--------------:|:-------------------------:|:------------------------------------------------------------------------:|:---------------------:|
| 0 |  [./data/alpaca_chinese_part_0.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_0.json)| [OpenChinese](https://github.com/open-chinese) | ![](https://geps.dev/progress/100) |
| 1 |  [./data/alpaca_chinese_part_1.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_1.json) |[OpenChinese](https://github.com/open-chinese) | ![](https://geps.dev/progress/100) |
| 2 |  [./data/alpaca_chinese_part_2.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_2.json) |[OpenChinese](https://github.com/open-chinese) | ![](https://geps.dev/progress/100) |
| 3 |  [./data/alpaca_chinese_part_3.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_3.json) |[OpenChinese](https://github.com/open-chinese) | ![](https://geps.dev/progress/50) |
| 4 |  [./data/alpaca_chinese_part_4.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_4.json) |[OpenChinese](https://github.com/open-chinese) | ![](https://geps.dev/progress/0) |
| 5 |  [./data/alpaca_chinese_part_5.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_5.json) |[OpenChinese](https://github.com/open-chinese) | ![](https://geps.dev/progress/0) |
| 6 |  [./data/alpaca_chinese_part_6.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_6.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 7 |  [./data/alpaca_chinese_part_7.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_7.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 8 |  [./data/alpaca_chinese_part_8.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_8.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 9 |  [./data/alpaca_chinese_part_9.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_9.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 10 |  [./data/alpaca_chinese_part_10.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_10.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 11 |  [./data/alpaca_chinese_part_11.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_11.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 12 |  [./data/alpaca_chinese_part_12.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_12.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 13 |  [./data/alpaca_chinese_part_13.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_13.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 14 |  [./data/alpaca_chinese_part_14.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_14.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 15 |  [./data/alpaca_chinese_part_15.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_15.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 16 |  [./data/alpaca_chinese_part_16.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_16.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 17 |  [./data/alpaca_chinese_part_17.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_17.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 18 |  [./data/alpaca_chinese_part_18.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_18.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 19 |  [./data/alpaca_chinese_part_19.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_19.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 20 |  [./data/alpaca_chinese_part_20.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_20.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 21 |  [./data/alpaca_chinese_part_21.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_21.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 22 |  [./data/alpaca_chinese_part_22.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_22.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 23 |  [./data/alpaca_chinese_part_23.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_23.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 24 |  [./data/alpaca_chinese_part_24.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_24.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 25 |  [./data/alpaca_chinese_part_25.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_25.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 26 |  [./data/alpaca_chinese_part_26.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_26.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 27 |  [./data/alpaca_chinese_part_27.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_27.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 28 |  [./data/alpaca_chinese_part_28.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_28.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 29 |  [./data/alpaca_chinese_part_29.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_29.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 30 |  [./data/alpaca_chinese_part_30.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_30.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 31 |  [./data/alpaca_chinese_part_31.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_31.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 32 |  [./data/alpaca_chinese_part_32.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_32.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 33 |  [./data/alpaca_chinese_part_33.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_33.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 34 |  [./data/alpaca_chinese_part_34.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_34.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 35 |  [./data/alpaca_chinese_part_35.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_35.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 36 |  [./data/alpaca_chinese_part_36.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_36.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 37 |  [./data/alpaca_chinese_part_37.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_37.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 38 |  [./data/alpaca_chinese_part_38.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_38.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 39 |  [./data/alpaca_chinese_part_39.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_39.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 40 |  [./data/alpaca_chinese_part_40.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_40.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 41 |  [./data/alpaca_chinese_part_41.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_41.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 42 |  [./data/alpaca_chinese_part_42.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_42.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 43 |  [./data/alpaca_chinese_part_43.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_43.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 44 |  [./data/alpaca_chinese_part_44.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_44.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 45 |  [./data/alpaca_chinese_part_45.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_45.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 46 |  [./data/alpaca_chinese_part_46.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_46.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 47 |  [./data/alpaca_chinese_part_47.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_47.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 48 |  [./data/alpaca_chinese_part_48.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_48.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 49 |  [./data/alpaca_chinese_part_49.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_49.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 50 |  [./data/alpaca_chinese_part_50.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_50.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 51 |  [./data/alpaca_chinese_part_51.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_51.json) | 等待认领 | ![](https://geps.dev/progress/0) |
| 52 |  [./data/alpaca_chinese_part_52.json](https://github.com/open-chinese/alpaca-chinese-dataset/blob/main/data/alpaca_chinese_part_52.json) | 等待认领 | ![](https://geps.dev/progress/0) |



