Brief documentation on the endpoints of your API
## **API documentation**
check the docs.md file
## request flow :
api->database server->databases->db_name->schemas->schema_name->public->tables->table_name->columns 

## **High-level answers to the following questions**:
1- How would you implement authentication? 
> Authentication can be handled by many ways. 
a- using custom basic authentication (username, password)
b- using 3rd party oauth2.0 authentication service such as Facebook, Google ...
c- if we are using kubernetes, we can abstract that using either istio and/or an api gateway with a 3rd party identity provider such as google, facebook .. istio/api gw will return a jwt token to the app (after they validate it)


2- If you had to scale this system up to serve 1000s of requests per hour, how would you do it?
> if the system is scaling to 1000s of req/s, one way we can scale it out is to deploy each API endpoint separately, and each microservice is deployed in a docker container. we can then deploy it to k8s, or any other container orchestration platform. Then we need to to make the app auto-scale (in k8s this is called horizental pod autoscaler).



3- If you had to be able to support Databases with 10,000 tables, how would your design change? What if you had to support databases with a million columns across 100,000 tables?
> the design of such a system requires distributing the databases across multiple database servers instead of only one. This also means that we need another database (preferably a NOSQL DB like AMAZON DynamoDB) to store the data (database name, database server host).
> Howerver, if the database needs to have a millions of columns and 100k tables, it is better to choose a columnar databases such as cassanda, HBase, clickhouse (clickhouse is a columnar sql based database).


## How to run
1- build the docker images:
```
docker-dompose build
```

2- run:
```
docker-dompose up
```
3- access the web UI of FastAPI; `<YOUR_PRIVATE_IP_ADDRESS>:8000/docs`

video: https://www.loom.com/share/c86e256861c946d3a7a577cb3935cd93