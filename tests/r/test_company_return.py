from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.company_return import company_return


def test_company_return():
  """Test module company_return.py by downloading
   company_return.csv and testing shape of
   extracted data has 142 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = company_return(test_path)
  try:
    assert x_train.shape == (142, 12)
  except:
    shutil.rmtree(test_path)
    raise()
