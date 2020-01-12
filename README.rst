autosheets
==========

autosheets is a Python package for applying changes across multiple Google Sheets.
It only supports updating sheets with the word "habit" in the title that contain a
"Daily" worksheet.

It can be deployed via AWS Lambda (TODO) or it can be executed locally.

Installing
----------

Start by installing `poetry`_.

Install the dependencies using `poetry`_:

.. code-block:: text

   $ poetry update

Setup your authorization using `pygsheets`_. You'll need to rename you credential file as `client_secrets.json`
until it is configurable.

You should also end up with a file like the following: `sheets.googleapis.com-python.json`.

.. _poetry: https://python-poetry.org/docs/

.. _pygsheets: https://pygsheets.readthedocs.io/en/stable/authorization.html


Executing
----------

Run the command locally. At this time it will update any sheet with the word "habit"
that contains a worksheet called "Daily" with a new column with today's date.

.. code-block:: text

   $ sls invoke local -f autosheets
