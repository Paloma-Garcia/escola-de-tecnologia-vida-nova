programa
{
	funcao inicio()
	{
		inteiro Candidato_A = 0, Candidato_B = 0, voto = 0 
		
		inteiro brancos = 0, nulos = 0, total_votos = 0
		
		real PorcentagemCandidatoA, PorcentagemCandidatoB 
		
		real PorcentagemBrancos, PorcentagemNulos 
		
		inteiro total_de_votos
		
		faca
		{
			limpa()
			escreva("\nEscolha seu candidato ou tecle zero para encerrar\n\n") 
			
			escreva("  1 -> Candidato A\n")
			escreva("  2 -> Candidato B\n")
			escreva("  3 -> Branco\n")
			escreva("  0 -> Para Encerrar a votção\n")
			
			escreva("\nQualquer numero diferente de 0, 1, 2 e 3 anulara o seu voto\n")
			escreva("Digite seu voto: ")
			
		    leia(voto)
		    limpa()

		escolha (voto)
			{
				caso 0: // case para caso 0
				    escreva ("Votação encerrada!\n") 
				    total_de_votos = (Candidato_A + Candidato_B + brancos + nulos)
				    PorcentagemCandidatoA = (100 * Candidato_A) / total_de_votos
				    PorcentagemCandidatoB = (100 * Candidato_B) / total_de_votos
				    PorcentagemBrancos = (100 * brancos) / total_de_votos
				    PorcentagemNulos = (100 * nulos) / total_de_votos
				    escreva("\nPorcentagem CandidatoA: ", PorcentagemCandidatoA, "%")
				    escreva("\nPorcentagem CandidatoB: ", PorcentagemCandidatoB, "%") 
				    escreva("\nPorcentagem brancos: ", PorcentagemBrancos, "%")
				    escreva("\nPorcentagem nulos: ", PorcentagemNulos, "%")
				    escreva("\nTotal de Votos: ",total_de_votos)
				    se (Candidato_A > Candidato_B)
				    escreva("\nCandidatoA ganhou a eleicao") 
				    se (Candidato_B > Candidato_A)
				    escreva("\nCandidatoB ganhou a eleicao")
				    se (Candidato_A == Candidato_B)
				    escreva("\n Ninguem ganhou")
				pare
				
				
				caso 1: 
			 		Candidato_A = Candidato_A + 1 
			 	pare
			 	
			 	caso 2: 
			 		Candidato_B = Candidato_B + 1  
			 	pare
			 	
			 	caso 3: 
			 		brancos = brancos + 1 
			 	pare
			 	
			 	caso contrario:
			 		nulos = nulos + 1 
			}			 
		}
		enquanto(voto != 0) 
		
		
	}
}



/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1983; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */