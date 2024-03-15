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
    "import sys; sys.path.append('/Users/jfeeney/code/personal/dotfiles/jupyter')",
    "import jf"
]
```