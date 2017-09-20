from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.political_knowledge import political_knowledge


def test_political_knowledge():
  """Test module political_knowledge.py by downloading
   political_knowledge.csv and testing shape of
   extracted data has 4 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = political_knowledge(test_path)
  try:
    assert x_train.shape == (4, 12)
  except:
    shutil.rmtree(test_path)
    raise()
