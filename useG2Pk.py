"""
!pip install jamo
!pip install python-mecab-ko
!pip install konlpy
!pip install nltk
!pip install g2pk
"""

from g2pk import G2p
from tqdm import tqdm


def convert_g2pk_scripts(scripts):
    g2pk_scripts = []
    g2p = G2p()
    for idx, item in enumerate(scripts):
        script = item[0]
        label = item[1]
        temp = g2p(script)
        g2pk_scripts.append([temp, label])
        temp = g2p(script, descriptive=True)
        g2pk_scripts.append([temp, label])
        temp = g2p(script, group_vowels=True)
        g2pk_scripts.append([temp, label])
        temp = g2p(script, to_syl=False)
        g2pk_scripts.append([temp, label])

    return g2pk_scripts


def convert_g2pk_scripts_pandas(scripts):
    g2pk_scripts = []
    g2p = G2p()
    for index, row in tqdm(scripts.iterrows()):
        script = row['x']
        label = row['y']
        temp = g2p(script)
        g2pk_scripts.append([temp, label])
        temp = g2p(script, descriptive=True)
        g2pk_scripts.append([temp, label])
        temp = g2p(script, group_vowels=True)
        g2pk_scripts.append([temp, label])
        temp = g2p(script, to_syl=False)
        g2pk_scripts.append([temp, label])

    return g2pk_scripts





