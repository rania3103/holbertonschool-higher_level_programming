#!/usr/bin/python3
"""a function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """" print text with 2lines in case of finding .?: in
    the text or an error msg in case of error"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        res = ""
        for i in range(len(text)):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                res += text[i] + "\n\n"
            else:
                res += text[i]
        print(res, end="")
text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")