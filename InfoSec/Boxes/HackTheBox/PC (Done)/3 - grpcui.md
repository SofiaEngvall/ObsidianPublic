
[github](https://github.com/fullstorydev/grpcui)

```sh
┌──(kali㉿kali)-[~]
└─$ go install github.com/fullstorydev/grpcui/cmd/grpcui@latest  
go: downloading github.com/fullstorydev/grpcui v1.3.1
go: downloading github.com/fullstorydev/grpcurl v1.8.6
go: downloading github.com/jhump/protoreflect v1.12.0
go: downloading github.com/pkg/browser v0.0.0-20180916011732-0a3d74bf9ce4
go: downloading golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9
go: downloading google.golang.org/grpc v1.45.0-dev.0.20220218222403-011544f72939
go: downloading github.com/golang/protobuf v1.5.2
go: downloading google.golang.org/protobuf v1.28.0
go: downloading golang.org/x/sys v0.0.0-20220406163625-3f8b81556e12
go: downloading golang.org/x/net v0.0.0-20200822124328-c89045814202
go: downloading github.com/envoyproxy/go-control-plane v0.9.10-0.20210907150352-cf90f659a021
go: downloading google.golang.org/genproto v0.0.0-20200526211855-cb27e3aa2013
go: downloading github.com/cespare/xxhash/v2 v2.1.1
go: downloading github.com/cncf/udpa/go v0.0.0-20210930031921-04548b0d99d4
go: downloading github.com/cncf/xds/go v0.0.0-20211011173535-cb28da3451f1
go: downloading github.com/envoyproxy/protoc-gen-validate v0.1.0
go: downloading golang.org/x/text v0.3.7
go: downloading golang.org/x/oauth2 v0.0.0-20200107190931-bf48bf16ab8d
go: downloading github.com/census-instrumentation/opencensus-proto v0.2.1
go: downloading cloud.google.com/go v0.56.0
```

```sh
┌──(kali㉿kali)-[~]
└─$ /home/kali/go/bin/grpcui --plaintext 10.10.11.214:50051
'gRPC Web UI available at http://127.0.0.1:32989/

```

![[grpcui.png]]

create account, login as account, catch getInfo request with burp


