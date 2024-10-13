import asyncio

import nats


async def main():
    # connect to nats
    nc = await nats.connect("nats://127.0.0.1:4222")

    # message for send
    message = "Hello World!"

    # subject in which the message is sent
    subject = "test.subject"

    # publish a message to the specified topic
    await nc.publish(subject, message.encode())

    print(f"Message '{message}' published in subject '{subject}'")

    # close the connection
    await nc.close()


asyncio.run(main())
