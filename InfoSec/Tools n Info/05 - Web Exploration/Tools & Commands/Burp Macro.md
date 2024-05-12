
https://tryhackme.com/r/room/burpsuiteintruder

1. Navigate to `http://10.10.20.108/admin/login/`. Activate **Intercept** in the Proxy module and attempt to log in. Capture the request and send it to Intruder.
    
2. Configure the positions the same way as we did for brute-forcing the support login:
    
    - Set the attack type to "Pitchfork".
    - Clear all predefined positions and select only the username and password form fields. Our macro will handle the other two positions.
        
    
    ![Showing the predefined positions](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/cdade963a8004b0d9da03e075a60f3aa.png)
    
3. Now switch over to the Payloads tab and load in the same username and password wordlists we used for the support login attack.
    
    Up until this point, we have configured Intruder in almost the same way as our previous credential stuffing attack; this is where things start to get more complicated.
    
4. With the username and password parameters handled, we now need to find a way to grab the ever-changing loginToken and session cookie. Unfortunately, "recursive grep" won't work here due to the redirect response, so we can't do this entirely within Intruder – we will need to build a macro.
    
    Macros allow us to perform the same set of actions repeatedly. In this case, we simply want to send a GET request to `/admin/login/`.
    
    Fortunately, setting this up is a straightforward process.
    
    - Switch over to the main "Settings" tab at the top-right of Burp.
    - Click on the "Sessions" category.
    - Scroll down to the bottom of the category to the "Macros" section and click the **Add** button.
    - The menu that appears will show us our request history. If there isn't a GET request to `http://10.10.20.108/admin/login/` in the list already, navigate to this location in your browser, and you should see a suitable request appear in the list.
    - With the request selected, click **OK**.
    - Finally, give the macro a suitable name, then click **OK** again to finish the process.
    
    There are a lot of steps here, comparatively speaking, so the following GIF shows the entire process:
    
    ![Process showing the addition of the macro](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/3b370cfce8a050faf415c7d9a5a8227e.gif)
    
5. Now that we have a macro defined, we need to set Session Handling rules that define how the macro should be used.
    
    - Still in the "Sessions" category of the main settings, scroll up to the "Session Handling Rules" section and choose to **Add** a new rule.
    - A new window will pop up with two tabs in it: "Details" and "Scope". We are in the Details tab by default.
        
    
    ![Window showing the details and scope](https://assets.muirlandoracle.co.uk/thm/modules/burp/38ceffeebf99.png)
    
    - Fill in an appropriate description, then switch to the Scope tab.
    - In the "Tools Scope" section, deselect every checkbox other than Intruder – we do not need this rule to apply anywhere else.
    - In the "URL Scope" section, choose "Use suite scope"; this will set the macro to only operate on sites that have been added to the global scope (as was discussed in [Burp Basics](https://tryhackme.com/room/burpsuitebasics)). If you have not set a global scope, keep the "Use custom scope" option as default and add `http://10.10.20.108/` to the scope in this section.
        
        ![Change the URL scope](https://assets.muirlandoracle.co.uk/thm/modules/burp/4d3fc6d19a12.png)
        
6. Now we need to switch back over to the Details tab and look at the "Rule Actions" section.
    
    - Click the **Add** button – this will cause a dropdown menu to appear with a list of actions we can add.
    - Select "Run a Macro" from this list.
    - In the new window that appears, select the macro we created earlier.
        
    
    As it stands, this macro will now overwrite all of the parameters in our Intruder requests before we send them; this is great, as it means that we will get the loginTokens and session cookies added straight into our requests. That said, we should restrict which parameters and cookies are being updated before we start our attack:
    
    - Select "Update only the following parameters and headers", then click the **Edit** button next to the input box below the radio button.
    - In the "Enter a new item" text field, type "loginToken". Press **Add**, then **Close**.
    - Select "Update only the following cookies", then click the relevant **Edit** button.
    - Enter "session" in the "Enter a new item" text field. Press **Add**, then **Close**.
    - Finally, press **OK** to confirm our action.
        
    
    The following GIF demonstrates this final stage of the process:
    
    ![Showing the added macro](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/250c140897e3b470093e7232c70c07cf.gif)
    
7. Click **OK**, and we're done!
    
8. You should now have a macro defined that will substitute in the CSRF token and session cookie. All that's left to do is switch back to Intruder and start the attack!
    
    **Note:** You should be getting 302 status code responses for every request in this attack. If you see 403 errors, then your macro is not working properly.
    
9. As with the support login credential stuffing attack we carried out, the response codes here are all the same (302 Redirects). Once again, order your responses by length to find the valid credentials. Your results won't be quite as clear-cut as last time – you will see quite a few different response lengths: however, the response that indicates a successful login should still stand out as being significantly shorter.
    
10. Use the credentials you just found to log in (you may need to refresh the login page before entering the credentials).