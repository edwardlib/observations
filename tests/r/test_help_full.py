from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.help_full import help_full


def test_help_full():
  """Test module help_full.py by downloading
   help_full.csv and testing shape of
   extracted data has 1472 rows and 788 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = help_full(test_path)
  try:
    assert x_train.shape == (1472, 788)
  except:
    shutil.rmtree(test_path)
    raise()
