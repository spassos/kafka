# Kafka Essentials

![kafka_logo](https://kafka.apache.org/images/logo.png)

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


## Instalação do Kafka

### Linux

1 - Atualizar o SO:

```sh
sudo apt update
```

2 - Instalar o JDK 8:

```sh
sudo apt install openjdk-8-jdk
```

3 - Verificar se a instalação ocorreu com sucesso:

```sh
java -version
```

4 - Baixar os binários do Kafka, neste [link](https://kafka.apache.org/downloads).

5 - Descompactar os binários:

```sh
tar -xvf kafka_2.12-2.5.0.tgz
```

6 - Renomear e mover a pasta para o caminho `~`

```sh
mv kafka_2.12-2.5.0 kafka
mv kafka/ ~
```

7 - Editar o arquivo `.bashrc` para reconhecer os comandos utilizados no Kafka como por exemplo o `kafka-topics.sh`

```sh
gedit .bashrc
```

Incluir no final do arquivo `.bashrc`
```sh
export PATH=/home/seu_nome_usuario/kafka/bin:$PATH
```

8 - Acessar o diretório do kafka e incluir as pastas `data/kafka` e `data/zookeeper`. São nesses diretórios que o Apache Kafka armaneza os dados dos tópicos e logs. 

```sh
cd kafka/
mkdir data
cd data
mkdir kafka
mkdir zookeeper
```

9 - Editar o arquivo `zookeeper.properties` e alterar o parâmetro dataDir para `/home/seu_usuario/kafka/data/zookeeper` e salvar as alteração:

```sh
cd kafka/config
gedit zookeeper.properties
```

10 - Editar o arquivo `server.properties`e alterar o parâmetro log.dirs para `/home/seu_usuario/kafka/data/kafka` e salvar as alterações

```sh
cd kafka/config
gedit server.properties
```

11 - Subir os serviços Zookeeper e Kafka:

```sh
zookeeper-server-start.sh /home/seu_usuario/kafka/confi/zookeeper.properties

kafka-server-start.sh /home/seu_usuario/kafka/confi/server.properties
```
### Docker

Acessar o diretório com o arquivo `docker-compose.yml` e executar o comanado abaixo:

```sh
docker-compose up -d
```

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