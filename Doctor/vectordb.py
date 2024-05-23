from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct

client = QdrantClient(url="http://localhost:6333")

def create_collection(name,size):
    client.create_collection(
        collection_name=name,
        vectors_config=VectorParams(size=size, distance=Distance.DOT),
    )

def insert_update(img_path,img_embed,id,collection_name):
    operation_info = client.upsert(
        collection_name=collection_name,
        wait=True,
        points=[
            PointStruct(id=id, vector=img_embed, payload={"image_path": img_path}),
        ],
    )
    print(operation_info)

def search_image(img_embed,collection_name):
    search_result = client.search(
        collection_name=collection_name, query_vector=img_embed, limit=3
    )
    return search_result

def delete_collection(name):
    try:
        client.create_collection(
            collection_name=name,
        )
        return True
    except:
        return False
# print(client.search(collection_name="flowes", id=10, limit=3))