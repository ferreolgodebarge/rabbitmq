import pika


# configure connection parameters
host = 'localhost'
port = 5672
vhost = 'vh1'
credentials = pika.PlainCredentials('fefe', 'fefe')
parameters = pika.ConnectionParameters(host, port, vhost, credentials)

# Create a connection object
connection = pika.BlockingConnection(parameters)

# Create a channel
channel = connection.channel()

# Connect to the queue or create it if not exists
channel.queue_declare(queue='queue1')

# Create an exchange
channel.exchange_declare(exchange='ex1')

# publish a message
channel.basic_publish(exchange='ex1',
                      routing_key='queue1',
                      body='Hello World! this is my first message !')

print(" [x] Sent 'message'")

connection.close()
