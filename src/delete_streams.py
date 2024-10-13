import asyncio

import nats
from nats.aio.client import Client
from nats.js.client import JetStreamContext


async def main():
    nc: Client = await nats.connect("nats://127.0.0.1:4222")

    # get jetstream context
    js: JetStreamContext = nc.jetstream()

    # get all streams
    streams = await js.streams_info()

    # delete all streams
    for stream in streams:
        stream_name = stream.config.name
        print(f"Delete stream: {stream_name}")
        await js.delete_stream(stream_name)

    print("All streams delete")


asyncio.run(main())
