from pathlib import Path
from pprint import pprint

import tabula
import pandas as pd


# TODO: consts file
RESOURCES = Path('../tests/resources')
ACCOUNTS = RESOURCES / 'accounts.pdf'
CONF_STATEMENT = RESOURCES / 'confirmation-statement.pdf'

acct_df = tabula.read_pdf(ACCOUNTS, pages='all')
conf_df = tabula.read_pdf(CONF_STATEMENT, pages='all')


pprint(acct_df.head())
pprint(conf_df.head())



