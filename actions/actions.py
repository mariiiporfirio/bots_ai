# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# # Dicionário de livros com ISBNs corretos
# LIVROS_POR_ISBN = {
#     "9786555352256": {
#         "titulo": "A Empregada",
#         "autor": "Freida McFadden",
#         "ano": 2020,
#         "descricao": "Millie aceita um emprego como empregada doméstica numa casa de luxo e descobre segredos obscuros da família."
#     },
#     "9786555842073": {
#         "titulo": "Tudo é Rio",
#         "autor": "Carla Madeira",
#         "ano": 2019,
#         "descricao": "Romance sobre um triângulo amoroso marcado por tragédias e ciúmes em uma pequena cidade."
#     },
#     "9786555602883": {
#         "titulo": "A Biblioteca da Meia‑Noite",
#         "autor": "Matt Haig",
#         "ano": 2020,
#         "descricao": "Nora encontra uma biblioteca mágica entre a vida e a morte onde revisita todas as vidas que poderia ter vivido."
#     },
#     "9788580419479": {
#         "titulo": "A Paciente Silenciosa",
#         "autor": "Alex Michaelides",
#         "ano": 2019,
#         "descricao": "Alicia Berenson mata o marido e passa a viver em silêncio absoluto; um psicoterapeuta tenta descobrir a verdade."
#     },
#     "9788501077230": {
#         "titulo": "Jantar Secreto",
#         "autor": "Raphael Montes",
#         "ano": 2012,
#         "descricao": "Quatro amigos em Copacabana organizam jantares clandestinos com pratos polêmicos e ingredientes chocantes."
#     },
#     "9788535925188": {
#         "titulo": "Cabeça de Santo",
#         "autor": "Socorro Acioli",
#         "ano": 2013,
#         "descricao": "Samuel vive dentro da cabeça de uma estátua de santo, ouve orações e mergulha numa jornada de mistério e religiosidade."
#     },
#     "9788501115024": {
#         "titulo": "O Homem de Giz",
#         "autor": "C. J. Tudor",
#         "ano": 2019,
#         "descricao": "Um grupo de amigos se comunica por desenhos de giz até que encontram um corpo desmembrado. O mistério ressurge anos depois."
#     },
#     "9788535929636": {
#         "titulo": "O Conto da Aia",
#         "autor": "Margaret Atwood",
#         "ano": 1985,
#         "descricao": "Em Gilead, as mulheres férteis são forçadas a gerar filhos para os líderes do regime totalitário. Uma distopia feminista."
#     },
#     "9788555340736": {
#         "titulo": "O Peso do Pássaro Morto",
#         "autor": "Aline Bei",
#         "ano": 2020,
#         "descricao": "A vida de uma mulher dos 8 aos 52 anos, marcada por perdas e dores cotidianas; prosa poética sobre amadurecimento e luto."
#     },
#     "9786555656671": {
#         "titulo": "Todas as Cores da Escuridão",
#         "autor": "Chris Whitaker",
#         "ano": 2022,
#         "descricao": "Em Monta Clare, nos anos 1970, meninas começam a desaparecer. Patch arrisca tudo para resgatar uma criança, desencadeando mistério."
#     }
# }

# class ActionBuscarPorISBN(Action):
#     def name(self) -> Text:
#         return "action_buscar_por_isbn"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         isbn = tracker.get_slot("ISBN")

#         if not isbn:
#             dispatcher.utter_message(text="Desculpe, não consegui identificar o ISBN. Pode repetir?")
#             return []

#         livro = LIVROS_POR_ISBN.get(isbn)

#         if livro:
#             resposta = (
#                 f"📚 *Livro Encontrado:*\n"
#                 f"**Título:** {livro['titulo']}\n"
#                 f"**Autor:** {livro['autor']}\n"
#                 f"**Ano:** {livro['ano']}\n"
#                 f"**Descrição:** {livro['descricao']}"
#             )
#         else:
#             resposta = "Desculpe, não encontrei nenhum livro com esse ISBN."

#         dispatcher.utter_message(text=resposta)
#         return []
