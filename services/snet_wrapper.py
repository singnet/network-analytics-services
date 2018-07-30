# Tested on python3.6

# import logging

from aiohttp import web
from jsonrpcserver.aio import methods
from jsonrpcserver.exceptions import InvalidParams

# logger = logging.getLogger(__name__)
app = web.Application()



@methods.add
async def bipartite_graph(**kwargs):


    print('Somebody is in.')

    param1 = kwargs.get("param1", None)
    print(param1)

    return {"test": "test_response"}




async def handle(request):
    request = await request.text()
    response = await methods.dispatch(request)
    if response.is_notification:
        return web.Response()
    else:
        return web.json_response(response, status=response.http_status)







__end__ = '__end__'



if __name__ == '__main__':


    # logging.basicConfig(level=config.LOG_LEVEL, format="%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s")
    app.router.add_post('/', handle)
    web.run_app(app, host="127.0.0.1", port=5000)

