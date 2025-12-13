import discord, httpx
TOKEN = "MTM4NDg3NzE4NDQxNzUzMzk3Mg.GutZ2S.ldMaTNByXSaEJ8wTrNS2_oDWBERWLjs9OfZu-k"
RASA = "http://localhost:5005/webhooks/rest/webhook"
intencao = discord.Intents.default()
intencao.messages = True
cliente = discord.Client(intents=intencao)
@cliente.event
async def on_ready():
    print(f"Conectado como {cliente.user}")
async def enviar_mensagem(mensagem):
    async with httpx.AsyncClient() as client:
        resposta = await client.post(RASA, json={"sender": "user", "message": mensagem},
                                     timeout=60.0)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return f"Erro ao enviar mensagem: {resposta.status_code}"
@cliente.event
async def on_message(mensagem):
    if mensagem.author.bot:
        return
    resposta = mensagem.content
    respostaDoRobo = await enviar_mensagem(resposta)
    if isinstance(respostaDoRobo, list):
        for rsp in respostaDoRobo:
            if "text" in rsp:
                await mensagem.channel.send(rsp["text"])
    else:
        await mensagem.channel.send(respostaDoRobo)
cliente.run(TOKEN)