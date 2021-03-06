import asyncio
from asyncore import write
from lib2to3.pgen2.token import OP
import random
from typing import Optional
from typing import Any
from sys import version_info

class tcpGameBase():
    def __init__(self, questions = None, minutes_to_start:int = 0) -> None:
        self.client_writers = set()
        self.client_readers = set()
        self.client_id:int = Optional[int]
        self.minutes_to_start = minutes_to_start
        self._loop = asyncio.get_event_loop()
        self.is_runing = False



        if self._loop is None:
            raise Exception
        

    async def send_string(writer:asyncio.StreamWriter, 
                            message:str):
        text = f'{message}\n'
        try:
            writer.write(text.encode())
            await writer.drain()
        except ConnectionResetError as e:
            return e

    async def get_response(reader:asyncio.StreamReader):
        data = await reader.read(256)
        message = data.decode().strip()
        return message
    
    async def main(self, reader:asyncio.StreamReader,
                         writer:asyncio.StreamWriter):
        print('123')
        self.client_readers.add(reader)
        self.client_writers.add(writer)

        print(reader)
        print(writer)
        data = await reader.read(256)
        message = data.decode().strip()
        print(message)



        text = f'{message}\n'
        try:
            writer.write(text.encode())
            await writer.drain()
        except ConnectionResetError as e:
            return e
        
        
        




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    gameBaseClass = tcpGameBase()
    server_gen = asyncio.start_server(
        gameBaseClass.main, '127.0.0.1', 4009)

    server = loop.run_until_complete(server_gen)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        # print('CTRL C PRESS')
        loop.stop()  # Press Ctrl+C to stop
    finally:
        loop.stop()