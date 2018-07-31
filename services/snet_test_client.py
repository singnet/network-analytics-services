# Tested on python3.6

import logging
import time

def test_1():

    import jsonrpcclient

    resp = jsonrpcclient.request('http://127.0.0.1:5000','bipartite_graph',{'nodes':{"bipartite_0": [8, 7], "bipartite_1": [3, 4]},"edges": [[3, 8], [4, 7]]})

    # resp = jsonrpcclient.request('http://127.0.0.1:5000','bipartite_graph',{'nodes':{"bipartite_0": [8, 7], "bipartite_1": [3, 4]},"edges": [[7, 7]]})
    # print(type(resp))
    # print((resp['test']))




def test_2():

    import aiohttp
    import asyncio
    from jsonrpcclient.aiohttp_client import aiohttpClient

    async def main(loop):
        async with aiohttp.ClientSession(loop=loop) as session:
            client = aiohttpClient(session, 'http://127.0.0.1:5000/')
            print('hi')

            try:
                response = await client.request('bipartite_graph',{'noddes':{"bipartite_0": [8, 7], "bipartite_1": [3, 4]},"edges": [[3, 8], [4, 7]]})
                print(response)

            except Exception as e:

                logging.exception("message")

                print('error message:',str(e))



    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

def test_3():
    import jsonrpcclient

    input_0_0 = {"bipartite_0": [8, 7, 6, 10, 12, 13], "bipartite_1": [5, 3, 4, 1, 2, 3],
                 "edges": [[3, 8], [4, 7], [5, 6], [3, 7]]}
    input_0_1 = [8, 7]
    input_0_2 = 'none'

    resp = jsonrpcclient.request('http://127.0.0.1:5000', 'projected_graph',
                                 {'bipartite_graph':input_0_0, "nodes": input_0_1, 'weight':'kk'})


if __name__ == '__main__':

    test_1()
    # print('Using test_2')
    time.sleep(2)
    # print('Hi')
    test_1()
    # test_2()
    # test_3()
