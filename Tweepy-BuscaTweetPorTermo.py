import tweepy 

# Chaves de autenticação do Twitter
twconsumer_key = ''
twconsumer_secret = ''
twaccess_token = ''
twaccess_token_secret = ''
twbearer_token = ''

# Criação do cliente Tweepy
cliente = tweepy.Client(bearer_token=twbearer_token, consumer_key=twconsumer_key, consumer_secret=twconsumer_secret, access_token=twaccess_token, access_token_secret=twaccess_token_secret, wait_on_rate_limit=False)

# Define um termo a ser buscado
termo = "BBB"

# Define quantidade de tweets de 10 a 100 da busca
qtdadetweets = 30

# Busca recente de tweets com a palavra "BBB" e imprime o texto de cada tweet
for tweet in cliente.search_recent_tweets(query=termo, max_results=qtdadetweets).data:
    print(tweet['text'])