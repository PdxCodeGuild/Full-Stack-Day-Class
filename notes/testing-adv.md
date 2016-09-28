# Advanced Testing Concepts

Extensive testing is currently one of the major pillars of software quality.
With some good reason!
Writing tests allows you to catch regressions, confirm small parts are working, and induces better structured program code.

## Test Types

There are many different names folks have given to types of tests, depending on the size / scope of the behavior they assert.

[There is only _some_ agreement on what these types should be called.](http://stackoverflow.com/questions/4904096/whats-the-difference-between-unit-functional-acceptance-and-integration-test#4904533)
Unfortunately, some people call the same idea different names and some people call different ideas the same name...

I'm going to take names and approximate [definitions from Martin Fowler](http://martinfowler.com/articles/microservice-testing/#agenda).
He's a guy who's written a good amount on testing and service architecture.

* **Unit Tests** -- does a single function or class behavior work correctly?
* **Integration Test** -- do a group of units interact correctly to produce desired small-scale behaviors?
* **Component Test** -- does a well-defined and isolated component in the system work work like its interface says it should?
* **Contract Test** -- does the external programmatic interface of the system hold up its contract?
* **End-to-End Test** -- does the entire user-facing product satisfy its requirements?

As you go up this hierarchy, the tests are higher-level and require more coordinated components to work.
They also tend to run slower and require more testing fixtures or systems (e.g. test DB).

You also might hear many other testing terms:

* **Acceptance Test** -- like an end-to-end test; would the product be accepted by a client?
* **Selenium Test** -- also like an end-to-end test; [Selenium](http://docs.seleniumhq.org) is a browser automation toolkit, so you can make the browser click on things and see what the result is.

**Integration Test** is the most overloaded term.
Some people use it to refer to above, some people use it to refer to component tests, contract tests, or end-to-end tests.
Ask.

## Test Doubles

**Test doubles** are _fake_ implementations of values, models, units, or components with very simple implementations used to further isolate the **system under test**.

When you hear **mocks** or **stubs** (sometimes), those are two common words used for this idea.
There is also the concept of **spies**, which are fake objects that record how they were used.
Again, there are lots of redundant and overloaded terms.
I delegate to [Martin Fowler](http://martinfowler.com/bliki/TestDouble.html).

There are [Python](https://docs.python.org/3.5/library/unittest.mock.html) and [JavaScript](http://sinonjs.org) libraries (and too many JS ones) for implementing test doubles, but usually they are called mocks.
They also usually implement **patching**, or the temporary overriding of internal names for testing.
(Some people do this permanently, to extend internal types;
that's usually called **monkey patching**.)
(You can also read up on **dependency injection**, a way of avoiding having to do patching by being more functional. It's also necessary in more static languages.)

Let's say we want to test this Django view:

```py
def render_signup_ack(request):
    logic.create_account(request.POST['username'], request.POST['password'])
    return render(request, 'app/signup_ack.html', {'username': request.POST['username']})
```

In our separate testing module, we could write this test function that will not throw an exception on passing.

```py
from unittest.mock import MagicMock
from unittest.mock import patch

from . import view


@patch('logic.create_account')
@patch('view.render')
def test_render_signup_ack(mock_create_account, mock_render):
    mock_request = MagicMock()

    view_response = view.render_signup_ack(mock_request)

    mock_create_account.assert_called_once_with(
      mock_request.POST['username'], mock_request.POST['password'])
    mock_render.assert_called_once_with(mock_request, 'app/signup_ack.html', {'username': request.POST['username']})

    assert view_response == mock_render.return_value
```

There is a tradeoff for using mocks.
Too many and flexible mocks mean that tests won't catch integration errors.
I would say err on the side of making your real objects as easy to make and use as possible and compartmentalizing difficult to test code.
This is the origin of my suggestion to make most things "functional".

## Test-Driven Development

**Test-driven development** or **TDD** is a programming workflow where you:

1. Design, but do not code units
1. Write all tests for the contract of units
1. Write implementation code, constantly running all tests until they pass
1. Refactor code if necessary

Bugs are seen not as errors in logic code, but as forgotten tests.
This workflow focuses on writing _unit_ tests.

## Personal Token Skepticism

Unfortunately, some people treat testing or TDD in a dogmatic way.
Advice about testing can feel like a self-help book, and people can be overly rigid about it.

Widespread testing only really came into vogue in the 2000s, although the idea of [extreme programming](https://en.wikipedia.org/wiki/Extreme_programming) has been around since the 1990s.
People wrote a ton of fully functional and mostly-correct software before then.
People talk about testing today like indoor plumbing: absolutely necessary.
Is software today so significantly less buggy than then?
I'd argue no.
(Although there is a valid counter-argument that the problems have gotten much more complex and thus testing has been a necessary component.)

I think that testing is a tool to increase the _confidence_ you have in your code working correctly.
Confidence does not have the same definition as "correctness", and I think that's a good distinction.
It's a spectrum and you can decide if the tradeoffs are worth it.

I think TDD is useful in the small, but is a hinderance when designing larger systems.
Only writing tests doesn't give you a feel for how your own components interact with each other in a direct way.
That feeling is crucial to breaking apart your problem well.
So you might write all of these tests with a code structure in mind, then realize it sucks.
Then you have to refactor your tests _and_ your code!

I think there is also a lot to be said for designing your code and interfaces in a way that _prevent bugs before they happen_.
Have clear, separate types, clearly named functions, and define internal interfaces and APIs in a way that syntactically or logistically disallow you from making mistakes.

That said, I still love tests and write them.

* If writing a test is easy, the function is single-purpose and well designed.
* I do like the increase in confidence they give me.
* Tests give me a framework for easily running every function.
* I still try to think of ways to prevent bugs first.
