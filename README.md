# rabbitmq

./rabbitmq_server-3.7.10/sbin/rabbitmqctl add_user fefe fefe

./rabbitmq_server-3.7.10/sbin/rabbitmqctl list_users

./rabbitmq_server-3.7.10/sbin/rabbitmqctl add_vhost vh1

./rabbitmq_server-3.7.10/sbin/rabbitmqctl set_permissions -p vh1 fefe ".*" ".*" ".*"
