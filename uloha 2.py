def preklad(phrase: str) -> str:
    samohlásky = "aeiouy"

def rozlusti_slovo(slovo: str) -> str:
    vysledok = []
    i = 0

while i < len(slovo):
    if slovo[i] in samohlásky:
        result.append(slovo[i])

    if i + 1 < len(slovo) and slovo[i] == slovo[i + 1]:
        i += 2
            else:
                i += 1
    if i + 1 < len(slovo) and slovo[i + 1] in samohlasky:
        i += 2
        else:
            i += 1



