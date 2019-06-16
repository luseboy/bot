import nltk
import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('--------------Programs-------------')


















#nltk.download()

base = [('qual é o pacote prime?', '!prime'),
        ('como é o pacote prime?', '!prime'),
        ('puxa ai?', '!puxa'),
        ('pode puxar?', '!puxa'),
        ('quanto custa o prime?', '!prime'),
        ('como posso adquirir o pacote prime?', '!prime'),
        ('quero comprar o pacote prime como posso adquirir?', '!prime'),
        ('qual é o pacote limitado?', '!limitado'),
        ('como é o pacote limitado?', '!limitado'),
        ('como posso adquirir o pacote limitado?', '!limitado'),
        ('quero comprar o pacote limitado como posso adquirir?', '!limitado'),
        ('qual é o pacote pro?', '!pro'),
        ('como é o pacote pro?', '!pro'),
        ('como é o pacote pro?', '!pro'),
        ('quero comprar o pacote pro como posso adquirir??', '!pro')]

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')


# print(stopwordsnltk)

def removestopword(texto):
    frases = []
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwords]
        frases.append((semstop, emocao))
    return frases


def aplicastemer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasessstemming = []
    for (palavras, emocao) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwords]
        frasessstemming.append((comstemming, emocao))
    return frasessstemming


frasescomstemming = aplicastemer(base)


# print((frasescomstemming))


def buscapalavras(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras


palavras = buscapalavras((frasescomstemming))


# print(palavras)


def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras


frequencia = buscafrequencia((palavras))


# print(frequencia.most_common(50))


def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq


palavrasunicas = buscapalavrasunicas((frequencia))


# print(palavrasunicas)


def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasunicas:
        caracteristicas['"%s' % palavras] = (palavras in doc)
    return caracteristicas


caracteristicasfrase = extratorpalavras(['am', 'nov', 'ia'])

# print(caracteristicasfrase)

basecompleta = nltk.classify.apply_features(extratorpalavras, frasescomstemming)
# print(basecompleta[5])

classificador = nltk.NaiveBayesClassifier.train((basecompleta))
# print(classificador.show_most_informative_features(5))

@client.event
async def on_message(message):
    if message.author.bot:
        return
      # metin = message.content.mentions[0]
      # print(metin)

    if client.user.mention in message.content and str(message.channel.id) == "568870659757703200":
        mensagem = message.content[0:100]
        print(mensagem)
        testestemming = []
        teste = mensagem
        stemmer = nltk.stem.RSLPStemmer()
        for (palavras) in teste.split():
            comstem = [p for p in palavras.split()]
            testestemming.append(str(stemmer.stem(comstem[0])))

        novo = extratorpalavras(testestemming)
        print(classificador.classify(novo))
        resul = classificador.classify(novo)

        distribuicao = classificador.prob_classify(novo)
        for classe in distribuicao.samples():
            print("%s: %f" % (classe, distribuicao.prob(classe)))

        if resul == "!pro":
            await message.channel.send(
                "O pacote **PRO** custa **150** reais. Te ofereçe vídeo-aulas de todos os professores: **Tony, Pulga, Zotie, Barbosa e Taizun.** São vídeo-aulas que são focadas no **CENÁRIO PROFISSIONAL** passando dicas e ideias sobre **SCRIMS** e outros fatores avançados. Você terá vários benefícios, dentre eles: Você ganha a tag  *PRO BØYS* que te dá acesso a salas da Staff da comunidade da THE BØYS *(somente BIG 2 pra baixo)*,  além também de ganhar a tag *SCHØØL BOYS* que te dá acesso a sala de voz *SCHØØL LOUNGE* e ao chat de texto *school-pvt* que é o chat privado para os alunos da Boys Academy. Você também poderá participar dos futuros campeonatos exclusivos para os alunos, eles serão informados com aviso prévio.\n\n**Link para compra:** https://www.boysacademy.com.br/loja/Pacote-Pro-p133683088")
        elif resul == "!limitado":
            await message.channel.send(
                "O pacote **LIMITADO** custa **30** reais. Te ofereçe video-aulas de um professor de sua escolha, dentre os cinco: **Tony, Pulga, Barbosa, Zotie e Taizun.** Você terá vários benefícios, dentre eles: Você ganha a tag *SCHOOL BOYS* que te dá acesso a sala de voz *SCHØØL LOUNGE* e ao chat de texto *school-pvt* que é o chat privado para os alunos da Boys Academy. Você também poderá participar dos futuros campeonatos exclusivos para os alunos, eles serão informados com aviso prévio.\n\n**Link para compra:** https://www.boysacademy.com.br/loja/Pacote-Limitado-p113604093")
        elif resul == "!prime":
            await message.channel.send(
                "O pacote **PRIME** custa **100** reais. Te ofereçe video-aulas de todos os seguintes professores: **Tony, Pulga, Zotie, Barbosa e Taizun.** Vídeo-aulas que são focadas em fatores de **Mira/Construção/Movimentação**. Você terá vários benefícios, dentre eles: Você ganha a tag *SCHOOL BOYS* que te dá acesso a sala de voz *SCHØØL LOUNGE* e ao chat de texto *school-pvt* que é o chat privado para os alunos da Boys Academy. Você também poderá participar dos futuros campeonatos exclusivos para os alunos, eles serão informados com aviso prévio.\n\n**Link para compra:** https://www.boysacademy.com.br/loja/Pacote-Prime-p113604094 ")
        elif resul == "!puxa":
            await message.channel.send(
                "Vai tomar no cu mano")


client.run('NTg5ODE0Mjg3MDQwNTEyMDIw.XQZbyg.dkbl44UbZsYRn2rA8qYJQBuI6KI')
