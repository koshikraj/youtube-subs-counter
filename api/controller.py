import json
import falcon


import asyncio

from youtube_driver import get_channel_details, get_subs_count, subs_counter_compared


class ChannelDetails:

    def on_get(self, req, res):

        try:
            channel_details = get_channel_details(req.get_param('username', ''))
            res.status = falcon.HTTP_200
            res.body = json.dumps({'status': True,
                                   'data': channel_details,
                                   'message': 'success'
                               })
        except Exception as e:
            res.status = falcon.HTTP_400
            res.body = json.dumps({'status': False,
                                   'data': channel_details,
                                   'message': str(e)
                                   })


class SubsCounter:

    def on_get(self, req, res):
        try:
            username = req.get_param('username', '')
            subs_count = get_subs_count(username)

            res.status = falcon.HTTP_200
            res.body = json.dumps({'status': True,
                                   'data': {
                                       'username': username,
                                       'subs_count': subs_count
                                   },

                                   'message': 'success'
                                   })
        except Exception as e:
            res.status = falcon.HTTP_400
            res.body = json.dumps({'status': False,
                                   'data': [],
                                   'message': str(e)
                                   })


class SubsCounterCompared:

    def on_get(self, req, res):
        try:

            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.ensure_future(subs_counter_compared(res)))

            # Response body is created by the sub routine

        except Exception as e:
            res.status = falcon.HTTP_400
            res.body = json.dumps({'status': False,
                                   'data': [],
                                   'message': str(e)
                                   })

