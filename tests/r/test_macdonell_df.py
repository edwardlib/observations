from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.macdonell_df import macdonell_df


def test_macdonell_df():
  """Test module macdonell_df.py by downloading
   macdonell_df.csv and testing shape of
   extracted data has 3000 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = macdonell_df(test_path)
  try:
    assert x_train.shape == (3000, 2)
  except:
    shutil.rmtree(test_path)
    raise()
