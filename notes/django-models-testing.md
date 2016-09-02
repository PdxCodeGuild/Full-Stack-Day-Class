# Testing with Models

You can use [doctests](/notes/py-doctests.md) to test logic and models.
If you followed the [Django setup instructions](/notes/django-init.md#5-connect-doctests), doctests will be able to handle the DB.

Effectively, each docstring runs in its own empty DB.
So you can make models, save them, and they should be retrieved later.
Any other function's doctests should not see those saved models.

```py
from . import models


def count_employees(business):
    """Return the number of employees currently working at a business.

    >>> b = models.Business(name='PDX Code Guild', founded=2013)
    >>> b.save()
    >>> e1 = models.Employee(works_at=b, name='David', email='david@pdxcodeguild.com')
    >>> e1.save()
    >>> count_employees(b)
    1
    """
    return len(business.employees)


# Notice the following docstring won't see "David" from above.
def get_employee_emails(business):
    """Return a list of employee emails.

    >>> b = models.Business(name='PDX Code Guild', founded=2013)
    >>> b.save()
    >>> e1 = models.Employee(works_at=b, name='Helen', email='helen@pdxcodeguild.com')
    >>> e1.save()
    >>> get_employee_emails(b)
    ['helen@pdxcodeguild.com']
    """
    return [employee.email for employee in business.employees]
```
