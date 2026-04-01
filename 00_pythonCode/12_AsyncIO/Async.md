# Async Python

Multiprocessing

Multithreading


Async Nature of python solving problem

* fetch 10 webpages
* Read 20 files
* send 100 HTTP requests

#### async def

* declare a coroutine- special function feature that can be paused.

#### await

* Pauses the execution until the result is ready

#### asyncio

* Built in python library

#### Event Loop

* same as the js event loop
* the engine that runs and schedule co-routine in the loop

#### Blocking vs Non-Blocking

* Blocking:
  * time.sleep(2)
* Non-Blocking:
  * await asyncio.sleep(2)
