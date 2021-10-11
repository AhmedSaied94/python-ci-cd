#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
import html


print("Content-type: text/html")

print("""
<html>
    <head>
        <title> Hello python </title>
    </head>
    <body style="text-align: center;">
    <h1 style="color: red;"> Welcome to python cgi script test </h1>
""")
form = cgi.FieldStorage()
message = form.getvalue("message", "(Enter your message)")

print("""
        <p>Previous message: %s</p>
        <p> Form </p>
        <form method="post" action="index.cgi">
            <p>message: <input type="text" name="message"/></p>
        </form>
    </body>
</html>
""" % html.escape(message))
