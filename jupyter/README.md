# README: Jupyter

Use the following steps to use these functions in your ipython / jupyter sessions

## iPython Kernel (usually with Jupyter using a local kernel)
Create a default config for ipython

```bash
ipython profile create  
```

Add this line to ipython config

```python
c.InteractiveShellApp.exec_lines = [
    # Personal Imports
    "import sys; sys.path.append('/Users/jfeeney/code/personal/dotfiles/jupyter')",
    "import jf",
    "import snap",
    "from snap import GoogleProductCategoryTaxonomy"
    # Standard Imports
    "import pandas as pd",
    "import numpy as np",
    "import matplotlib.pyplot as plt",
    "import datetime"
]
```