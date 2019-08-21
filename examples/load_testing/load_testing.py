# Tested on python3.6

import sys
import multiprocessing as mp
import grpc
import time
import base64

# network_analytics_node_importance
from service_spec_node_importance import network_analytics_node_importance_pb2
from service_spec_node_importance import network_analytics_node_importance_pb2_grpc
# network_analytics_node_importance

# named_entity_disambiguation
sys.path.append('named_entity_disambiguation')
import NamedEntityDisambiguation_pb2
import NamedEntityDisambiguation_pb2_grpc
# named_entity_disambiguation

# topic_analysis
sys.path.append('topic_analysis')
from topic_analysis import topic_analysis_pb2
from topic_analysis import topic_analysis_pb2_grpc
# topic_analysis

# emotion_recognition
sys.path.append('emotion_recognition')
from emotion_recognition import EmotionService_pb2
from emotion_recognition import EmotionService_pb2_grpc
# emotion_recognition


def multi_pro_sample():

    output = mp.Queue()

    processes = [mp.Process(target=f, args=[output]) for x in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [output.get() for p in processes]

    print(results)

def f(output):
    print(3)
    output.put(4)


def multi_pro(service_name,num_requests):

    output = mp.Queue()

    processes = None

    if service_name == 'find_central_nodes':
        processes = [mp.Process(target=find_central_nodes, args=[output]) for x in range(num_requests)]
    if service_name == 'named_entity_disambiguation':
        processes = [mp.Process(target=named_entity_disambiguation, args=[output]) for x in range(num_requests)]
    if service_name == 'topic_analysis':
        processes = [mp.Process(target=topic_analysis, args=[output,x]) for x in range(num_requests)]
    if service_name == 'emotion_recognition':
        processes = [mp.Process(target=emotion_recognition, args=[output]) for x in range(num_requests)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [output.get() for p in processes]

    if service_name == 'topic_analysis':
        process_topic_anal_output(results)

    print(results)
    summed = sum([t[0] for t in results])
    print(summed , '/' , len(results))


def process_topic_anal_output(results):
    print('Processing results for topic analysis')
    for r in results:
        print(r[0])

def find_central_nodes(output):


    try:
        # channel = grpc.insecure_channel('tz-services-1.snet.sh:2234')
        channel = grpc.insecure_channel('localhost:5001')
        stub = network_analytics_node_importance_pb2_grpc.NetworkAnalyticsNodeImportanceStub(channel)

        graph = {
            "nodes": ['1', '2', '3', '4', '5', '6', '7', '8'],
            "edges": [['1', '2'], ['1', '4'], ['2', '3'], ['2', '5'], ['3', '4'], ['3', '6'], ['2', '7'], ['3', '8']],
            "weights": [3, 4, 5, 6, 7, 8, 9, 10]
        }


        edges_req = []
        for e in graph["edges"]:
            edges_req.append(network_analytics_node_importance_pb2.Edge(edge=e))

        graph_in = network_analytics_node_importance_pb2.Graph(nodes=graph["nodes"], edges=edges_req)



        center_req = network_analytics_node_importance_pb2.CentralNodeRequest(graph=graph_in)
        resp = stub.CentralNodes(center_req)

        # print('done')
        print(resp)
        output.put((1,resp.message))

    except  Exception as e:
        # print('done')
        output.put((0,str(e)))


def named_entity_disambiguation(output):



    try:
        channel = grpc.insecure_channel('tz-services-1.snet.sh:8006')
        # channel = grpc.insecure_channel('localhost:5001')
        stub = NamedEntityDisambiguation_pb2_grpc.DisambiguateStub(channel)

        req = NamedEntityDisambiguation_pb2.Input(input="I love New York city in Africa.")
        # req = NamedEntityDisambiguation_pb2.Input(input="I love me.")
        # req = NamedEntityDisambiguation_pb2.Input(input=".")
        resp = stub.named_entity_disambiguation(req)
        resp_message = 'success' if 'disambiguation' in str(resp) else 'failed'
        # print(resp)

        print('done')

        if resp_message == 'success':
            output.put((1,'success'))
        else:
            output.put((0,'failed'))

    except  Exception as e:
        print('done')
        output.put((0,str(e)))



def topic_analysis(output,x):

    # RAM estimation formula
    # s = (float(docs * W) + float(docs + W) * float(K * docs * 2)) * 8.0 / float(G)

    multiplier = 0
    time.sleep(x*multiplier)

    # sample_doc = 'topic_analysis/test_doc.txt'
    sample_doc = 'topic_analysis/test_doc_4MB.txt'
    with open(sample_doc, 'r') as f:
        docs = [f.read()]


    # print(docs)

    try:
        channel = grpc.insecure_channel('tz-services-1.snet.sh:2301')
        # channel = grpc.insecure_channel('localhost:5000')
        stub = topic_analysis_pb2_grpc.TopicAnalysisStub(channel)
        req = topic_analysis_pb2.PLSARequest(docs=docs, num_topics=2, maxiter=22, beta=1)

        resp = stub.PLSA(req)

        print('done')
        print(resp)
        output.put((1,resp.message))

    except  Exception as e:
        print('done')
        output.put((0,str(e)))


def emotion_recognition(output):

    img = 'emotion_recognition/t.jpeg'
    with open(img, 'rb') as f:
        img = f.read()
    image_64 = base64.b64encode(img).decode('utf-8')


    # print(docs)

    try:
        channel = grpc.insecure_channel('34.216.72.29:6305')
        stub = EmotionService_pb2_grpc.EmotionRecognitionStub(channel)
        req = EmotionService_pb2.RecognizeRequest(image_type='jpeg', image=image_64)

        resp = stub.classify(req)

        resp_message = 'success' if 'faces' in str(resp) else 'failed'

        if resp_message == 'success':
            output.put((1, 'success'))
        else:
            output.put((0, 'failed'))

        print('done')
        print(resp)
        output.put((1,''))

    except  Exception as e:
        print('done')
        output.put((0,str(e)))


if __name__ == '__main__':

    start_time = time.time()

    # multi_pro('find_central_nodes',100)
    # multi_pro('named_entity_disambiguation',200)
    multi_pro('topic_analysis',1)
    # multi_pro('emotion_recognition',70)


    # find_central_nodes()

    end_time = time.time()

    print('Testing took ' + str(((end_time - start_time) )) + ' seconds.')
    print('Testing took ' + str(((end_time - start_time) / 60)) + ' minutes.')

    pass
