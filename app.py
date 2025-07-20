import time
import os

# Tabela de valores simbólicos
scalarys = {
    "•x•": 1.0,
    "•∆•": 2.0,
    "•∆∆•": 4.0,
    "•O•": 3.0,
    "•OO•": 6.0,
    "∅": 0.0
}

# Converte valor numérico em símbolo Scalarys
def symbol_from_value(value):
    for k, v in scalarys.items():
        if abs(v - value) < 0.01:
            return k
    return f"[{value:.1f}]"

# Operações simbólicas
def calc_scalar(op, a, b):
    if op == '⊕':
        return a + b
    elif op == '⊖':
        return max(0, a - b)
    elif op == '⊗':
        return a * b
    elif op == '⊘':
        return a / b if b != 0 else 0
    else:
        return None

# Avalia expressão simbólica completa
def eval_expression(expr):
    parts = expr.split()
    if len(parts) < 3 or len(parts) % 2 == 0:
        return "Erro: expressão incompleta ou mal formatada."

    try:
        acc = scalarys.get(parts[0], 0)
        steps = f"{parts[0]}"

        for i in range(1, len(parts), 2):
            op = parts[i]
            b_symbol = parts[i + 1]
            b = scalarys.get(b_symbol, 0)
            acc = calc_scalar(op, acc, b)
            steps += f" {op} {b_symbol}"

        result_symbol = symbol_from_value(acc)
        return f"{steps} = {result_symbol} ({acc:.1f})"
    except Exception as e:
        return f"Erro: {e}"

# Loop com evolução dinâmica
def main_loop():
    print("📐 Interpretador Scalarys com Evolução Dinâmica")
    print("Digite uma expressão inicial. A cada loop, ela vai crescer:")
    print("Ex: •x• ⊗ •∆•")
    print("Digite 'sair' para encerrar.\n")

    expr = input("Expressão inicial: ").strip()
    if expr.lower() == "sair":
        print("Encerrado.")
        return

    base_expr = expr.strip()
    next_ops = ["⊗", "⊕", "⊘", "⊖"]  # pode variar entre tipos de operação
    next_syms = list(scalarys.keys())  # símbolos disponíveis

    index = 0
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            # Avalia e mostra o resultado atual
            result = eval_expression(expr)
            print("🧠 Expressão:", expr)
            print("→ Resultado:", result)

            # Avança a expressão: adiciona mais símbolos e operações
            next_op = next_ops[index % len(next_ops)]
            next_sym = next_syms[index % len(next_syms)]
            expr += f" {next_op} {next_sym}"

            index += 1
            time.sleep(1.5)  # intervalo de 1.5s por loop
    except KeyboardInterrupt:
        print("\n⏹ Loop interrompido pelo usuário.")

if __name__ == "__main__":
    main_loop()






