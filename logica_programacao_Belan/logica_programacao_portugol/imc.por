programa
{
	
	funcao inicio()
	{
		inteiro Quantidade_de_entrevistados = 0
	     real Media_de_Idade
		cadeia Nome
          cadeia Genero
          inteiro Idade, Anos, imc
		const inteiro Maior = 18
		real Peso
		real Altura
		
		

		faca
		 	{

		    
		    escreva ("Digite sua idade: ")
		leia(Idade)
		
		se (Idade >= Maior)
		   escreva ("Voce é maior de idade\n")
		senao
	{

		Anos = Maior - Idade
		escreva ("\nfaltam " ,Anos, " para atingir a maioridade \n")}
		
		

		 se (Idade <18)
		 
		  escreva("\nVoce nao esta habilitado a participar da entrevista\n")
			 
		} 	
		enquanto (Idade <18)
		
			escreva("Digite se nome: ")
		 	leia(Nome)
		 	limpa()
		 
		 
		 	escreva("Digite seu Genero: ")
		 	leia(Genero)
		 	limpa()

		 	escreva("Digite seu peso: ")
		 	leia(Peso)
		 	limpa()

		 	escreva("Digite sua altura: ")
		 	leia(Altura)
		 	limpa()

		 	imc = (Peso / (Altura*Altura))*10000
		 	escreva ("Seu IMC é: " , imc)
		 	se (imc < 18.5)

		 	{
		 	escreva ("\nSeu IMC esta abaixo do indicado")
		 	
		 	}
		 	senao se (imc> 24.9)
		 	
		 	{
		 	escreva ("\nSeu IMC esta acima do indicado")
		 	}

		 	senao
		 	{
		     escreva ("\nSeu IMC esta  no indicado")
		 	}

		 	//segunda fase apresentar quantidade de entrevistados



               enquanto (Quantidade_entrevistados != 0) = quantidade_entrevistados + 1 
		 	

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1276; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */