# Tested on python3.6


def test_1():

    import jsonrpcclient

    resp = jsonrpcclient.request('http://127.0.0.1:5000','bipartite_graph',{'param1':'Hii'})
    print(type(resp))
    print((resp['test']))




def test_2():

    import aiohttp
    import asyncio
    from jsonrpcclient.aiohttp_client import aiohttpClient

    async def main(loop):
        async with aiohttp.ClientSession(loop=loop) as session:
            client = aiohttpClient(session, 'http://127.0.0.1:5000/')
            response = await client.request('bipartite_graph',{'param1':'Hii'})
            print(response)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))



if __name__ == '__main__':

    test_1()
    # print('Using test_2')
    # test_2()