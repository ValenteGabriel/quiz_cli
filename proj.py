import json  # importa o módulo json para ler e escrever dados no formato JSON
from pathlib import Path  # importa Path para trabalhar com caminhos de arquivos

QUESTIONS_FILE = Path("questions.json")  # define o arquivo onde as perguntas serão salvas/lidas

DEFAULT_QUESTIONS = [  # lista padrão de perguntas, usada caso o arquivo ainda não exista
    {  # primeira pergunta
        "question": "Qual estrutura armazena pares chave-valor em Python?",  # texto da pergunta
        "options": ["lista", "tupla", "dicionário", "set"],  # alternativas de resposta
        "answer": 3  # número da alternativa correta
    },
    {  # segunda pergunta
        "question": "Qual comando cria uma função?",  # texto da pergunta
        "options": ["func", "def", "function", "lambda def"],  # alternativas de resposta
        "answer": 2  # número da alternativa correta
    },
    {  # terceira pergunta
        "question": "Qual método adiciona item ao fim de uma lista?",  # texto da pergunta
        "options": ["append", "push", "insert_end", "add_last"],  # alternativas de resposta
        "answer": 1  # número da alternativa correta
    },
    {  # quarta pergunta
        "question": "Qual exceção aparece ao converter texto inválido para inteiro?",  # texto da pergunta
        "options": ["TypeError", "NameError", "ValueError", "IndexError"],  # alternativas
        "answer": 3  # número da alternativa correta
    }
]


def load_questions():  # define uma função para carregar as perguntas
    if not QUESTIONS_FILE.exists():  # verifica se o arquivo questions.json ainda não existe
        QUESTIONS_FILE.write_text(  # cria o arquivo e escreve as perguntas padrão nele
            json.dumps(DEFAULT_QUESTIONS, ensure_ascii=False, indent=2),  # converte a lista para JSON formatado
            encoding="utf-8"  # usa codificação UTF-8 para aceitar acentos
        )

    return json.loads(QUESTIONS_FILE.read_text(encoding="utf-8"))  # lê o arquivo e converte o JSON para lista Python


def ask(question, index, total):  # define uma função para fazer uma pergunta ao usuário
    print(f"\nPergunta {index}/{total}")  # mostra o número da pergunta atual
    print(question["question"])  # mostra o texto da pergunta

    for number, option in enumerate(question["options"], start=1):  # percorre as opções numerando a partir de 1
        print(f"{number}. {option}")  # mostra cada opção numerada

    while True:  # cria um loop até o usuário digitar uma resposta válida
        try:  # tenta executar o código que pode gerar erro
            choice = int(input("Resposta: "))  # lê a resposta e tenta converter para inteiro

            if 1 <= choice <= len(question["options"]):  # verifica se a opção está dentro do intervalo válido
                return choice == question["answer"]  # retorna True se acertou e False se errou

        except ValueError:  # captura erro caso o usuário digite algo que não seja número
            pass  # ignora o erro e continua o fluxo

        print("Digite uma opção válida.")  # avisa que a entrada foi inválida


def main():  # define a função principal do programa
    questions = load_questions()  # carrega as perguntas do arquivo JSON
    score = 0  # começa a pontuação em zero

    for index, question in enumerate(questions, start=1):  # percorre todas as perguntas numerando a partir de 1
        if ask(question, index, len(questions)):  # chama a pergunta e verifica se o usuário acertou
            print("Correto!")  # mostra mensagem de acerto
            score += 1  # soma 1 ponto

        else:  # executa caso a resposta esteja errada
            right = question["options"][question["answer"] - 1]  # pega o texto da alternativa correta
            print(f"Errado. Resposta: {right}")  # mostra a resposta correta

    percent = score / len(questions) * 100 if questions else 0  # calcula a porcentagem de acertos

    print(f"\nPontuação: {score}/{len(questions)} ({percent:.1f}%)")  # mostra a pontuação final


if __name__ == "__main__":  # verifica se o arquivo está sendo executado diretamente
    main()  # chama a função principal