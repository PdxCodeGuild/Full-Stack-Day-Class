# Secrets and Environment Variables

**Never check in secrets to public source control.**
Anything surrounding authentication or security should be kept more secret.

* Usernames
* Passwords
* Keys
* Tokens
* Seeds

For example:

* AWS keys
* Google Maps API key
* SSH Key
* DB Password
* Random number generator seed
* Twitter OAuth token

If someone malicious has access to these facts, they can pretty easily delete or steal data from your application.

For most dinky services no one will care if the keys are public, but if you check in AWS keys and push them to GitHub there are bots that scrape for them and can rake up a $2K bill for you overnight.

## Mitigation Tactic

A first pass on how to mitigate this is to store secrets in **environment variables**.
They are variables that the operating system allows running programs to read.
They are used to communicate configuration facts to a running program; they sort of overlap in role with command line arguments.
They live in a dictionary in `os.environ`.
They tend to be in `CONSTANT_CASE` even though they're called "variables", but they are usually constant for the life of a single program.

If I have an `envtest.py`:

```py
import os
print('Hi, {}!'.format(os.environ['NAME']))
```

And run it with:

```bash
$ NAME=David python envtest.py
Hi, David!
```

We see that it found that variable in the environment and could access it.

So, to hold secrets in them and use them in code:

1. Create a file that will contain all the secret environment variables `.env-dev`
1. Git ignore `.env*` (we'll be using other `.env` files later)
1. Fill `.env-dev` with `ENV_VAR_NAME=value` lines for each secret
1. Have your code `import os` and use the `os.environ` dictionary to reach in and grab the secrets
1. Load the environment variables you have saved in `.env-dev` whenever you run your Python code: `env $(xargs < .env-dev) python SCRIPT.py`
