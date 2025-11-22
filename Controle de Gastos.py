import os
from datetime import datetime

# Definição do nome do arquivo de banco de dados conforme planejado [cite: 7]
ARQUIVO_DADOS = "gastos.txt"

def limpar_tela():
    """Limpa a tela do terminal para melhor visualização."""
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_data_atual():
    """Retorna a data atual formatada."""
    return datetime.now().strftime("%d/%m/%Y")

def inicializar_arquivo():
    """Cria o arquivo gastos.txt se ele não existir[cite: 7]."""
    if not os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            pass

def salvar_transacao(tipo, valor, descricao):
    """
    Salva uma nova transação no arquivo gastos.txt.
    Formato: tipo|valor|descricao|data
    Atende ao requisito de gravação de dados[cite: 13, 14].
    """
    data = obter_data_atual()
    linha = f"{tipo}|{valor}|{descricao}|{data}\n"
    
    with open(ARQUIVO_DADOS, "a", encoding="utf-8") as f:
        f.write(linha)
    
    print(f"\n✅ {tipo} cadastrada com sucesso!")
    input("Pressione Enter para continuar...")

def ler_dados():
    """Lê e retorna todas as linhas do arquivo gastos.txt."""
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        return f.readlines()

def adicionar_receita():
    """Função para cadastrar entrada de dinheiro[cite: 29]."""
    limpar_tela()
    print("--- ADICIONAR RECEITA ---")
    try:
        valor = float(input("Digite o valor da receita: R$ "))
        descricao = input("Digite uma descrição (ex: Salário, Venda): ")
        salvar_transacao("Receita", valor, descricao)
    except ValueError:
        print("\n❌ Erro: Por favor, digite um valor numérico válido.")
        input("Pressione Enter para tentar novamente...")

def adicionar_despesa():
    """Função para cadastrar saída de dinheiro[cite: 30]."""
    limpar_tela()
    print("--- ADICIONAR DESPESA ---")
    try:
        valor = float(input("Digite o valor da despesa: R$ "))
        descricao = input("Digite uma descrição (ex: Aluguel, Mercado): ")
        salvar_transacao("Despesa", valor, descricao)
    except ValueError:
        print("\n❌ Erro: Por favor, digite um valor numérico válido.")
        input("Pressione Enter para tentar novamente...")

def listar_movimentacoes():
    """
    Lista todas as movimentações salvas e exibe formatado.
    Atende ao requisito de leitura e organização[cite: 15, 31].
    """
    limpar_tela()
    print("--- EXTRATO DE MOVIMENTAÇÕES ---")
    print(f"{'DATA':<12} | {'TIPO':<10} | {'VALOR (R$)':<12} | {'DESCRIÇÃO'}")
    print("-" * 60)
    
    transacoes = ler_dados()
    
    if not transacoes:
        print("Nenhuma movimentação registrada.")
    else:
        for linha in transacoes:
            partes = linha.strip().split('|')
            if len(partes) == 4:
                tipo, valor, descricao, data = partes
                print(f"{data:<12} | {tipo:<10} | {float(valor):<12.2f} | {descricao}")
    
    print("-" * 60)
    input("\nPressione Enter para voltar ao menu...")

def exibir_saldo():
    """Calcula e exibe o saldo total (Receitas - Despesas)[cite: 32]."""
    transacoes = ler_dados()
    total_receitas = 0.0
    total_despesas = 0.0
    
    for linha in transacoes:
        partes = linha.strip().split('|')
        if len(partes) == 4:
            tipo, valor, _, _ = partes
            if tipo == "Receita":
                total_receitas += float(valor)
            elif tipo == "Despesa":
                total_despesas += float(valor)
    
    saldo = total_receitas - total_despesas
    
    limpar_tela()
    print("--- SALDO ATUAL ---")
    print(f"Total de Receitas: R$ {total_receitas:.2f}")
    print(f"Total de Despesas: R$ {total_despesas:.2f}")
    print("-" * 30)
    print(f"SALDO FINAL:       R$ {saldo:.2f}")
    print("-" * 30)
    input("\nPressione Enter para voltar ao menu...")

def menu():
    """
    Menu principal com as opções definidas no planejamento.
    Interatividade via teclado[cite: 9, 10, 11].
    """
    inicializar_arquivo()
    while True:
        limpar_tela()
        print("=== CONTROLE DE GASTOS PESSOAIS ===")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Listar Movimentações")
        print("4. Exibir Saldo Total")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            adicionar_receita()
        elif opcao == '2':
            adicionar_despesa()
        elif opcao == '3':
            listar_movimentacoes()
        elif opcao == '4':
            exibir_saldo()
        elif opcao == '5':
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

# Execução do programa
if __name__ == "__main__":
    menu()