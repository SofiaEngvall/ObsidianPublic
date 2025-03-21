
call function with `go myfunc()` and it will run in the bg

the main program will continue, and might even end

make sure to sync shared memory

### Channels

used to send data between

`ch := make(chan int)`

`ch <- v`  Send v to channel ch.
`v := <-ch`  Receive from ch, put in v

By default, sends and receives block until the other side is ready. This allows goroutines to synchronize without explicit locks or condition variables.

`ch := make(chan int,5)`  set buffer size to 5 = 5 queue lenght - If we don't use this the send will be paused until the next receive






