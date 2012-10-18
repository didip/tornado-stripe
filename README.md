tornado-stripe
=============

Asynchronous or synchronous [Stripe](https://stripe.com/docs/api) client for the [Tornado Web Server](http://tornadoweb.org/).

It's a complete implementation of Stripe v1 API using Tornado AsyncHTTPClient.

tornado-stripe is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).


Requirement
-----------

`tornado>=2.4`


Installation
------------

To install from source:

    python setup.py build
    sudo python setup.py install

tornado-stripe has been tested on Python 2.6 and 2.7.

You may also install it using pip or easy_install with:

    pip install tornado-stripe

or

    easy_install install tornado-stripe


Quick Usage
-----------

```python
from tornado_stripe import Stripe

# blocking client
stripe = Stripe('api_key', blocking=True)

DUMMY_PLAN = {
    'amount': 2000,
    'interval': 'month',
    'name': 'Amazing Gold Plan',
    'currency': 'usd',
    'id': 'stripe-test-gold'
}

# Creating Stripe plan
stripe.plans.post(**DUMMY_PLAN)

# Fetching Stripe plan
plan = stripe.plans.id(DUMMY_PLAN['id']).get()
```


URL Builder
-----------

`tornado_stripe.Stripe` maps to Stripe Curl URL exactly one-to-one.

```python
from tornado_stripe import Stripe
stripe = Stripe('api_key', blocking=True)

stripe.charges                                  # == /v1/charges
stripe.charges.id(CHARGE_ID)                    # == /v1/charges/{CHARGE_ID}
stripe.customers                                # == /v1/customers
stripe.customers.id(CUSTOMER_ID)                # == /v1/customers/{CUSTOMER_ID}
stripe.customers.id(CUSTOMER_ID).subscription   # == /v1/customers/{CUSTOMER_ID}/subscription
stripe.invoices                                 # == /v1/invoices
stripe.invoices.id(INVOICE_ID)                  # == /v1/invoices/{INVOICE_ID}
stripe.invoiceitems                             # == /v1/invoiceitems
stripe.invoiceitems.id(INVOICEITEM_ID)          # == /v1/invoiceitems/{INVOICEITEM_ID}
stripe.tokens                                   # == /v1/tokens
stripe.tokens.id(TOKEN_ID)                      # == /v1/tokens/{TOKEN_ID}
stripe.events                                   # == /v1/events
stripe.events.id(EVENT_ID)                      # == /v1/events/{EVENT_ID}
```


Performing HTTP requests
------------------------

```python
stripe = tornado_stripe.Stripe('api_key')

# GET
stripe.plans.get()
stripe.plans.id(PLAN_ID).get()

# POST
DUMMY_PLAN = {
    'amount': 2000,
    'interval': 'month',
    'name': 'Amazing Gold Plan',
    'currency': 'usd',
    'id': 'stripe-test-gold'
}
stripe.plans.post(**DUMMY_PLAN)

# DELETE
stripe.plans.id(DUMMY_PLAN['id']).delete()
```


Running Tests
-------------

You must set `STRIPE_API_KEY` environment variable. Example:

    export STRIPE_API_KEY=your-stripe-api-key; nosetests

