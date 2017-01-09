# ratchetcc/ratchet-cassandra
Docker image for Apache Cassandra (single node or cluster)

## Usage

To create the image `ratchetcc/ratchet-cassandra` execute the following command:

	docker build -t ratchetcc/ratchet-cassandra .	

## Run

	docker create --name cassandra --net=host \
		-p 7199:7199 -p 7000:7000 -p 7001:7001 -p 9160:9160 -p 9042:9042 \
		ratchet/ratchet-cassandra sh /opt/cassandra/run.sh

Run with local folders mounted

	docker create --name cassandra --net=host \
		-p 7199:7199 -p 7000:7000 -p 7001:7001 -p 9160:9160 -p 9042:9042 \
		-v /opt/conf/cassandra:/opt/cassandra/cassandra/conf -v /opt/data/volumes/cassandra:/opt/cassandra/data \
		ratchet/ratchet-cassandra sh /opt/cassandra/run.sh

## Configure Cassandra

Mount the configuration file (cassandra.yaml) to a local folder by adding e.g. 
`-v /opt/conf/cassandra:/opt/cassandra/cassandra/conf` and change the following parameters:

```yaml
listen_address: localhost
rpc_address: localhost
broadcast_rpc_address: localhost

seed_provider:
    - class_name: org.apache.cassandra.locator.SimpleSeedProvider
      parameters:
          - seeds: "seeders1,seeder2"
```

Reference https://docs.datastax.com/en/cassandra/2.1/cassandra/configuration/configTOC.html for further details.
