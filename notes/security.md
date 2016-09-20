# Basic Security

When writing your applications, you should be keeping in mind ways that people can attack them and defend against unwanted data, hardware, and functionality access.
Security breaches cost you trust and money.

## SQL Injection

**Injection vulnerabilities** are when user input is accidentally placed in an unexpected context and can change program behavior.
Most of these vulnerabilities come from not escaping user input.

**SQL injection** is taking advantage of dirty user input in SQL queries.
SQL is the text-based language interface with many DBs.
Since the language is text and data is often text, it's possible to accidentally interpret data as instructions if the data is not escaped.
This can lead to data loss or modification or leaks.

```sql
UPDATE posts SET text = 'This is my post text!' WHERE id = 43;
UPDATE posts SET text = 'This is wrong'; UPDATE users SET is_super = true WHERE id = 99; --' WHERE id = 43;
```

Ensure you're escaping your data if you're manually constructing SQL queries.

Remember the legend of [little Bobby Tables](https://www.xkcd.com/327/).

### XSS

Another injection attack via JavaScript is **XSS** or a **cross site scripting vulnerability**.
If user text is not escaped when rendered to a template, JavaScript code can be included and run on the user's browser.
This could steal their session tokens or other data.

```html
<section>
  <h2>Blog Comments</h2>
  <ol>
    <li>Such a cool site!</li>
    <li>Ehh, fine <script>uploadSessionToken();</script></li>
  </ol>
</section>
```

You also don't have to worry about this if you use standard Django templating.
If you have a way to have users input HTML, ensure it's free of tags that can "do things".

### Root Breaking

Be aware when your app is accessing resource on the local filesystem in a programmatic way.
If the user has some direct control over that resource, it's possible they could access arbitrary files and scope out server information.

An egregious example.

In `urls.py`:

```py
urlpatterns = [
    url(r'^image/(?<media_path>.+)$', views.render_media, name='media'),
]
```

In `views.py`:

```py
def render_media(request, media_path):
    with open(APP_ROOT + media_path) as media_file:
        return HttpResponse(media_file.read())
```

Then someone could go to `GET /image/../../../../etc/passwd` and get out system information.

Either use arbitrary IDs or do some sort of smart path containment when accepting input.

Not just file reading falls prey to this, any file modification, like ownership change or moving could be abused.

## Avoid Secret Eval

Some Python systems effectively run [eval()](https://docs.python.org/3.5/library/functions.html#eval) to function.
[Pickle](https://docs.python.org/3.5/library/pickle.html), and [__import__](https://docs.python.org/3.5/library/functions.html#__import__) work this way.
Eval will execute Python code strings, so if someone can get the code they want to that point, it will run and perhaps reveal info.

Although JSON doesn't use `eval()`, think about how you're using the input.

## ID Enumeration and Authentication

If you don't want all of your resources public, make sure to store access control lists in your models.

Let's say you're making a secret note app and it has a route `GET /note/ID`.
Even if you implement logins and the main page only shows links to IDs by that user, if there isn't per-note view user checking, someone could guess the IDs of another note and see it.

Always do specific user checking in sensitive views, not just that they're logged in.

## Client Distrust

There is basically no way to guarantee that a client's browser is actually running your JavaScript:

* Someone could "view source" and change it
* Someone could man-in-the-middle any JS loaded of plain HTTP
* Someone could install a malicious browser extension that modifies the JS globals

This means any of the responses that your JS sends to your server via AJAX are totally controllable by an attacker.

Client-side validation or escaping or constraint enforcement can be circumvented and should never be done in JavaScript.

## Unmanaged Languages

Python is great in that it is high enough level that you can't actually interact with how the interpreter is running on the hardware and Python ensures correct semantics.
Unless there's a bug in the Python interpreter itself.

Lower level languages have the unfortunate capability of data and instructions are much more intertwined.
You can read up on how that allows for corrupted data to possibly change what the server runs.

* Buffer overflow
* Stack smashing

## Articles

Here are some relevant articles:

* https://docs.djangoproject.com/en/1.10/topics/security/
* http://www.webappsec.org/projects/articles/062105.shtml
* https://www.nccgroup.trust/us/about-us/newsroom-and-events/blog/2011/august/javascript-cryptography-considered-harmful/
