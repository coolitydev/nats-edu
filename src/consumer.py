import asyncio
from asyncio import CancelledError

import nats
from nats.aio.msg import Msg


async def message_handler(msg: Msg) -> None:
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received a message on '{subject}': {data}")


async def main():
    # connect to nats
    nc = await nats.connect("nats://127.0.0.1:4222")

    # subject for subscription
    subject = "test.subject"

    # subscribe to subject
    await nc.subscribe(subject, cb=message_handler)

    print(f"Subscribed to subject '{subject}'")

    # building a future for keeping connections open
    try:
        await asyncio.Future()
    except CancelledError:
        pass
    finally:
        # close connection
        await nc.close()

asyncio.run(main())