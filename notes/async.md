# Asynchronous Programming

The programming languages we've learned thus far have been basically [imperative](/notes/py-program-flow.md) and single-threaded.
All values have to be resolved in order from start to finish.
There is only one thing being executed at once.
No operation can begin util the previous one is done.

There are some models for breaking this "one instruction at a time in order" model of computation.

**Concurrency** is keeping track of multiple tasks of work and their results.
**Parallelism** is performing tasks simultaneously.

There are three common situations that warrant async programming.
We'll only really learn the first one in this class.

## 1. IO / Event Wait

Often you need to relieve a lot of data from network, disk, or somewhere.
While the computer is waiting for that data, in a standard model, it can't do anything else.
But it's not _doing_ anything while waiting, and the computer could be using that free time.

Promises and callbacks allow you to queue up work to be done as soon as the data has been received.

## 2. Heavy Blocking Work

Sometimes you need to do a lot of computation.
But you also want your program to stay responsive during that time.
Modern computers also have many CPU cores and could work on more things simultaneously.

Separate threads or processes allow multiple computations to happen simultaneously.

## 3. Low Latency

Sometimes you need to handle a lot of things simultaneously.
Like server network connections.

Coroutines allow multiple "threads" of execution, but without the overhead of real threads.
