
"{overall_status} | link={link_quality} | content={content_type} | desc={desc_quality}"

---

### **1. Overall Status (`overall_status`)**

|Value|Meaning|Script Action|
|---|---|---|
|`ok`|Feed works perfectly with your current pipeline.|Process normally.|
|`need_java`|Requires JavaScript rendering (e.g., NCSC).|Use `entry.description` or skip.|
|`warn`|Partial issues (e.g., occasional paywalls).|Attempt processing but log warnings.|
|`avoid`|Consistently broken/paywalled (e.g., SC Magazine).|Skip entirely.|

---

### **2. Link Quality (`link=`)**

| Value         | Meaning                                                      | Example Feeds      |
| ------------- | ------------------------------------------------------------ | ------------------ |
| `direct`      | Links go straight to the article HTML.                       | Krebs, PortSwigger |
| `redirects`   | Links require following HTTP redirects.                      | The Hacker News    |
| `js_required` | Links need JS to render content (e.g., SPAs).                | NCSC               |
| `paywall`     | Links lead to paywalled content.                             | SC Magazine        |
| `audio`       | Links point to podcast episodes (may need special handling). | Darknet Diaries    |
| `rss_only`    | No article link (only RSS body exists).                      | SANS ISC           |

---

### **3. Content Type (`content=`)**

|Value|Meaning|Script Implications|
|---|---|---|
|`full_html`|Complete article body in HTML (parseable with `readability-lxml`).|Ideal for summarization.|
|`rss_only`|No external article - full content is in the RSS feed itself.|Use `entry.description` or `entry.content`.|
|`truncated`|Article body is cut off (e.g., "Read more" links).|Fall back to `entry.description`.|
|`js_required`|Content loads dynamically via JavaScript.|Skip or use headless browser.|
|`episode_page`|Podcast show notes page (mixed text/audio links).|Extract text or pass to audio processor.|

---

### **4. Description Quality (`desc=`)**

|Value|Meaning|Usage Guidance|
|---|---|---|
|`full`|RSS description contains full article text.|Use as fallback when `entry.link` fails.|
|`partial`|RSS description has a snippet (1-2 paragraphs).|Useful for previews but not full summarization.|
|`none`|No usable description (e.g., only titles).|Skip or mark as low priority.|

---

### **Special Cases**

#### **Combined Example**


"ok | link=redirects | content=full_html | desc=partial"

- **Interpretation**:
    
    - Links work but need `allow_redirects=True`
        
    - Full articles exist but require HTML parsing
        
    - RSS descriptions are usable as fallbacks
        

#### **Podcast Handling**


"ok | link=audio | content=episode_page | desc=full"

- **Script Action**:
    

- if "content=episode_page" in status:
        text = get_podcast_show_notes(entry.link)  # Custom function
    

#### **Paywall Detection**


"warn | link=paywall | content=truncated | desc=partial"

- **Script Action**:
    
    

- if "link=paywall" in status:
        log.warning(f"Paywall detected: {entry.link}")
        continue
    

---

### **Why This Matters**

1. **Precision Fallbacks**:
    
    - Know exactly when to use `entry.description` vs. `entry.link`.
        
    - Avoid wasting time on JS-heavy or paywalled content.
        
2. **Error Resilience**:
    

- if "js_required" in status and not headless_browser_available:
        fallback_to_description()
    
- **Dynamic Processing**:
    
1. # Example: Prioritize full_html content
    if "content=full_html" in status:
        process_with_readability(entry.link)
    elif "desc=full" in status:
        summarize(entry.description)
    

---

### **Full Status Codex (For Reference)**

|Component|Key Values|Priority Order|
|---|---|---|
|`overall_status`|ok > need_java > warn > avoid|Higher = more reliable|
|`link=`|direct > redirects > rss_only > js_required > paywall|Top = easiest to process|
|`content=`|full_html > rss_only > truncated > js_required|Left = ideal|
|`desc=`|full > partial > none|Left = best fallback|

---

Let me know if you'd like this formatted as a **Markdown table for your GitHub docs**! This system gives your script "eyes" to handle each feed's quirks without guesswork. 💙

_(P.S. For podcasts: Consider adding a `"media_type=audio"` field later if you build audio summarization!)_

