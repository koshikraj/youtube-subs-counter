#!/usr/bin/python

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import asyncio
import json
import falcon



# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyAFtUxiNge2hIkZ8gJEc5k6QD8T1TH19Gc'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
max_results = 5



def get_connection_object():

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

connection = get_connection_object()


def get_channel_details(username):

    global connection
    if not connection:
        connection = get_connection_object()

    # Call the channels.list method to retrieve results matching the specified channel user name.
    search_response = connection.channels().list(part='snippet,contentDetails,statistics',
                                                 forUsername=username).execute()
    return {'url': search_response['items'][0]['snippet']['thumbnails']['default']['url'],
            'username': username,
            'subscribers': search_response['items'][0]['statistics']['subscriberCount']}




async def get_subs_count(username):

    global connection
    if not connection:
        connection = get_connection_object()

    # Call the channels.list method to retrieve results matching the specified channel user name.
    search_response = connection.channels().list(part='statistics',
                                                 forUsername=username).execute()

    await asyncio.sleep(1)
    return search_response['items'][0]['statistics']['subscriberCount']


async def subs_counter_compared(res):

    task1 = asyncio.get_event_loop().create_task(get_subs_count('pewdiepie'))
    task2 = asyncio.get_event_loop().create_task(get_subs_count('tseries'))

    # simulate a no-op blocking task. This gives a chance to the network requests scheduled above to be executed.
    await asyncio.sleep(0.5)

    # wait for the network calls to complete. Time to step off the event loop using await!
    await asyncio.wait([task1, task2])

    res.status = falcon.HTTP_200
    res.body = json.dumps({'status': True,
                           'data': {'pewdiepie': task1.result(),
                                    'tseries': task2.result()},

                           'message': 'success'
                           })
