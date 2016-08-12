# Keeping Secrets

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

A first pass on how to mitigate this is:

1. Store only secrets in a special file
1. Git ignore that file
1. Somehow "import" the values in that file from checked in source
