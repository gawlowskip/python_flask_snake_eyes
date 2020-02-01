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
