# Kafka Essentials

Criado pelo Linkedin em 2011, o [Apache Kafka](https://kafka.apache.org/) é uma plataforma de streaming distribuída mundialmente conhecida por sua performance e escalabilidade. Atualmente, tem sido utilizado por grandes empresas como *Netflix, Spotify, Uber e Twitter*.

A página oficial da plataforma descreve três recursos principais:

* Publique e assine fluxos de registros, semelhantes a uma fila de mensagens ou sistema de mensagens corporativo;
* Armazene fluxos de registros de maneira durável e tolerante a falhas;
* Processe fluxos de registros conforme eles ocorrem;

Resumidamente o Kafka te permite:

> Produzir mensagens, armazená-las e consumi-las conforme ocorrem.

## Como ele faz tudo isso?
Vamos definir brevemente alguns termos que são constantemente utilizados quando falamos de Kafka:

* Mensagem: dado ou informação que deseja ser trafegada.
* Tópico: é como categorizamos e salvamos as mensagens.
* Producer: é quem produz uma mensagem para o tópico.
* Consumer: é quem consome as mensagens produzidas para um tópico.
* Broker: é quem hospeda os tópicos e salva todas as mensagens.

![fluxo_kafka](https://miro.medium.com/max/1400/1*qYGIdHktRtQsaGwz11XSOA.png)

## Principais comandos


### Listar todos os tópicos do Kafka
```sh
kafka-topics.sh —-bootstrap-server localhost:9092 —-list
```

### Detalhes de um tópico
```sh
kafka-topics.sh --bootstrap-server localhost:9092 --topic <nome_topico> --describe
```

### Criar um novo tópico
```sh
kafka-topics.sh —-bootstrap-server localhost:9092 —-create —-topic <nome_topico>
```


### Mudar número de partições de um tópico existente
```sh
kafka-topics.sh --bootstrap-server localhost:9092 --alter --topic <nome_topico> --partitions 4
```


### Excluir um tópico
```sh
kafka-topics.sh —-bootstrap-server localhost:9092 —-delete —-topic <nome_topico>
```


### Produzir uma mensagem
```sh
kafka-console-producer.sh —-bootstrap-server localhost:9092 —-topic <nome_topico>
> { mensagem: “mensagem teste” }
```


### Consumir mensagens
```sh
kafka-console-consumer.sh —-bootstrap-server localhost:9092 —-topic <nome_topico> 
```


### Consumir mensagens dentro do grupo de consumo
```sh
kafka-console-consumer.sh —-bootstrap-server localhost:9092 —-topic <nome_topico> --group <nome_grupo>
```
