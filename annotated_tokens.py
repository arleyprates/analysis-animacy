def initialize_variables():
    global corpus
    corpus = open('corpus.txt', 'r').read() 

    global index
    index = 0

    global H_tokens
    global A_tokens
    global I_tokens

    H_tokens = []
    A_tokens = []
    I_tokens = []


def token():
    tk = ''
    global index
    global corpus
    if corpus[index] == '(' or corpus[index] == '"' or corpus[index] == '—' or corpus[index] == '\n' or corpus[index] == ' ':
        i = index + 1
    else:
        i = index
    while(i < len(corpus) and corpus[i] != '…' and corpus[i] != ' ' and corpus[i] != '.' and corpus[i] != ',' and corpus[i] != '"' and corpus[i] != ')' and corpus[i] != '?' and corpus[i] != '!' and corpus[i] != '!' and corpus[i] != '—' and corpus[i] != '”' and corpus[i] != '\n' and corpus[i] != '“' and corpus[i] != '’' and corpus[i] != '‘'):
        tk += corpus[i]
        i += 1
    i +=1
    
    global H_tokens
    global A_tokens
    global I_tokens
    
    if tk:
        if 'H_' == tk[0:2]:
            H_tokens.append(tk[2:])
        elif 'A_' == tk[0:2]:
            A_tokens.append(tk[2:])
        else:
            I_tokens.append(tk)

    index = i
    return(tk)

def main():
    initialize_variables()
    global corpus
    while index < len(corpus):
        print(token())
    print(H_tokens)
    print(len(A_tokens))
    print(len(I_tokens))

main()
'''
for i in range(0,len(corpus)):
    if corpus[i] == ' ':

    if corpus[i] == '_':
        if corpus[i-1] == 'H'
'''
