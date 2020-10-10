# unZip-Utility

An unzip utility written in python

## Getting Started

1. Install `tqdm` `loguru` `black` from `pip`

   ```bash
   pip install tqdm loguru black
   ```

   1. If you have trouble with this, try
      ```bash
      python -m pip install tqdm loguru black
      ```

2. Pick issues from the [issue explorer](https://github.com/StevensCTC/unZip-Utility/issues) that you want to work on. Comment on one and wait for it to be assigned to you to avoid code duplication
3. Resolve the issue (likely implement features, or bugfixes)
   1. Use [logger](https://github.com/Delgan/loguru): `logger.info`, `logger.debug`, `logger.error`,`logger.critical`, and `logger.success` in place of `print`
   2. Use [tqdm](https://github.com/tqdm/tqdm#tqdm) to create clean progress bars
4. Format your code: run `black main.py --line-length 80`
5. Pull Request!
