from elasticsearch import Elasticsearch

client = Elasticsearch("http://localhost:9200/")

query = {"query": {"match": {"text": {"query": "fame"}}}}

query_results = client.search(index="fivecolumnspattern", body=query)
query_results = query_results["hits"]["hits"]

print(query_results)

# print(query_results[0]["_source"]["url"])
# print(query_results[0]["_source"]["timestamps"])
# print(query_results[0]["_source"]["text"])
# print(query_results[0]["_source"]["billionaire"])
# print(query_results[0]["_source"]["video_title"])
