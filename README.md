<img src="https://i.imgur.com/inrKMue.png" alt="Floodgates" width="600"/>

[![version-1 0](https://user-images.githubusercontent.com/101282618/157538866-bfbcf791-8c26-4cdf-891f-c5c9dee8ac79.svg)](https://github.com/simbyte404/floodgates-bomber)
[![made-with-python](https://user-images.githubusercontent.com/101282618/157539597-50b15d78-a173-48c5-84a4-f21e256e9c31.svg)](https://www.python.org)

Floodgates is an email flooding script made in Python 3.10. With its intelligent design, ease-of-use, and compatibility with most well-known and used email providers, it's quick an easy to pick up and utilize for your projects!

## What's an email flooder?

An email flooder, also known as an email bomber or spammer, is a piece of software which can send multiple emails at once to a recipient within a short amount of time. They're commonly used to stress test email servers and domains, or to test spam filter strengths on personal accounts.

## Getting started

Floodgates was designed with the object of being quick and easy to use for anyone of any technical level. Setting up and using is done in just three easy steps!

1. Download the `Floodgates.py` file from this repository. No need for any external libraries, files, or installations -- all you need is a Python 3.5+ installation, and you're good to go!
2. Run the script and follow the steps provided. There are a few sections to run through, but it takes less than a minute to go through them all.
3. Sit back and wait for it to send your messages! It might take a while depending on the number of messages and the delay in between sends you asked for, but all there is to do is let it run!

## Issues and limitations

Naturally, there are a few problems to using Floodgates, as with all programs and projects. Below is a list of the current known issues and limitations as we've documented them.

### Current issues

- [#1 - AOL SMTP connection gets refused](/../../issues/1)
    - Currently, we believe is due to a lack of documentation on what port AOL's SMTP accepts, and what security protocol they accept. We'll keep troubleshooting this.

### Current limitations

- Problems with slow network connections
    - Due to the way the `smtplib` Python library works, slower network connections might not adequately handle the connections needed without timing out. This can cause messages to either stop sending mid-way, or the connection to fail before getting to that point.

## Contributions

Think you can help us improve Floodgates? Let us know! 
