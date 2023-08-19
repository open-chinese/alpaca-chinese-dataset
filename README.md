# Alpaca Chinese Dataset 中文指令微调数据集【持续更新】

### 加入项目

在大模型兴起之后，随着我花越来越多的时间在这个方向的学习和工作上，也越是发现开源中文数据集的匮乏。因此希望又更多的人可以参与进来。

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
| alpaca-chinese |  alpaca-chinese-52k.json | 包含了52k英文和中文的数据 |


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


