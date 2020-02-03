# Section 12 - Creating a complete User system

Throwing you off the deep end, for real

This challenge is going to be a little more involved than the previous ones 
and it will be modeled after a real life feature. 
Let's pretend that a client requested that users must confirm their e-mail address 
before being allowed to login and use your platform.

Your goal is to implement this. 
Expect this to take anywhere from 30 minutes to a few hours to implement depending on your current experience, 
and don't feel bad if it takes you all day or you end up giving up. The goal here is to learn, not take shortcuts.

Let me give you something to ponder before you get started:

We already have an active field in the user model and at first glance 
it might seem like a good idea to just have all new users default to being inactive as the first thing you do 
but I strongly recommend against this.

An account being confirmed and active are 2 completely different things. 
You're going to want different flash messages depending on if they are inactive and not confirmed. 
You also want to be able to distinguish unconfirmed and inactive users in the admin 
when we eventually get to that point.

Here's a few tips to get you started:

One approach would be to use the same token generation idea as the password reset 
to tie in confirmations to a specific user. I recommend this approach. 
I wanted to point that out because it might not be obvious and I didn't want you to get stuck.

When it comes to designing new features 
I often think things out on paper and answer questions like "how will this feature work?", 
"how many new templates or 'screens' will this feature involve making?", "what bits of the technology stack will 
I need to use to complete this feature?".

The main goal of this challenge isn't to implement user confirmations 
(which honestly is useful to know how to do because a lot of clients will request this in real life), 
but it's to get you in the habit of breaking down problems into smaller problems.

You might be sweating this assignment really hard because it sounds like a lot, 
but just chunk it out into smaller tasks and slowly crank through them. 
It's also totally ok to do a bit and take a break, 
then continue with the rest of the course and come back to this challenge.

* Register (user is not confirmed)
* Show message that User is not confirmed, check your email
* Add GET route to confirm registration
* Login only for confirmed user
* If not confirmed - resend confirmation code

# Section 14 - Logging, middleware and error handling

What would your application use?

Take a moment and think about other services your app might use in the real world. 
Would it use the Disqus comment system? Then go ahead and add in a config option and template for it.

# Section 15 - Quality of live CLI improvements

It's up to you

This challenge is up to you. What's a quality of life improvement that you'd like to see? If you thought of one, 
then go at it and implement it yourself.

Feel free to message me with your quality of life idea too, I'd be curious to see what you came up with.

e.g. create a blueprint skeleton

# Section 16 - Accepting recurring payments

A double header

This section was massive, so there's a lot to take in. Luckily most of the code is code that you won't have to fully 
absorb and memorize because most of it is code you could port around to different projects and slightly modify.

However, there's 2 things I'd like you to do.

The first challenge is easy, try adding a new subscription plan, and feel free to play around with 
the CSS so that 4 plans fit nicely.

The second challenge is implementing another real life feature that you'll likely want if you ever create 
an application that requires billing.

This is a big one but don't worry, I know you can do it. Remember what I said in a previous challenge 
about breaking things down into smaller problems? This is going to be one of those times haha.

I'd like you to modify the coupon system to allow for URL based coupons. Instead of having to tell someone 
to enter in XXX coupon code during payment, wouldn't it be nice if you could just send them a URL 
to click with the coupon already activated?

At a quick glance this is actually pretty easy to solve. Flask makes it easy to get query string parameters 
and you could just pass it into the template if it exists. I'm sure you would have thought of that on your own, 
but it's more complicated than that.

In a real production grade situation you would want to be able to send someone a link to sign up with 
a discount even if they didn't have a user account. Basically, you'll need to wire things up so that 
if you send someone a payment URL with a coupon code and they are not signed up, 
it will redirect them to sign up and after signing up it will redirect them to the payment form 
with the coupon code intact.

You'd also want it to work for users who already have an account but aren't signed in.

This will involve changing a few things, perhaps you'd even consider changing 1 or more decorators. 
You'll also need to use hidden fields in the user sign up / login forms to keep tabs on the discount code 
because otherwise it will get lost.

Good luck, and expect this feature to take a minimum of a few hours.
