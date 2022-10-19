# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas - A maior nota - A menor nota - A média da turma - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(*valores, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param valores: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    alunos = dict()
    alunos['total'] = len(valores)
    alunos['maior'] = max(valores)
    alunos['menor'] = min(valores)
    alunos['média'] = sum(valores) / len(valores)
    if sit:
        if alunos['média'] >= 7:
            alunos['situação'] = 'BOA'
        elif alunos['média'] >= 5:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'RUIM'
    return alunos


# PP
resp = notas(9.5, 2.5, 9, 10, sit=True)
print(resp)
help(notas)
