from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.schutz import schutz


def test_schutz():
  """Test module schutz.py by downloading
   schutz.csv and testing shape of
   extracted data has 9 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = schutz(test_path)
  try:
    assert x_train.shape == (9, 9)
  except:
    shutil.rmtree(test_path)
    raise()
