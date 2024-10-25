import random

print("\n\n>>>>>>  PEDRA, PAPEL E TESOURA  <<<<<<")

print ("""
REGRAS:
    1. Pedra ganha de Tesoura (Pedra quebra Tesoura).
    2. Tesoura ganha de Papel (Tesoura corta Papel).
    3. Papel ganha de Pedra (Papel cobre Pedra).
""")

escolhas = ["Pedra", "Papel", "Tesoura"]


sair = 'q'
contador_usuario = 0
contador_maquina = 0    

vitoria_descricao = {("Pedra", "Tesoura"): "Pedra quebra Tesoura", ("Tesoura", "Papel"): "Tesoura corta Papel", ("Papel", "Pedra"): "Papel cobre Pedra"}

while True: 
    
    escolha_usuario = input("\n==> Sua vez (Digite 'q' para sair): ").title()
    
    if escolha_usuario == 'Q':
        print("|___Você saiu do jogo!___|")
        break
    
    if escolha_usuario not in escolhas:
        print ('\n!!! Apenas "Pedra", "Papel" ou "Tesoura" !!!\n')
        continue
    
    escolhas_sorteadas = random.choice(escolhas)
    print(f"\n=> Máquina escolheu: {escolhas_sorteadas}")

    if (escolha_usuario, escolhas_sorteadas) in vitoria_descricao:
        print(f"\n*** Você venceu! {vitoria_descricao[(escolha_usuario, escolhas_sorteadas)]} ***\n")
        contador_usuario += 1
    
    elif escolha_usuario == escolhas_sorteadas:
        print("\n@@@ Empate! @@@\n")
    
    else:
        print("### Você perdeu! ###")
        contador_maquina += 1        
        
    print(f"\n========== PLACAR ==========")
    print(f"-> Você: {contador_usuario} x Máquina: {contador_maquina}")
    print("============================\n")
    
          
    