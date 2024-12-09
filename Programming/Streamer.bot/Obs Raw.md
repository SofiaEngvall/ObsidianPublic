
![[Images/Pasted image 20240809142637.png]]

or

```c#
using System;

public class CPHInline
{
	public bool Execute()
	{
		//{"requestType":"GetSceneList","requestData":{}}
		CPH.LogInfo( CPH.ObsSendRaw("GetSceneList", "", 0));
		
		return true;
	}
}
```
