
```sh
┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ curl 144.126.192.69 -H "Host: rust.ctfio.com"                                            
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
</body>
</html>
```

```sh
┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ curl -L 144.126.192.69 -H "Host: rust.ctfio.com"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EvilCorp Marketing - Online Marketing Services</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
<a href="https://app.rust.ctfio.com" class="link-button" >Customer Login</a>
<header>
    <h1>EvilCorp Marketing</h1>
    <nav>
        <ul>
            <li><a href="#services">Services</a></li>
            <li><a href="#about">About Us</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
</header>
<main>
    <section class="hero">
        <div class="hero-content">
            <h2>Unlock Your Business Potential with Online Marketing</h2>
            <p>At EvilCorp Marketing, we specialize in driving your business to new heights through powerful online marketing strategies. Reach your target audience and boost your online presence with our expert team.</p>
            <a href="#contact" class="btn">Get Started</a>
        </div>
    </section>
    <section id="services">
        <h2>Our Services</h2>
        <div class="services-container">
            <div class="service-item">
                <h3>Search Engine Optimization (SEO)</h3>
                <p>Improve your website´s visibility on search engines and attract more organic traffic.</p>
            </div>
            <div class="service-item">
                <h3>Pay-Per-Click Advertising (PPC)</h3>
                <p>Drive targeted traffic to your website through effective PPC campaigns.</p>
            </div>
            <div class="service-item">
                <h3>Social Media Marketing</h3>
                <p>Engage with your audience and build a loyal following on social media platforms.</p>
            </div>
        </div>
    </section>
    <section id="about">
        <h2>About Us</h2>
        <p>EvilCorp Marketing is a leading digital marketing agency with a proven track record of helping businesses succeed online. Our team of experts is dedicated to crafting tailored strategies that align with your business goals and deliver measurable results.</p>
    </section>
</main>
<footer>
    <p>&copy; 2023 EvilCorp Marketing. All rights reserved.</p>
</footer>
</body>
</html>   
```
