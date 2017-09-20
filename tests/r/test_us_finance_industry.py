from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_finance_industry import us_finance_industry


def test_us_finance_industry():
  """Test module us_finance_industry.py by downloading
   us_finance_industry.csv and testing shape of
   extracted data has 84 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_finance_industry(test_path)
  try:
    assert x_train.shape == (84, 7)
  except:
    shutil.rmtree(test_path)
    raise()
