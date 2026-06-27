
## Repositório para prática de Python

Este repositório foi criado com o intuito de armezenar projetos de treino que irei desenvolver nos próximos dias.

- Os desafios foram montados através da IA, devendo a mesma ser usada somente para as correções do código.
- Meta: Fazer os registros descritivos dos desafios concluídos e dos aprendizados

<details>
      <summary> <span style="font-size: 25px;"> <strong> 🔥Desafios Propostos </strong> </span> </summary>

  - <strong> Desafio 1 — Adivinhe o Número </strong>

      - Dificuldade: ⭐☆☆☆☆
      
      - Objetivo
      
      - O computador escolhe um número aleatório entre 1 e 100.
      
      - O jogador deve tentar adivinhar.
      
      - Após cada tentativa, informe:
      
      - "Muito alto"
      - "Muito baixo"
      - "Parabéns, você acertou!"
      
      No final mostre:
      - quantidade de tentativas
      - número sorteado
    
    - Desafio extra
      - Escolha um nível de dificuldade:
      
            - Fácil → infinitas tentativas
            - Médio → 10 tentativas
            - Difícil → 5 tentativas
      
   - <strong>Desafio 2 — Caixa Eletrônico</strong>

      - Dificuldade: ⭐⭐☆☆☆

      - Crie um pequeno sistema de caixa eletrônico.

            Menu:
            
            1 - Ver saldo
            2 - Depositar
            3 - Sacar
            4 - Extrato
            5 - Sair

      - Regras:
        - saldo começa em R$1000
        - não permitir saque maior que o saldo
        - guardar todas as operações em uma lista
        - mostrar o extrato no final
      - Extra
        - Impedir depósitos negativos.
        
   - <strong>Desafio 3 — Sistema de Biblioteca</strong>

     - Dificuldade: ⭐⭐⭐☆☆

     - Crie um programa onde o usuário pode:

          1 - Cadastrar livro
          2 - Listar livros
          3 - Procurar livro
          4 - Remover livro
          5 - Sair

     - Os livros podem ser armazenados em uma lista.

     - Exemplo:

          Python
          Clean Code
          1984
          Dom Casmurro
     - Extra
      
          Não permitir cadastrar dois livros iguais.

   - <strong>Desafio 4 — Jogo de Batalha</strong>

     - Dificuldade: ⭐⭐⭐⭐☆

     - Imagine um personagem.

            Ele possui:
            Vida: 100
            Ataque: 15
            Defesa: 8
          
     - O inimigo também.
     - Cada turno:

            jogador ataca
            inimigo ataca

     - O dano pode variar um pouco usando random.

     - O jogo termina quando alguém morrer.

     - Extra

            Criar três inimigos diferentes.

  - 🔥 Desafio 5 — Mercado Inteligente

     - Dificuldade: ⭐⭐⭐⭐⭐

     - Faça um sistema de mercado.

     - Menu:
          
            Cadastrar produto
            Comprar produto
            Listar estoque
            Alterar preço
            Remover produto
            Fechar caixa
            Sair

     - Cada produto possui:

            nome
            preço
            quantidade

     - Quando o cliente compra:

            reduz estoque
            calcula valor da compra

     - Ao fechar o caixa mostrar:

            faturamento
            produto mais vendido
            produto sem estoque
            quantidade restante de cada produto
     - Extra

          Permitir salvar tudo em um arquivo texto ou JSON
</details>

<details>
<summary> <span style="font-size:25px;"> <strong> Desafio Final: 📦 Mini WMS (Sistema de Gerenciamento de Estoque) </strong> </span> </summary>

- Desenvolva um sistema em Python para controlar um pequeno estoque.

  - Funcionalidades:

        cadastrar produtos
        registrar entradas
        registrar saídas
        pesquisar por nome
        alertar produtos com estoque baixo
        gerar um relatório final

  - No começo, faça tudo pelo terminal. Depois, você poderá evoluir para:

        interface gráfica com Flet;
        banco de dados SQLite;
        exportação para Excel;
        dashboard com gráficos.
</details>
 
## Diário de Programação
- Está seção funcionara como um relatório descrevendo os passos das coisas que foram feitas no dia 
<details>
<summary> <strong> 27/06/2026 </strong></summary>

- 1° dia praticando

  - Primeiro desafio foi concluído com sucesso. Ainda há espaços para melhorias, mas consegui programar sozinho e resolver os problemas com auxilio mínimo da IA
      
  - O desafio de hoje consistiu em fazer um programa onde a máquina determina um valor aleatório entre 1 e 100 e o usuário deve advinhar qual foi o valor escolhido. 
  
  - Ao momento que o usuário envia seu palpite o programa lê o valor e SE for igual ao sorteado imprime-se "Parabéns, você acertou.

  - Se não, caso o valor seja abaixo do escolhido, imprime-se "Muito baixo"

  - Se não, caso o valor seja maior do que o escolhido, imprime-se "Muito alto"

  - Foram definidos níveis de dificuldade, sendo eles: Fácil, Médio e Difícil.

            Fácil = Tentativas Ilimitadas
            Médio = 10 tentativas
            Difícil = 5 tentativas

  - Esta programa permitiu que eu pratique minha esrtura de código e a fixação de conceitos como: if/else, while e funções. 

</details>