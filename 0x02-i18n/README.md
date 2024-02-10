## Issue with Babel and Jinja2 Extensions

If you encounter an AttributeError related to Jinja2 extensions when using Babel's `pybabel extract` command, such as:

```
oualid@OUALID:~/Desktop/ALX/alx  projects/alx-backend/0x02-i18n$ pybabel extract -F babel.cfg -o messages.pot .
extracting messages from 0-app.py
extracting messages from 1-app.py
extracting messages from 2-app.py
extracting messages from 3-app.py
extracting messages from templates/0-index.html (extensions="jinja2.ext.autoescape,jinja2.ext.with_")
Traceback (most recent call last):
  File "/home/oualid/.local/bin/pybabel", line 8, in <module>
    sys.exit(main())
  File "/home/oualid/.local/lib/python3.10/site-packages/babel/messages/frontend.py", line 979, in main
    return CommandLineInterface().run(sys.argv)
  File "/home/oualid/.local/lib/python3.10/site-packages/babel/messages/frontend.py", line 905, in run
    return cmdinst.run()
  File "/home/oualid/.local/lib/python3.10/site-packages/babel/messages/frontend.py", line 516, in run
    for filename, lineno, message, comments, context in extracted:
  File "/home/oualid/.local/lib/python3.10/site-packages/babel/messages/extract.py", line 215, in extract_from_dir
    yield from check_and_call_extract_file(
  File "/home/oualid/.local/lib/python3.10/site-packages/babel/messages/extract.py", line 279, in check_and_call_extract_file
    for message_tuple in extract_from_file(
  File "/home/oualid/.local/lib/python3.10/site-packages/babel/messages/extract.py", line 321, in extract_from_file
    return list(extract(method, fileobj, keywords, comment_tags,
  File "/home/oualid/.local/lib/python3.10/site-packages/babel/messages/extract.py", line 450, in extract
    for lineno, funcname, messages, comments in results:
  File "/home/oualid/.local/lib/python3.10/site-packages/jinja2/ext.py", line 808, in babel_extract
    extensions[import_string(extension_name)] = None
  File "/home/oualid/.local/lib/python3.10/site-packages/jinja2/utils.py", line 149, in import_string
    return getattr(__import__(module, None, None, [obj]), obj)
AttributeError: module 'jinja2.ext' has no attribute 'autoescape'
```

The issue might be due to a compatibility problem between the versions of Jinja2 and Babel. To resolve this, you can downgrade Jinja2 to a version that is known to be compatible with Babel. You can do this by running:

```bash
pip install Jinja2==3.0.3
```

After downgrading Jinja2, try running the `pybabel extract` command again, and the issue should be resolved. This solution ensures compatibility between Jinja2 and Babel extensions, allowing for smooth extraction of messages.
