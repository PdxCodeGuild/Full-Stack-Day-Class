# CSRF

Let's say your website has an important "verb endpoint".

```
GET /transfer_money/FROM_USER/to/TO_USER?amount_dollars=AMOUNT_DOLLARS
```

If malicious website was to learn of this endpoint and make a link to it in their page, then any user that clicks on the link will perform that action without their consent!

This is called a **cross-site request forgery** or **CSRF**.

Django has some defenses against this enabled by default.

1.  Never allow `GET` requests to modify data.

1.  All `POST` requests have to have a valid **CSRF token** as part of the response.

    This can be put in via `{% csrf_token %}` in a form.

A CSRF token is a random number that the server remembers and sends to the client as part of all `POST` forms.
Then all form responses are checked for the correct token number.
If the token isn't correct, the request is rejected.

The Django docs have [more notes on CSRF protection](https://docs.djangoproject.com/en/1.10/ref/csrf/).
