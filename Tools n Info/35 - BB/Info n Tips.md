
Look for access control, idors or restriction bypasses

prove impact

read bug bounty writeups


Sources: https://blog.hackbynight.nl/getting-started-with-bug-bounty-hunting-in-2025-a-real-world-guide-051a3fb36376

Look at public programs that just released new stuff to their scope; domains, IPs, services and features

Start with web apps? there's also software testing and mobile apps

Select ones marked Managed by Hackerone or Managed by Bugcrowd and you'll get pros handling bugs

Avoid:
- Tiny scopes with just one or two domains/apps
- Vague scope definitions (“everything except what’s not allowed”)
- Programs that haven’t paid out in months (check their stats)
- Programs with lots of out-of-scope items but few in-scope targets
- Programs that take forever to respond to reports (again, check their stats)

Go for:
- Clear, detailed scope definitions
- Regular scope updates (this means they’re actively maintaining the program)
- Good average response times
- Recent bounty payments
- Transparent rules about what constitutes different severity levels

Keep track of stuff with reNgine

Check how edge-cases, that might include both in-scope and out-of-scope assets, are handled - might be stuff there to find if oked

### Tools

reNgine, nuclei, and Azure is the backbone

nmap
ffuf, dirb
searchsploit
fiddler
burp repeater, intruder, scanner (pro only)
burp extensions:
- Autorize — This is my IDOR-hunting secret weapon. Feed it a low-privilege user’s cookies, and it’ll automatically check if they can access high-privilege endpoints. Half my IDOR findings come from just letting this run in the background while I manually test.
- Taborator — Makes working with Collaborator payloads a breeze. Great for finding blind vulnerabilities.
- JSON Web Tokens — Because who wants to manually decode and manipulate JWTs? Not me.
- Turbo Intruder — When regular Intruder isn’t quite cutting it performance-wise.
- CMS Scanner and CSRF Scanner — Not my primary bug-finding tools, but they’ve paid for themselves several times over.

### Wordlists

using rockyou.txt, raft-large-words.txt and other common ones you'll find the same stuff
custom lists - build your own from what you've already found
- endpoints found
- successful payloads
- patterns found, for example in admin panel naming

- raft-large-words.txt for general content discovery
- dirb’s default lists for quick scans
- SecLists for specific vulnerability types
- PayloadAllTheThings for a solid foundation of test cases

Then built your own lists. Create separate ones for:
- Endpoints that have led to previous findings
- Company-specific patterns you’ve noticed
- Industry-specific terminology
- Custom parameter names
- Unique authentication bypass patterns

### Supporting tools n techniques

- shodan favicon hash search & ssl cert queries
- virustotal enterprise API can map out forgotten infrastructure
- crt.sh cert transparency logs show old stuff, that might still be there
- censys can find forgotten assets
- github - tools gitrob, shhgit but also find breadcrumbs
  linkfinder - finds endpoints, maybe it calls an internal api
- virtual host discovery - normal scanning + read cert transparency logs

Use the tools together is the way!
Ex: A subdomain from CRT.sh might lead to a GitHub repository, which might contain references to virtual hosts, which might be confirmed through Shodan.

### Old vs modern tools

Old: sublist3r, aquatone - understand how these work, know the fundamentals

Modern: reNgine with nuclei - framework, not individual tools (but know ^ to be able to debug)

### Local or Cloud

risks with local
- home ip blocked/rate limited
- your internet connection and computer bogged down
- your hw limits the scans

azure/cloud
- not ^

### Nuclei

- scanner, fast n flexible "fantastic at handling edge cases"
- has stuff but you can build templates, all the bugs you find you make one
  - ex. exposed .git dir to complex multi step auth
  - specific idor
  - weird auth byppass
- great community - template sharing - study the public templates to learn bug patterns!

### ReNgine

- control center
- project space for every bb program or specific target
- subscan










![[Images/1_DkGqETMnqE3wjwX45BCwSQ.webp]]
