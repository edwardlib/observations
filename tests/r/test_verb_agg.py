from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.verb_agg import verb_agg


def test_verb_agg():
  """Test module verb_agg.py by downloading
   verb_agg.csv and testing shape of
   extracted data has 7584 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = verb_agg(test_path)
  try:
    assert x_train.shape == (7584, 9)
  except:
    shutil.rmtree(test_path)
    raise()
