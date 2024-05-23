from flask import Flask, request, jsonify
import graphene
from graphene import Mutation, String, Int, ObjectType, Schema
from itertools import combinations_with_replacement

app = Flask(__name__)


#Aqui, fiz nossa função para calcular combinações de pontuações
def calcular_combinacoes(score):
    pontos_possiveis = [3, 6, 7, 8]

    def combinacoes(possiveis, alvo):
        dp = [0] * (alvo + 1)
        dp[0] = 1
        for pontos in possiveis:
            for i in range(pontos, alvo + 1):
                dp[i] += dp[i - pontos]
        return dp[alvo]

    try:
        team1, team2 = map(int, score.split('x'))
    except ValueError:
        return 0

    return combinacoes(pontos_possiveis, team1) * combinacoes(pontos_possiveis, team2)


#Aqui está nossa Rota REST para realizar a verificação das combinações
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    score = data.get('score')
    if not score:
        return jsonify({"error": "Invalid input"}), 400

    combinacoes = calcular_combinacoes(score)
    return jsonify({"combinations": combinacoes})


#GraphQL Mutation
class Verify(Mutation):
    class Arguments:
        score = String(required=True)

    combinations = Int()

    def mutate(self, info, score):
        combinations = calcular_combinacoes(score)
        return Verify(combinations=combinations)


class Mutation(ObjectType):
    verify = Verify.Field()


schema = Schema(mutation=Mutation)


@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    result = schema.execute(
        data.get('query'),
        variables=data.get('variables')
    )
    return jsonify(result.data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
