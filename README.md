## MindsDB Integration Cookiecutter
Use this cookiecutter template to create integrations into <a href="https://github.com/mindsdb/mindsdb">MindsDB</a>. This template is designed for _Handler Integrations_.

### Usage
Make sure you have `cookiecutter` installed on your machine via running the following commands.

```sh
$ pip install -U cookiecutter
...
$ cookiecutter -V
```

Make sure you already have `mindsdb/mindsdb` cloned locally. We assume that it's located on `~/mindsdb` for now.

To create your handler, run the following command and keep answering the questions.

```sh
cookiecutter gh:lnxpy/cookiecutter-mindsdb -o ~/mindsdb/mindsdb/integrations/handlers/
```

### Versioning
If you've decided to use `bump2version` for managing your handler version, simply navigate to your handler directory and bump up/down your handler version via:

```sh
bumpversion patch/minor/major
```

Then you'll see that it's updated your handler's version!

### Implementation
All the files you need to update are listed as follows.

- `README.md`
- `requirments.txt` (if you already have it)
- `icon.svg`
- `<HANDLER>_handler.py`
- `<HANDLER>_tables.py`

Once you're satisfied with your changes, you can open a merge request for your changes to be reviewed.
