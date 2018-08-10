# Tested on python3.6

from aiohttp import web
from jsonrpcserver.aio import methods
from jsonrpcserver.exceptions import InvalidParams
from jsonrpcserver.exceptions import ServerError
import time
import bipartite_graphs
import logging


# logger = logging.getLogger(__name__)
app = web.Application()



@methods.add
async def bipartite_graph(**kwargs):

    print('>>>>>>>>>>>>>>In endpoint bipartite_graph')
    print(time.strftime("%c"))

    nodes = kwargs.get("nodes", None)
    edges = kwargs.get("edges", None)

    if nodes is None:
        InvalidParams.message = 'nodes parameter is required'
        raise InvalidParams
    else:
        print('nodes parameter is present')


    if edges is None:
        InvalidParams.message = 'edges parameter is required'
        raise InvalidParams
    else:
        print('edges parameter is present')


    b = bipartite_graphs.BipartiteGraphs()


    try:

        ret = b.bipartite_graph(nodes,{'edges':edges})
        if ret[0]:
            return ret[2]
        else:
            InvalidParams.message = ret[1]
            raise  InvalidParams


    except Exception as e:

        logging.exception("message")

        ServerError.message = str(e)
        raise ServerError


@methods.add
async def projected_graph(**kwargs):

    print('>>>>>>>>>>>>>>In endpoint projected_graph')
    print(time.strftime("%c"))

    bipartite_graph = kwargs.get("bipartite_graph", None)
    nodes = kwargs.get("nodes", None)
    weight = kwargs.get("weight", None)

    if bipartite_graph is None:
        InvalidParams.message = 'bipartite_graph parameter is required'
        raise InvalidParams
    else:
        print('bipartite_graph parameter is present')

    if nodes is None:
        InvalidParams.message = 'nodes parameter is required'
        raise InvalidParams
    else:
        print('nodes parameter is present')

    if weight is None:
        InvalidParams.message = 'weight parameter is required'
        raise InvalidParams
    else:
        print('weight parameter is present')


    b = bipartite_graphs.BipartiteGraphs()


    try:

        ret = b.projected_graph(bipartite_graph,{'nodes':nodes},weight)
        if ret[0]:
            return ret[2]
        else:
            InvalidParams.message = ret[1]
            raise  InvalidParams


    except Exception as e:

        logging.exception("message")

        ServerError.message = str(e)
        raise ServerError





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
    # web.run_app(app, host="127.0.0.1", port=5000)
    web.run_app(app, host="0.0.0.0", port=35000)

