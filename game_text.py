def valor():
	value = input("\tCAMINHO: #")
	return value

def opcao_desconhecida():
	print("\n\tOpção desconhecida. Irei repetir a última narrativa.\n")

def entrada():
	print("""\n\n
	### A CAVERNA ###
	by nikorasu42

	Você é um cavaleiro honrado que adentra uma caverna misteriosa!
	Munido de sua armadura brilhante, seu escudo enfeitado e sua espada afiada, você desce as escadas rumo ao desconhecido.
	Ao adentrar as profundezas da cripta, você encontra duas portas. Qual você escolhe?

	a) Porta Esquerda.
	b) Porta Direita.

	Escolha com cautela, nobre soldado!""")
	caminho = valor()

	if caminho == 'a':
		print("\n\tVocê escolheu entrar na porta esquerda. O seu destino está selado.\n")
		porta_esquerda()		

	elif caminho == 'b':
		print("\n\tVocê escolheu entrar na porta direita. O seu destino está selado.\n")
		porta_direita()

	else:
		opcao_desconhecida()
		entrada()
	

def porta_esquerda():
	print("""
	Você se depara com uma criatura horrenda e terrível.
	É como se os seus piores pesadelos e traumas tivessem se unido e se transformado nessa criatura bestial.
	Você enfrentará os seus medos, ou se renderá a suas fraquezas?

	a) Enfrentar a criatura, como um verdadeiro herói.
	b) Correr pela sua vida e perder toda a sua honra.

	Escolha com cautela, nobre soldado!""")
	monstro = valor()
	
	if monstro == 'a':
		ataca_monstro()

	elif monstro == 'b':
		foge_monstro()

	else:	
		opcao_desconhecida()
		porta_esquerda()

def porta_direita():
	print("""
	Dentro dessa sala há nada mais que um imenso abismo que o separa de uma outra entrada.
	Olhar para o abismo lhe faz recordar todas as suas mágoas pelos erros do passado, e você sente um forte ímpeto de saltar em direção a morte. Ao mesmo tempo, você sabe que também pode tentar chegar ao outro lado.

	a) Suicídio.
	b) Redenção.""")
	escolha = valor()

	if escolha == 'a':
		suicidio()

	elif escolha == 'b':
		redencao()		

	else:
		opcao_desconhecida()
		porta_direita()

def ataca_monstro():
	print("""
	Você agiu como um homem de verdade e resolveu enfrentar os seus monstros internos.
	Depois de uma batalha sangrenta e cansativa, você demonstra a sua superioridade degolando ferozmente a criatura com a sua espada!
	Cansado da batalha, você tem a opção de continuar explorando a caverna ou voltar para o seu vilarejo com a cabeça do monstro, mostrando para todas a sua coragem e sendo eternamente reconhecido.

	a) Continuar explorando.
	b) Voltar para o vilarejo.

	Escolha com cautela, nobre soldado!""")
	volta_continua = valor()

	if volta_continua == 'a':
		tesouro()			

	elif volta_continua == 'b':
		vilarejo()
	else:
		opcao_desconhecida()
		ataca_monstro()

def foge_monstro():
	print("""
	Você tenta fugir do monstro, porém ele é veloz e consegue lhe atacar pelas costas.
	Você é comido vivo, e torturado no inferno por ser um cavaleiro covarde que fugiu da batalha.""", end = ' ')
	endgame()	

def vilarejo():
	print("""
	Você volta para o vilarejo carregando a cabeça do monstro.
	Consegue entrar para a história daquela região, conquista fama e glória.
	Se casa com uma linda mulher e tem vários filhos.
	Você vive feliz para sempre.""", end = ' ')	
	endgame()

def tesouro():
	print("""
	Você descobre que o monstro guardava a entrada para um salão repleto de tesouros, jóias e relíquias. 		O seu futuro agora será de eterno luxo e riquezas inestimáveis. Será um nobre do mais alto escalão, amigo íntimo da nobreza.
	Terá várias amantes e propriedades. A vida dos sonhos agora é sua.""", end = ' ')
	endgame()

def suicidio():
	print("""
	Você pula o abismo em direção aos braços da morte. O eterno descanso lhe espera.
	Aqueles que você amava e foram perdidos lhe aguardam, nobre cavaleiro que cansou da guerra.""", end = ' ')
	endgame()	

def redencao():
	print("""
	Você decide que ainda não é hora de desistir, pois ainda há aqueles que precisam ser salvos.
	Talvez um outro dia, você pensa.

	Saindo pela próxima porta você encontra o mais belo dos jardins. Presenciar tão vasta beleza faz os seus olhos encherem de lágrimas. Recuperada as esperanças através da fé, você decide se reerguer e começar de novo, para consertar os erros do seu passado.""", end = ' ')
	endgame()

def endgame():
	print("Parabéns!")
	print("\n\n\tFim do jogo.\n")

entrada()
