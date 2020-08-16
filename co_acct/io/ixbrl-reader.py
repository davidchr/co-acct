from pathlib import Path

from ixbrlparse import IXBRL

from cohoacct.constants import FIELDS
from cohoacct.company.company_accounts import CompanyAccounts

# TESTING PURPOSES
RESOURCES = Path('../../tests/resources')
fin1 = RESOURCES / 'fin1-xbrl.html'
fin2 = RESOURCES / 'fin2-xbrl.html'
fin3 = RESOURCES / 'fin3-xbrl.html'
fin4 = RESOURCES / 'fin4-xbrl.html'
micro_accounts = RESOURCES / 'micro-accounts-xbrl.html'


def read_ixbrl(filepath):
    """
    Convert an html file with ixbrl format to a CompanyAccount object.

    Paramters
    ---------
    filepath : str
    Path to the html file with ixbrl format

    Returns
    -------
    financial : CompanyAccounts
        An object with company accounts and basic details
    """

    with filepath.open() as file_object:
        x = IXBRL(file_object)

    # for i in x.numeric:
    #     print('---------------------------')
    #     print(i.__dict__['context'].__dict__)
    #     print(i.__dict__)
    #     print(i.__dict__['format'].__dict__)

    for i in x.nonnumeric:
        print('---------------------------')
        print(i.__dict__['context'].__dict__)
        print(i.__dict__)
        # print(i.__dict__['format'].__dict__)

    # return CompanyAccounts()


read_ixbrl(micro_accounts)
