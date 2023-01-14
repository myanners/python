import tweepy as tw 

# Chaves de autenticação do Twitter
#API Key
consumer_key = ''
#API Key Secret
consumer_secret = ''
#Access Token
access_token = ''
#Access Token Secret
access_token_secret = ''
#Bearer Token
bearer_token = ''

# Criação do cliente Tweepy para abrir conexão com Twitter (instancia do metodo Client)
cliente = tw.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

#Define o termo e lingua falada do tweet
termo= 'BBB lang:pt'

#Define quantidade de 0 a 100 tweets a serem buscados
qtdadetweets = 100

#Define periodo de inicio e fim
start = '2023-01-13T21:00:01Z'
end = '2023-01-13T22:00:01Z'

#Procura Tweet no metodo Client.search_recent_tweets(query, *, end_time=None, expansions=None, max_results=None, media_fields=None, next_token=None, place_fields=None, poll_fields=None, since_id=None, sort_order=None, start_time=None, tweet_fields=None, until_id=None, user_fields=None, user_auth=False)
resposta = cliente.search_recent_tweets(query=termo, max_results=qtdadetweets, start_time=start, end_time=end)

#Printa todos os tweets
print(resposta.data)

#Guarda os dados em uma variavel
dados = resposta.data

#Printa Tweet id e text do primeiro tweet da lista
print(dados[0].id)
print(dados[0].text)

#Printa todos os tweets usando laço
for i in dados:
    print(i.id)
    print(i.text)

