from kafka import KafkaConsumer
from kafka import TopicPartition
from json import loads
from kafka import KafkaProducer
# 87.98.133.57:65196
# 10.10.10.5:9094
def test(server,topic):
    # TOPIC = "alert"
    consumer = KafkaConsumer(
        bootstrap_servers=[server],
        auto_offset_reset='latest',
        consumer_timeout_ms=1000,
        group_id="group1",
        enable_auto_commit=False,
        auto_commit_interval_ms=1000,
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
    topic_partition = TopicPartition(topic, 0)
    assigned_topic = [topic_partition]
    consumer.assign(assigned_topic)
    # consumer.seek_to_end(topic_partition)
    consumer.seek_to_beginning(topic_partition)
    what=[]
    for message in consumer:
        print(message.value)
        # print("%s key=%s value=%s" % (message.topic, message.key, message.value))
        what.append(message.value)
    return what
    # consumer.commit()
# w=test()

# for n in range(len(w)):
#     print(w[n]['Driver Behavior'])
