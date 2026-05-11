import json
from pathlib import Path

QUESTIONS_FILE = Path("questions.json")
DEFAULT_QUESTIONS = [
    {"question": "Qual estrutura armazena pares chave-valor em Python?", "options": ["lista", "tupla", "dicionário", "set"], "answer": 3},
    {"question": "Qual comando cria uma função?", "options": ["func", "def", "function", "lambda def"], "answer": 2},
    {"question": "Qual método adiciona item ao fim de uma lista?", "options": ["append", "push", "insert_end", "add_last"], "answer": 1},
    {"question": "Qual exceção aparece ao converter texto inválido para inteiro?", "options": ["TypeError", "NameError", "ValueError", "IndexError"], "answer": 3}
]


def load_questions():
    if not QUESTIONS_FILE.exists():
        QUESTIONS_FILE.write_text(json.dumps(DEFAULT_QUESTIONS, ensure_ascii=False, indent=2), encoding="utf-8")
    return json.loads(QUESTIONS_FILE.read_text(encoding="utf-8"))


def ask(question, index, total):
    print(f"\nPergunta {index}/{total}")
    print(question["question"])
    for number, option in enumerate(question["options"], start=1):
        print(f"{number}. {option}")
    while True:
        try:
            choice = int(input("Resposta: "))
            if 1 <= choice <= len(question["options"]):
                return choice == question["answer"]
        except ValueError:
            pass
        print("Digite uma opção válida.")


def main():
    questions = load_questions()
    score = 0
    for index, question in enumerate(questions, start=1):
        if ask(question, index, len(questions)):
            print("Correto!")
            score += 1
        else:
            right = question["options"][question["answer"] - 1]
            print(f"Errado. Resposta: {right}")
    percent = score / len(questions) * 100 if questions else 0
    print(f"\nPontuação: {score}/{len(questions)} ({percent:.1f}%)")


if __name__ == "__main__":
    main()
