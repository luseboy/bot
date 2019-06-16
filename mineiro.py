# dependencias
import nltk
import discord
import asyncio

client = discord.Client()

# evento do bot ficar online
@client.event
async def on_ready():
    print('O BOT FOI INICIADO COM SUCESSO!')
    print('BØYS ACADEMY v1.4')
    await client.change_presence(activity=discord.Streaming(name="BØYS ACADEMY", url='https://www.twitch.tv/luseboy_'))

        #nltk.download()

# base do bot
# pacote prime
base = [('qual é o pacote prime?', '!prime'),
        ('como é o pacote prime?', '!prime'),
        ('quanto custa o prime?', '!prime'),
        ('como posso adquirir o pacote prime?', '!prime'),
        ('quero comprar o pacote prime como posso adquirir?', '!prime'),
        ('o que inclui o pacote prime?', '!prime'),
        ('o pacote prime tem quais beneficios?', '!prime'),
        ('o que eu ganho com o pacote prime?', '!prime'),
        ('quais os professores do pacote prime?', '!prime'),
        ('o que eu recebo no pacote  prime?', '!prime'),
        ('qual o maior forte do pacote prime?', '!prime'),
        ('pacote mediano', '!prime'),
        ('quanto custa o pacote prime?', '!prime'),
        ('onde eu compro o pacote prime?', '!prime'),
        ('onde eu adquiro o pacote prime?', '!prime'),
        ('qual o link para comprar o pacote prime?', '!prime'),
        ('eu quero um pacote mediano, qual vc me oferece?', '!prime'),
        ('pacote mediano', '!prime'),
        ('sou um player razoável, qual pacote me recomenda?', '!prime'),
        ('jogador razoável', '!prime'),
        ('sou mediano, qual me recomenda?', '!prime'),
        ('sou um jogador mediano, qual me recomenda?', '!prime'),
        ('sou mediano, pacote eu compro?', '!prime'),
        ('me explique como funciona o pacote prime', '!prime'),
        ('pacote prime', '!prime'),
        ('pacote 100 reais', '!prime'),
        ('quais os benefícios do pacote prime', '!prime'),
        ('quais os beneficios do pacote prime?', '!prime'),
        ('beneficios prime?', '!prime'),
        ('beneficios do pacote prime', '!prime'),
        ('vantagens do pacote prime', '!prime'),
        ('me fala sobre o prime', '!prime'),
        ('qual o pacote mediano?', '!prime'),
        ('o que está incluso no pacote prime?', '!prime'),
        ('no pacote prime, vcs visam ensinar mais o que?', '!prime'),
        ('o que é ensinado no pacote prime?', '!prime'),
        ('no pacote prime, os videos de voces visam ensinar o que?', '!prime'),
        ('o que é repassado no pacote prime?', '!prime'),
        ('prime', '!prime'),
        ('prime', '!prime'),
        ('como funciona as aulas prime?', '!prime'),
        ('como funciona as aulas prime', '!prime'),
        ('aulas prime', '!prime'),
        ('oque tem no pacote prime?', '!prime'),
        ('queria saber qual pacote vc me recomenda, comecei a jogar hoje', '!prime'),
        ('acabei de começar a jogar , qual pacote você me recomenda', '!prime'),
        ('Galera, boa noite. Quais são os benefícios no discord pro pacote prime ?', '!prime'),
        ('qual pacote tem video aula com todos os professores', '!prime'),
        ('Qual é o conteúdo que vem no pacote prime?', '!prime'),
        ('o que tem no pacote prime?', '!prime'),
        ('oque tem no pacote prime?', '!prime'),
        ('oq tem no pacote prime?', '!prime'),
        ('que tem nesse pacote prime?', '!prime'),
        ('o que há no pacote prime?', '!prime'),
        ('pacote prime?', '!prime'),
        ('o que tem no pacote prime?', '!prime'),
        ('tem o que no pacote prime?', '!prime'),
        ('que tem no pacote prime?', '!prime'),
        ('quem compra o pacote prime, ganha algum cargo?', '!prime'),

        # pacote limitado
        ('pacote mais básico', '!limitado'),
        ('básico pacote', '!limitado'),
        ('qual é o pacote limitado?', '!limitado'),
        ('como é o pacote limitado?', '!limitado'),
        ('como posso adquirir o pacote limitado?', '!limitado'),
        ('quero comprar o pacote limitado como posso adquirir?', '!limitado'),
        ('qual o pacote mais barato?', '!limitado'),
        ('quero comprar o pacote limitado', '!limitado'),
        ('pacote limitado?', '!limitado'),
        ('o que inclui o pacote limitado?', '!limitado'),
        ('quanto custa o pacote mais barato?', '!limitado'),
        ('quanto custa o pacote limitado?', '!limitado'),
        ('pacote iniciante', '!limitado'),
        ('pacote mais básico', '!limitado'),
        ('o que eu ganho no pacote ilimitado?', '!limitado'),
        ('sou iniciante, que pacote eu compro?', '!limitado'),
        ('gostaria de comprar o pacote limitado, qual o link?', '!limitado'),
        ('qual pacote vc me recomenda? sou iniciante no jogo', '!limitado'),
        ('pacote pra noob', '!limitado'),
        ('pacote pra nub', '!limitado'),
        ('como e o  pacote de 30', '!limitado'),
        ('pacote limitado', '!limitado'),
        ('pacote de 30 reais', '!limitado'),
        ('quais os benefícios do pacote limitado?', '!limitado'),
        ('beneficios limitado', '!limitado'),
        ('vantagens do pacote limitado', '!limitado'),
        ('beneficios do pacote limitado', '!limitado'),
        ('quais os beneficios do pacote limitado?', '!limitado'),
        ('me fala sobre o limitado', '!limitado'),
        ('sou um player ruim, qual pacote vc me recomenda?', '!limitado'),
        ('limitado', '!limitado'),
        ('limitado', '!limitado'),
        ('como funciona as aulas limitado?', '!limitado'),
        ('como funciona as aulas limitada?', '!limitado'),
        ('pacote limitado', '!limitado'),
        ('beneficios limitado para o discord', '!limitado'),
        ('como funciona as aulas limitadas?', '!limitado'),
        ('como funciona as aulas do limitado?', '!limitado'),
        ('oque tem no pacote limitado?', '!limitado'),
        ('oque tem  pacote limitado?', '!limitado'),
        ('que tem no pacote limitado?', '!limitado'),
        ('o que há no pacote limitado?', '!limitado'),
        ('oq tem no pacote limitado?', '!limitado'),
        ('limitado', '!limitado'),
        ('limitad', '!limitado'),

        # pacote pro
        ('qual é o pacote pro?', '!pro'),
        ('quero comprar o pacote avançado', '!pro'),
        ('como é o pacote pro?', '!pro'),
        ('quero comprar o pacote pro como posso adquirir??', '!pro'),
        ('desejo o pacote pro', '!pro'),
        ('como funciona o pacote pro?', '!pro'),
        ('onde eu compro o pacote pro?', '!pro'),
        ('qual o melhor pacote?', '!pro'),
        ('qual o pacote que você me recomenda?', '!pro'),
        ('o pacote pro é bom?', '!pro'),
        ('vale a pena comprar o pacote pro?', '!pro'),
        ('onde vou para comprar o pacote pro?', '!pro'),
        ('como funciona o pacote pro?', '!pro'),
        ('o que eu ganho com o pacote pro?', '!pro'),
        ('quais os beneficios do pacote pro?', '!pro'),
        ('o que o pacote pro inclui?', '!pro'),
        ('qual o pacote mais avançado?', '!pro'),
        ('qual o pacote mais completo e melhor?', '!pro'),
        ('profissional?', '!pro'),
        ('sou um player profissional, qual pacote devo comprar para eu melhorar mais ainda?', '!pro'),
        ('pacote para scrims? profissional', '!pro'),
        ('qual pacote eu devo comprar para me tornar um bom jogador?', '!pro'),
        ('quero um pacote focado em scrims?', '!pro'),
        ('sou um player avançado, qual me recomenda?', '!pro'),
        ('sou um jogador avançado, qual pacote vc me recomenda?', '!pro'),
        ('nivel tonyboy', '!pro'),
        ('nivel pulgaboy', '!pro'),
        ('jogar igual tonyboy', '!pro'),
        ('jogar igual pulgaboy', '!pro'),
        ('quero jogar igual os boys, qual eu compro?', '!pro'),
        ('nivel barboysa', '!pro'),
        ('nivel barbosa', '!pro'),
        ('quero o melhor pacote, qual eu compro?', '!pro'),
        ('quero jogar igual os the boys, qual pacote eu compro?', '!pro'),
        ('qual pacote vc me recomenda?', '!pro'),
        ('O pacote pro inclui oq tanto?', '!pro'),
        ('Man eu ja tenho uma noção de jogo qual pacote eu compro?', '!pro'),
        ('Oque tem no pacote pro?', '!pro'),
        ('pacote pro', '!pro'),
        ('pacote de 150 reais', '!pro'),
        ('me fala os benefícios do pacote pro', '!pro'),
        ('beneficios do pacote pro', '!pro'),
        ('pacote pro beneficios', '!pro'),
        ('quais os beneficios do pacote pro?', '!pro'),
        ('qual os beneficios do pacote pro', '!pro'),
        ('quais as vantagens do pacote pro?', '!pro'),
        ('me fala sobre o pro', '!pro'),
        ('tem algum pacote para players mais avancados?', '!pro'),
        ('pro', '!pro'),
        ('pro', '!pro'),
        ('como funciona as aulas pro?', '!pro'),
        ('queria saber como ficar do nível dos pros?', '!pro'),
        ('beneficios pro para o discord', '!pro'),
        ('Qual é o conteúdo que vem no pacote pro?', '!pro'),
        ('Quanto  custa o pacote pró?', '!pro'),
        ('como funciona o pacote pró?', '!pro'),
        ('como é o pacote pro?', '!pro'),

        # pacotes
        ('Que os pacotes que existem?', '!pacotes'),
        ('que tipos de pacotes tem?', '!pacotes'),
        ('que aulas existem?', '!pacotes'),
        ('qual a diferença do pacote pro para o limitado?', '!pacotes'),
        ('quais os pacotes?', '!pacotes'),
        ('que pacotes estão a venda?', '!pacotes'),
        ('quais as aulas?', '!pacotes'),
        ('pacotes que existem?', '!pacotes'),
        ('pacotes da boys academy?', '!pacotes'),
        ('que tipo são os conteúdos da boys academy?', '!pacotes'),
        ('quais as opções de pacotes que eu tenho?', '!pacotes'),
        ('qual a diferença do pacote pro para o prime?', '!pacotes'),
        ('qual a diferença do pacote prime para o limitado?', '!pacotes'),
        ('qual a diferença do pacote limitado para o pro?', '!pacotes'),
        ('me diz as diferenças sobre os pacotes', '!pacotes'),
        ('queria saber quais pacotes tem', '!pacotes'),
        ('que pacotes tem aqui?', '!pacotes'),
        ('que pacotes posso comprar?', '!pacotes'),
        ('quero comprar as aulas?', '!pacotes'),
        ('onde eu efetuo a compra?', '!pacotes'),
        ('como eu compro os pacotes', '!pacotes'),
        ('pacotes', '!pacotes'),
        (' compro pacote?', '!pacotes'),
        ('quero comprar', '!pacotes'),
        ('quero comprar a boys academy', '!pacotes'),
        ('quero a boys academy', '!pacotes'),
        ('quero efetuar a compra de um pacote', '!pacotes'),
        ('quero comprar', '!pacotes'),
        ('me fala os pacotes', '!pacotes'),
        ('me fala quais os pacotes disponiveis', '!pacotes'),
        ('Pacotes e preços?', '!pacotes'),
        ('pacotes', '!pacotes'),
        ('quais os pacotes q vcs oferecem?', '!pacotes'),
        ('quais os pacotes que estão disponiveis na boys academy?', '!pacotes'),
        ('quanto custa os pacotes ?', '!pacotes'),
        ('qual o preço dos pacotes?', '!pacotes'),
        (' o que é o pacote School ?', '!pacotes'),
        ('Que pacotes que tem?', '!pacotes'),
        ('pacote', '!pacotes'),
        ('comu fasso pra comprar a boys academy ?', '!pacotes'),
        ('como faço pra comprar a boys academy?', '!pacotes'),
        (' q pacotes tem?', '!pacotes'),
        ('quero saber os pacotes', '!pacotes'),
        ('qual o valor?', '!pacotes'),
        ('quanto custa?', '!pacotes'),
        ('oque é ensinado nos videos?', '!pacotes'),
        ('o que eles ensinam nos videos?', '!pacotes'),
        ('o que é ensinado?', '!pacotes'),
        ('quais são os professores?', '!pacotes'),
        ('quem ensina nos videos?', '!pacotes'),
        ('quem posso escolher para me dar aula?', '!pacotes'),
        ('quem é os professores da boys academy?', '!pacotes'),
        ('quem dá aula na boys academy?', '!pacotes'),
        ('quem vai me dar aula?', '!pacotes'),
        ('quais os professores da boys academy?', '!pacotes'),
        ('quem ensina nos videos?', '!pacotes'),
        ('quais professores posso escolher?', '!pacotes'),
        ('tem quantos professores?', '!pacotes'),
        ('quem são os professores?', '!pacotes'),
        ('quem eu posso escolher para ver as aulas?', '!pacotes'),
        ('quem é o professor?', '!pacotes'),
        ('quem me da aula?', '!pacotes'),
        ('que professores tem?', '!pacotes'),
        ('que professores existem?', '!pacotes'),
        ('como funciona?', '!pacotes'),
        ('quais são os pacote?', '!pacotes'),
        ('como funciona?', '!pacotes'),
        ('como funciona a boys academy?', '!pacotes'),
        ('Pacotes em geral', '!pacotes'),
        ('como eu compro?', '!pacotes'),
        ('como eu faço pra compro?', '!pacotes'),
        ('como comprar?', '!pacotes'),
        ('Mano vc pode me passar o preço de cada pacote', '!pacotes'),

        # pagamento, recebimento e horário
        ('quais são as formas de pagamento?', '!pag'),
        ('quais as formas de pagamento?', '!pag'),
        ('qual o horário de atendimento?', '!pag'),
        ('como faz pra receber o produto?', '!pag'),
        ('que horas é o atendimento?', '!pag'),
        ('como faço pra receber o que comprei?', '!pag'),
        ('quando começa o atendimento?', '!pag'),
        ('com quem devo falar para receber o produto?', '!pag'),
        ('como eu faço pra pagar?', '!pag'),
        ('quais os metodos de pagamento?', '!pag'),
        ('por onde eu recebo os videos?', '!pag'),
        ('como é a entrega dos videos?', '!pag'),
        ('quando é o atendimento?', '!pag'),
        ('quando vou receber os videos?', '!pag'),
        ('como faz para gerar o boleto?', '!pag'),
        ('consigo pagar pelo paypal?', '!pag'),
        ('vc acha q demoram mt para responder o atendimento?', '!pag'),
        ('efetuei a compra, com quem eu falo?', '!pag'),
        ('como faço pra receber o pacote?', '!pag'),
        ('aceita paypal?', '!pag'),
        ('tem boleto bancário?', '!pag'),
        ('me explique o pagamento', '!pag'),
        ('me explique o recebimento do produto', '!pag'),
        ('como faz pra receber o produto?', '!pag'),
        ('depois de eu ter comprado o produto, o que eu faço?', '!pag'),
        ('o que faço depois de ter pago?', '!pag'),
        ('o que faço depois de ter comprado?', '!pag'),
        ('quais os tipos de pagamento?', '!pag'),
        ('quais os metodos de pagamentos?', '!pag'),
        ('qual perfil eu chamo pra mandar o comprovante?', '!pag'),
        ('qual perfil eu mando o comprovante?', '!pag'),
        ('o que faço depois de ter comprado o pacote?', '!pag'),
        ('quem eu chamo depois de ter comprando a boys academy?', '!pag'),
        ('como faz pra receber o produto?', '!pag'),
        ('Como que faço pra receber as vídeos aulas online', '!pag'),
        ('onde posso realizar os pagamentos?', '!pag'),
        ('como faço pra pagar?', '!pag'),
        ('quero saber como é que faço pra pagar esse pacote', '!pag'),
        ('posso pagar por boleto bancário?', '!pag'),
        (' assim que recebrem o dinheiro, eu terei acesso aos videos?', '!pag'),
        ('ja comprei  o boys academy mas o kong nao responde alguem me ajuda?', '!pag'),
        ('Ele vai mandar os vídeos no meu e-mail?', '!pag'),
        ('Ja efetuei a compra, o que faço agora?', '!pag'),
        ('quais os métodos de pagamento?', '!pag'),
        ('qual métodos pra adquirir uma das aulas', '!pag'),
        ('quais são os horarios?', '!pag'),
        ('horarios?', '!pag'),
        ('quando são os horarios?', '!pag'),
        ('que horas funciona o atendimento?', '!pag'),
        ('qual o horario do atendimento?', '!pag'),
        ('como eu pago o curso', '!pag'),
        ('qual é o horario de atendimento?', '!pag'),
        ('como posso fazer o pagamento', '!pag'),
        ('como posso efetuar o pagamento?', '!pag'),
        ("como posso fazer o pagamento?", '!pag'),
        ('como posso pagar?', '!pag'),
        ('pagar', '!pag'),
        ('posso pagar?', '!pag'),
        ('posso pagar', '!pag'),
        ('Boa tarda alguém pode me mandar o boleto por favor', '!pag'),
        ('pode me enviar o boleto?', '!pag'),
        ('Como faço pra pegar meu pacote que comprei no Boys Academy?', '!pag'),
        ('como faço pra pegar meu pacote que comprei?', '!pag'),
        ('como faço pra receber meu pacote?', '!pag'),
        ('Como faço pra pegar meu pacote que comprei no Boys Academy', '!pag'),


        # upgrades
        ('como funciona o upgrade de pacote?', '!upgrade'),
        ('como eu faço o upgrade de pacote?', '!upgrade'),
        ('com que eu falo para fazer upgrade de pacote?', '!upgrade'),
        ('onde eu acho os preços dos upgrades?', '!upgrade'),
        ('eu fiz a compra antes do pacote pro, com quem falo pra fazer o upgrade?', '!upgrade'),
        ('tenho o pacote prime, tem como fazer o upgrade dele?', '!upgrade'),
        ('upgrade de pacote', '!upgrade'),
        ('upgrade', '!upgrade'),
        ('como funciona o upgrade?', '!upgrade'),
        ('o que é o upgrade?', '!upgrade'),
        ('upgrade', '!upgrade'),
        ('oq é upgrade?', '!upgrade'),
        ('pode me explicar como funciona o upgrade?', '!upgrade'),
        ('me fala sobre os upgrades', '!upgrade'),
        ('qual é a do upgrade?', '!upgrade'),
        ('o upgrade funciona como?', '!upgrade'),
        ('com quem eu devo falar pra fazer o upgrade?', '!upgrade'),
        ('upgrade', '!upgrade'),
        ('upgrade?', '!upgrade'),
        ('como é o upgrade de pacote?', '!upgrade'),
        ('como faço pra da um up no meu pacote', '!upgrade'),
        ('up pacote', '!upgrade'),
        ('quais valores do upgrade', '!upgrade'),
        ('quais valroes dos upgrade', '!upgrade'),
        ('como é os upgrades?', '!upgrade'),
        ("Quais são os upgrades?", '!upgrade'),
        ('como são os upgrades?', '!upgrade'),
        ('Upgrades?', '!upgrade'),
        ('Gente eu tenho o pacote pro , eu quero o completo oq eu fasso?', '!upgrade'),
        ('Gente eu tenho o pacote prime , eu quero o pacote pro oq eu fasso?', '!upgrade'),
        ('tenho o pacote pro e quero fazer o upgrade, pode ma ajudar?', '!upgrade'),

        # plataforma
        ('Os pacotes tem alguma plataforma específica?', '!plat'),
        ('plataforma', '!plat'),
        ('qual a plataforma do curso?', '!plat'),
        ('posso ser do console pra ver as aulas?', '!plat'),
        ('posso ser do mobile pra ver as aulas?', '!plat'),
        ('existe uma plataforma especifica para o pacote?', '!plat'),
        ('qual a plataforma do curso?', '!plat'),
        ('qual a plataforma dos videos?', '!plat'),
        ('plataforma do curso?', '!plat'),
        ('plataforma das aulas', '!plat'),
        ('plataforma dos pacotes', '!plat'),
        ('muda algo ser do celular?', '!plat'),
        ('tem algum problema ser do console?', '!plat'),
        ('algum problema eu ser do ps4?', '!plat'),
        ('posso comprar sendo do celular?', '!plat'),
        ('Os pacotes tem alguma plataforma específica?', '!plat'),
        ('pacote para plataforma especifico', '!plat'),
        ('pacote para qualquer plataforma?', '!plat'),
        ('posso ser do pc  pra comprar as aulas?', '!plat'),
        ('me fale sobre as plataformas', '!plat'),
        ('como funciona as plataformas?', '!plat'),
        ('sou do pc, tem algum problema?', '!plat'),
        ('sou do mobile, tem algum problema?', '!plat'),
        ('sou do ps4 tem algum problema?', '!plat'),
        ('são aulas apenas para o pc?', '!plat'),
        ('se eu for do pc, posso comprar?', '!plat'),
        ('se eu for do ps4, posso comprar?', '!plat'),
        ('se eu for do xbox, posso comprar?', '!plat'),
        ('serve pra todas plataformas?', '!plat'),
        ('Vcs também ajudam a melhorar pessoas de Playstation 4?', '!plat'),
        ("Vcs também ajudam a melhorar pessoas de Xbox", "!plat"),
        ('posso comprar sendo do mobile?', '!plat'),
        ('as aulas sao para ps4?', '!plat'),
        ('as aulas sao para pc?', '!plat'),
        ('as aulas sao para xbox?', '!plat'),
        ('ps4', '!plat'),
        ('xbox', '!plat'),


        # site
        ('qual o site da boys academy?', '!site'),
        ('qual o site para comprar pacotes?', '!site'),
        ('site da academy', '!site'),
        ('site comprar pacote', '!site'),
        ('qual o site?', '!site'),
        ('qual o site?', '!site'),
        ('onde eu posso ver os pacotes?', '!site'),
        ('qual o site pra ver os cursos disponiveis?', '!site'),
        ('você pode me mandar o site?', '!site'),
        ('site', '!site'),
        ('qual o site onde mostra os pacotes?', '!site'),
        ('vocês tem um site?', '!site'),
        ('me manda o site da boys academy', '!site'),
        ('manda o site da boys academy ai', '!site'),
        ('qual o site?', '!site'),
        ('site', '!site'),
        ('site boys academy', '!site'),
        ('me envia o site ai', '!site'),
        ('qual o site?', '!site'),
        ('qual é o site da boys academy?', '!site'),
        ('qual o site?', '!site'),
        ("site", '!site'),
        ('qual o site?', '!site'),
        ('o site?', '!site'),
        ('me manda o site', '!site'),
        ('qual o site', '!site'),
        ('o site?', '!site'),
        ('site', '!site'),
        ('como acesso o site?', '!site'),
        ('como posso acessar o site?', '!site'),

        # pacote lendário
        ('quando o pacote lendário irá voltar?', '!lendario'),
        ('como é o pacote lendário?', '!lendario'),
        ('como faço pra ter aulas práticas?', '!lendario'),
        ('existe algum pacote com aulas com o professor?', '!lendario'),
        ('como faço aulas com o professor?', '!lendario'),
        ('como eu faço aulas práticas?', '!lendario'),
        ('existe algum pacote com aulas práticas?', '!lendario'),
        ('posso ter aula ingame com os boys?', '!lendario'),
        ('como faço aulas praticas com os boys?', '!lendario'),
        ('como eu posso ter aulas diretamente com algum boy? em jogo', '!lendario'),
        ('existe como ter aulas no jogo junto com algum professor?', '!lendario'),
        ('algum professor dá aula em jogo?', '!lendario'),
        ("algum professor dá aula prática?", '!lendario'),
        ('gostaria de ter aulas práticas com algum professor, teria como?', '!lendario'),
        ('como faço pra poder ter aulas com o professor no fortnite? em jogo', '!lendario'),
        ('o pacote lendário irá voltar em algum momento?', '!lendario'),
        ('Gostaria de saber qual pacote conseguirei jogar com um dos professores', '!lendario'),
        ('com o pacote pro eu consigo jogar com algum professor?', '!lendario'),
        ('com o pacote eu consigo jogar com o professor?', '!lendario'),
        ('quando volta o pacote lendário da boys academy?', '!lendario'),
        ('quando o lendario vai voltar?', '!lendario'),
        ('existe um pacote pra jogar com o professor?', '!lendario'),
        ('posso jogar com algum professor?', '!lendario'),
        ('posso jogar com os professores?', '!lendario'),
        ('posso jogar junto com o professor?', '!lendario'),
        ('como é o pacote lendario', '!lendario'),
        ('lendario', '!lendario'),
        ('pacote lendario', '!lendario'),
        ('como é pacote lendario?', '!lendario'),
        ('legendary pacote', '!lendario'),
        ('pacote legendary', '!lendario'),
        (' o pacote lendário ainda existe?', '!lendario'),
        ('Tenho direito a aulas com o professor in-game?', '!lendario'),
        ('POSSO JOGA COM O TONYBOY', '!lendario'),
        ('POSSO JOGAR COM O TONYBOY?', '!lendario'),
        ('POSSO JGOAR com o PULGABOY?', '!lendario'),
        ('posso jogar com o pulga?', '!lendario'),

        # o que tem nas aulas?
        ('o que tem nas aulas?', '!aulas'),
        ('o que é ensinado nos videos?', '!aulas'),
        ('o que é ensinado na boys academy?', '!aulas'),
        ('sobre o que as aulas falam?', '!aulas'),
        ('o que os boys ensinam?', '!aulas'),
        ('sobre o que são as aulas?', '!aulas'),
        ('o que é repassado nas aulas?', '!aulas'),
        ('quais os tópicos da aula?', '!aulas'),
        ('o que os boys passam nas aulas?', '!aulas'),
        ('quais os tópicos que as aulas abrangem?', '!aulas'),
        ('como funciona as aulas?', '!aulas'),
        ('como é as aulas?', '!aulas'),
        ('como é o ensimamento?', '!aulas'),
        ('ola mim querer saber como funcionar aulas bois academy', '!aulas'),
        ('ola, gostaria de saber como funciona as aulas', '!aulas'),
        ('Oi, gostaria de saber como funciona as aulas!', '!aulas'),
        ('como é as aulas?', '!aulas'),
        ('como funciona a aula?', '!aulas'),
        ('como funciona o pacote?', '!aulas'),
        ('o que tem nas aulinhas?', '!aulas'),
        ('pode me falar como funciona as aulas?', '!aulas'),
        ('como é as aulas??', '!aulas'),
        ('como funciona os videos?', '!aulas'),
        ('como são os videos?', '!aulas'),
        ('como é os videos?', '!aulas'),
        ('como são as aulas?', '!aulas'),
        ('como funciona os videos?', '!aulas'),
        ('como funciona as videos-aulas?', '!aulas'),
        ('como são os videos-aulas?', '!aulas'),
        ('o que são os videos?', '!aulas'),
        ('do que são os videos?', '!aulas'),
        ('do que são as video-aulas?', '!aulas'),
        ('qual o conteudo dos pacotes?', '!aulas'),
        ('conteudo aulas', '!aulas'),
        ('aulas conteudo', '!aulas'),
        ('qual o conteudo dos pacotes', '!aulas'),
        ('o que tem nos pacotes?', '!aulas'),

        # campeonatos
        ('como funciona os campeonatos?', '!camp'),
        ('quando irá ter campeonatos?', '!camp'),
        ('quando ocorre campeonatos?', '!camp'),
        ('como faz pra participar dos campeonatos?', '!camp'),
        ('como é os campeonatos da boys academy?', '!camp'),
        ('como faz pra participar dos camps da boys academy?', '!camp'),
        ('o que é os campeonatos?', '!camp'),
        ('Como que eu faço para ir para um campeonato?', '!camp'),
        ('Ata, então se eu adquirir um pacote, os campeonatos são de graça?', '!camp'),
        ('Oi, boa noite, eu queria saber por onde que voces anunciam os campeonatos e se tem que pagar para joga?','!camp'),
        ('Um Tempo atras, eu comprei o pacote prime da boys academy, mas pelo oque me lembro nao tinha os campeonatos, agora eu posso participar dos campeonatos?','!camp'),
        ('como é os camps?', '!camp'),
        ('quando ocorre os campeonatos?', '!camp'),
        ('campeonato', '!camp'),
        ('o que é o campeonato?', '!camp'),
        ('campeonato?', '!camp'),
        ('me fale sobre os campeonatos', '!camp'),
        ('como faço pra participar dos campeonatos?', '!camp'),
        ('quando que acontece os camps?', '!camp'),
        ('como eu participo dos camps?', '!camp'),
        ('como é o camp?', '!camp'),
        ('posso participar dos camps?', '!camp'),
        ('posso particiapr do camp?', '!camp'),
        ('ae irmãozão como funciona os campeonato?', '!camp'),
        ('qual a fita dos campeonatos?', '!camp'),
        ('qq são esses campeonatos?', '!camp'),
        ('me explica os campeonatos', '!camp'),
        ('campeonatos', '!camp'),
        ('como funciona o campeonato?', '!camp'),
        ('como é os campeonatows?', '!camp'),
        ('campeonato?', '!camp'),

        # o que é a boys academy?
        ('o que é?', '!academy'),
        ('o que é a boys academy?', '!academy'),
        ('o que é esse projeto?', '!academy'),
        ('o que é essa academy?', '!academy'),
        ('quero melhorar no jogo, a boys academy ajuda?', '!academy'),
        ('quero melhorar, a boys academy é ideal?', '!academy'),
        ('pra que serve a boys academy?', '!academy'),
        ('qual o objetivo da boys academy?', '!academy'),
        ('pra q é a boys academy?', '!academy'),
        ('oq é a boys academy?', '!academy'),
        ('quero melhorar no jogo, a boys academy é a ideal?', '!academy'),
        ('O que é  Boys-academy ?', '!academy'),
        ('me explique o que é a boys academy', '!academy'),
        ('que é boys-academy?', '!academy'),
        ('como que é a boys academy??', '!academy'),
        ('o que é a Academy?', '!academy'),
        ('como funciona a boys academy?', '!academy'),
        ('como é a boys academy?', '!academy'),
        ('o que é a boys academy??', '!academy'),
        ("oq é a boys academy?", '!academy'),
        ('qq é a academy?', '!academy'),
        ('oq é a boys academyy?', '!academy'),
        ('qual é a da boys academy?', '!academy'),
        ('o que é a academy?', '!academy'),
        ('como é a academy?', '!academy'),
        ('oq é a academy?', '!academy'),
        ('qual é a da academy?', '!academy'),
        ('Oi, o que é a academy?', '!academy'),
        ('Oque é a boysacademy', '!academy'),
        ('oque é a academia boys', '!academy'),
        ('Como funciona o curso?', '!academy'),
        ('como que é o curso?', '!academy'),
        ('como é esse curso aí?', '!academy'),
        ('Oque é a boysacademy msm', '!academy'),
        ('me fala sobre a boys academy', '!academy'),
        ('me fale sobre boys academy', '!academy'),
        ('me fale sobre academy', '!academy'),

        # help
        ('help-me', '!help'),
        ('me ajude', '!help'),
        ('você pode me ajudar', '!help'),
        ('quem te criou?', '!help'),
        ('você tem um erro, pra quem devo falar?', '!help'),
        ('ajuda', '!help'),
        ('me ajuda?', '!help'),
        ('como você responde pra mim?', '!help'),
        ('mim ajuda', '!help'),
        ('vc pd me ajudar?', '!help'),
        ('vc pode me responder uma pergunta?', '!help'),
        ('como vc pode me ajudar?', '!help'),
        ('me ajudaaa', '!help'),
        ('pode me ajudar', '!help'),
        ('mi ajuda', '!help'),
        ("como vc funciona?", '!help'),
        ('como você funciona?', '!help'),
        ('por favor, me ajude', '!help'),
        ('ajuda-me', '!help'),
        ('ajuda-me', '!help'),
        ("me ajuda?", '!help'),
        ('vc pode me ajudar?', '!help'),
        ('me ajude', '!help'),
        ('help', '!help'),
        ('me helpa', '!help'),
        ('helpa', '!help'),
        ('me help', '!help'),
        ('help?', '!help'),
        ('vc pode me help?', '!help'),
        ('can you help me?', '!help'),
        ('help-me', '!help'),
        ('help', '!help'),
        ("vc pode me ajudar?", '!help')

        ]

# palavras que o bot não entende
stopwords = ['quanto', 'quais', 'onde', 'que', 'oq', 'quero', 'posso', 'quando', 'qual', 'ola', 'oi', 'quem',
             'como', 'a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta',
             'esta',
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
    if client.user.mention in message.content and message.channel.id == 568870659757703200:
        mensagem = message.content[0:500]
        print('Mensagem do usuário:')
        print(mensagem)
        testestemming = []
        teste = mensagem
        stemmer = nltk.stem.RSLPStemmer()
        if message.content == client.user.mention:
            return await message.channel.send(
                f"{message.author.mention} Você precisa me perguntar algo né bobo, como você quer que eu adivinhe?")
        for (palavras) in teste.split():
            comstem = [p for p in palavras.split()]
            testestemming.append(str(stemmer.stem(comstem[0])))

        novo = extratorpalavras(testestemming)
        print('Resultado:')
        print(classificador.classify(novo))
        resul = classificador.classify(novo)
        print('Outros resultados:')

        distribuicao = classificador.prob_classify(novo)
        for classe in distribuicao.samples():
            print("%s: %f" % (classe, distribuicao.prob(classe)))
        # resultados
        if resul == "!pro":
            await message.channel.send(
                f"{message.author.mention} \nO pacote **PRO** custa **100** reais. É o pacote mais avançado que temos atualmente. Te ofereçe vídeo-aulas de todos os professores: **Tony, Pulga, Zotie e Barbosa.** São vídeo-aulas que são focadas no **CENÁRIO PROFISSIONAL** passando dicas e ideias sobre **SCRIMS** e outros fatores avançados. Você terá vários benefícios, dentre eles: Você ganha a tag  *PRO BØYS* que te dá acesso a salas da Staff da comunidade da THE BØYS *(somente BIG 2 pra baixo)*,  além também de ganhar a tag *SCHØØL BOYS* que te dá acesso a sala de voz *SCHØØL LOUNGE* e ao chat de texto *school-pvt* que é o chat privado para os alunos da Boys Academy. Você também poderá participar dos futuros campeonatos exclusivos para os alunos, eles serão informados com aviso prévio.\n\n**Link para compra:** https://www.boysacademy.com.br/loja/Pacote-Pro-p133683088")
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!limitado":
            await message.channel.send(
                f"{message.author.mention} \nO pacote **LIMITADO** custa **30** reais. É o pacote mais básico de todos, para iniciantes. Te ofereçe video-aulas de um professor de sua escolha, dentre os cinco: **Tony, Pulga, Barbosa e Zotie.** Você terá vários benefícios, dentre eles: Você ganha a tag *SCHOOL BOYS* que te dá acesso a sala de voz *SCHØØL LOUNGE* e ao chat de texto *school-pvt* que é o chat privado para os alunos da Boys Academy. Você também poderá participar dos futuros campeonatos exclusivos para os alunos, eles serão informados com aviso prévio.\n\n**Link para compra:** https://www.boysacademy.com.br/loja/Pacote-Limitado-p113604093")
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!prime":
            await message.channel.send(
                f"{message.author.mention} \nO pacote **PRIME** custa **70** reais. É um pacote mediano, porém com vários vídeos de diferentes professores. Te ofereçe video-aulas de todos os seguintes professores: **Tony, Pulga, Zotie e Barbosa.** Vídeo-aulas que são focadas em fatores de **Mira/Construção/Movimentação**. Você terá vários benefícios, dentre eles: Você ganha a tag *SCHOOL BOYS* que te dá acesso a sala de voz *SCHØØL LOUNGE* e ao chat de texto *school-pvt* que é o chat privado para os alunos da Boys Academy. Você também poderá participar dos futuros campeonatos exclusivos para os alunos, eles serão informados com aviso prévio.\n\n**Link para compra:** https://www.boysacademy.com.br/loja/Pacote-Prime-p113604094 ")
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!pacotes":
            await message.channel.send(
                f"{message.author.mention} \nAtualmente nós temos **quatro** pacotes disponíveis em nosso site!\nPacote **LIMITADO** (R$ 30,00)\nPacote **PRIME**(R$ 70,00)\nPacote **PRO** (R$ 100,00)\n**Combo Completo** (Pacote PRIME & Pacote PRO) (R$ 150,00)\n\nNo momento são **4** professores, são os seguintes: **Tony, Pulga, Zotie e Barbosa.**\n\n*Para saber mais sobre cada pacote, pergunte sobre ele, eu tentarei ao máximo lhe ajudar! Se quiser saber as diferenças, pergunte também sobre os pacotes, e tire suas conclusões, caso queira também saber sobre o que o pacote inclui, pergunte sobre um desses acima. Você também pode checar nosso site:\nhttps://www.boysacademy.com.br*")
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!pag":
            await message.channel.send(
                f'{message.author.mention} \n- Temos dois métodos de pagamento, **PayPal e Boleto**. Para comprar por boleto contate o Rewtor. Caso escolha o PayPal como forma de pagamento, efetue a compra pelo site!\n- Após a compra mande o comprovante de pagamento para o Discord: **<@553782641590009878>** dentro do horário de atendimento que é das **15:00 até às 20:00** de **Segunda a Sábado**.\n- Depois de ter enviado o comprovante você será auxiliado para receber seu produto. Todo o sistema será realizado através do GoogleDrive, então é necessário que você possua uma conta no mesmo.')
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!upgrade":
            await message.channel.send(
                f'{message.author.mention} \n*Os upgrades funcionam da seguinte forma:*\n**Pacote LIMITADO  ======> Pacote PRIME = R$ 40,00\nPacote PRIME ======> Pacote PRO = R$ 30,00** (Só poderá ser feito 1 mês após o aluno ter comprado o pacote PRIME).\n\nPara efetuar seu upgrade você deve enviar uma mensagem para o privado de um de nossos atendentes de acordo com a forma de pagamento que será usada por você.\n\n***Boleto Bancário: @rewtorboy\nPaypal: @kongboy***')
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!plat":
            await message.channel.send(
                f'{message.author.mention} \nO curso está disponível para **todas as plataformas**. Isso não interfere na aula, pois as dicas são gerais, mas há dicas que são especialmente para a plataforma do professor, porém a maior parte das dicas são gerais!')
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!site":
            await message.channel.send(f'{message.author.mention} \n**Site da BØYS ACADEMY**\nhttps://www.boysacademy.com.br')
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!lendario":
            await message.channel.send(
                f"{message.author.mention} \n**Não há mais aulas práticas (junto com o professor in'game)**. Isso por causa da superlotação desse pacote. Anteriormente tentamos, porém com a superlotação acabou não dando muito certo, e não há previsões para o pacote Lendário voltar!\n\n*Porém temos outros 3 pacotes, caso você  se interesse, me pergunte sobre eles :)*\n\n*Para quem comprou o pacote lendário quando existia, e não conseguiu ter todas as aulas, contate <@553782641590009878>*")
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!aulas":
            await message.channel.send(
                f'{message.author.mention} \nFaz essa mesma pergunta, só que informa qual pacote você quer saber sobre as aulas, aí eu posso te ajudar!')
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!camp":
            await message.channel.send(
                f'{message.author.mention} \n**Somente para o pessoal que é da SCHOOL BOYS!**\nOs campeonatos são realizados periodicamente, ocorrem sempre em uma temporada diferente, ou seja,  **1 campeonato por season do Fortnite**. Caso o campeonato seja em dupla, é realizado um sorteio para decidir as duplas, lembrando que não participa quem não tem algum pacote da **Boys Academy**. \n\n*Sempre quando houver algum campeonato, ele é avisado no chat privado dos alunos, também as recompensas da vitória do campeonato será falado com aviso prévio... então fique ligado!*')
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!academy":
            await message.channel.send(
                f'{message.author.mention} \nA **BØYS ACADEMY** é um projeto que visa a **melhoria do nivel de jogo** de todos os jogadores dentro da comunidade do Fortnite, onde as aulas são feitas por **jogadores profissionais** para você evoluir em pontos fundamentais e ter **sucesso no jogo.**')
            await message.add_reaction('<:correto:553691801366822915')
        elif resul == "!help":
            await message.channel.send(
                f'{message.author.mention} \nOi, sou um bot de **Inteligência Artificial**, provavelmente você pediu ajuda, e vou tentar te ajudar!\n\nBom, como sou um bot de IA, eu respondo as suas perguntas, mas somente em relação a **BØYS ACADEMY**, se a pergunta que você fizer eu souber responder, eu te ajudarei da forma correta! \n\nFui desenvolvido pelo **Daleboy** e pelo **Luse**, então se você ver algo errado em mim, procure por eles para poderem arrumar :)')
            await message.add_reaction('<:correto:553691801366822915')


client.run('MeuTokenSecreto.dll')
