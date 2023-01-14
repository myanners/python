import tweepy 

# Chaves de autenticação do Twitter
#API Key
twconsumer_key = ''
#API Key Secret
twconsumer_secret = ''
#Access Token
twaccess_token = ''
#Access Token Secret
twaccess_token_secret = ''
#Bearer Token
twbearer_token = ''

# Criação do cliente Tweepy
cliente = tweepy.Client(bearer_token=twbearer_token, consumer_key=twconsumer_key, consumer_secret=twconsumer_secret, access_token=twaccess_token, access_token_secret=twaccess_token_secret, wait_on_rate_limit=False)

# Define um termo a ser buscado
termo = "BBB lang:pt"

# Define quantidade de tweets de 10 a 100 da busca
qtdadetweets = 30

# Busca recente de tweets com a palavra "BBB" e imprime o texto de cada tweet
response = cliente.search_recent_tweets(query=termo, max_results=qtdadetweets, expansions='author_id')
for tweet in response.data:
    author_id = tweet['author_id']
    for user in response.includes['users']:
        if user['id'] == author_id:
            print(' ')
            print('====================================================')
            print(' ')
            print(user['username'])
            print('@........................@')
            print(tweet['text'])