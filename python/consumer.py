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
#channel.queue_declare(queue='queue1')

# Get an exchange
channel.queue_bind(exchange='ex1',
                   queue='queue1')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue='queue1',
                      no_ack=True)

channel.start_consuming()
