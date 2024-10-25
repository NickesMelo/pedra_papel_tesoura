
# Pedra, Papel e Tesoura

Um simples jogo de "Pedra, Papel e Tesoura" desenvolvido em Python, onde o jogador compete contra a máquina, que escolhe suas jogadas de forma aleatória.

## 📜 Regras do Jogo
1. **Pedra ganha de Tesoura** - Pedra quebra Tesoura.
2. **Tesoura ganha de Papel** - Tesoura corta Papel.
3. **Papel ganha de Pedra** - Papel cobre Pedra.

O jogador e a máquina fazem suas escolhas, e o jogo informa o vencedor, além de manter um placar atualizado.

## 📂 Estrutura do Projeto
- **Jogo:** Arquivo principal onde o jogo é executado.
- **Contador de placar:** Conta as vitórias do jogador e da máquina.
- **Dicionário de vitória:** Define as combinações vencedoras e exibe uma explicação para cada vitória.

## 🚀 Como Jogar
1. Clone o repositório:
   ```bash
   git clone https://github.com/NickesMelo/pedra_papel_tesoura
   ```
2. Navegue até a pasta do projeto:
   ```bash
   cd seu_repositorio
   ```
3. Execute o jogo:
   ```bash
   python app.py
   ```
4. Durante o jogo, digite sua jogada (**Pedra**, **Papel** ou **Tesoura**). Para sair, digite **q**.

## 📊 Exemplo de Saída
```plaintext
>>>>>> PEDRA, PAPEL E TESOURA <<<<<<

REGRAS:
    1. Pedra ganha de Tesoura (Pedra quebra Tesoura).
    2. Tesoura ganha de Papel (Tesoura corta Papel).
    3. Papel ganha de Pedra (Papel cobre Pedra).

==> Sua vez (Digite 'q' para sair): Pedra
=> Máquina escolheu: Tesoura

*** Você venceu! Pedra quebra Tesoura ***

========== PLACAR ==========
-> Você: 1 x Máquina: 0
============================
```

## 🛠️ Tecnologias Utilizadas
- Python 3

## 💡 Melhorias Futuras
- Adicionar um sistema de pontuação mais avançado.
- Implementar uma interface gráfica para facilitar a jogabilidade.

---

Divirta-se jogando e desafiando a máquina! 😄
