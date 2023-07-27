import sqlite3

dbPath = './2024.db'
outputPath = './mywords.txt'

# Switches for all items

settings = {
    'support': True,  # 助记
    'derivative': True,  # 派生
    'antonym': True,  # 反义
    'phrase': True,  # 词组
    'discrimination': True,  # 辨义
    'related': True,  # 关联
    'example': True,  # 例句
    'unit': True,  # 单元
    'book': True  # 权重
}


# The order of items that appear only once
'''
onceItemOrder = ['support', 'derivative', 'antonym', 'phrase', 'discrimination', 'related', 'unit', 'book']
'''
onceItemOrder = ['unit']

# new line symbol
nl = '。。。。。。'

# 可选

opt = {
    'unit': [lambda unit: f"{nl}from Unit {unit}" if settings['unit'] else ''] ,# 单元
    'support': [lambda supp: f"{nl}助记：{supp}" if settings['support'] and supp else ''],  # 助记
    'derivative': [lambda deri: f"{nl}派生词：{deri}" if settings['derivative'] and deri else ''],  # 派生
    'antonym': [lambda anto: f"{nl}反义词：{anto}" if settings['antonym'] and anto else ''],  # 反义
    'phrase': [lambda phra: f"{nl}词组和短语：{phra}" if settings['phrase'] and phra else ''],  # 词组
    'discrimination': [lambda disc: f"{nl}词义辨析：{disc}" if settings['discrimination'] and disc else ''],  # 辨义
    'related': [lambda rela: f"{nl}关联词：{rela}" if settings['related'] and rela else ''],  # 关联
    'example': [lambda exam: f"{nl}{exam}" if settings['example'] and exam else ''],  # 例句
    'book': [lambda book: f"{nl}属于{book}" if settings['book'] else '']  # 权重
}

# 必须
ess = [
    'word',  # 单词
    'pos',  # 词性
    'meaning'  # 释义
]

sql = f"SELECT {','.join(ess)},{','.join(opt)} FROM words_all_info;"

# CURD
conn = sqlite3.connect(dbPath)
curs = conn.cursor()
data = list(curs.execute(sql))

# 在读取数据后opt自我改造一下
tuple(map(lambda i, v: opt[v].append(i), *tuple(zip(*enumerate(opt)))))

# 存放单词最终结果
wordsDic = {}

for items in data:
    word, pos, meaning = items[:3]
    inf = items[3:]
    res = {k: opt[k][0](inf[opt[k][1]]) for k in opt}
    posMeaning = pos + ' ' + meaning
    if word in wordsDic:
        wordsDic[word]['pri'] += nl + posMeaning
        #wordsDic[word]['sec'] += res['example']
    else:
        wordsDic[word] = {
            'pri': posMeaning,
            #'sec': f"{nl*2}例句：{res['example']}",
            'once': nl.join([res[k] for k in onceItemOrder])
        }

# 按照欧路词典格式生成文件
with open(outputPath, 'w', encoding='utf-8') as f:
    for item in ('。。。。。。。。。。。。。。' + ''.join([wordsDic[word][k] for k in wordsDic[word]]) + '。。。。。。。。。。。。。。\n' for word in wordsDic):
        f.write(item)

# 释放资源
curs.close()
conn.close()