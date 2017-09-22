from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.help_rct import help_rct


def test_help_rct():
  """Test module help_rct.py by downloading
   help_rct.csv and testing shape of
   extracted data has 453 rows and 27 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = help_rct(test_path)
  try:
    assert x_train.shape == (453, 27)
  except:
    shutil.rmtree(test_path)
    raise()
