When creating open-source Python 3 scripts, it's important to follow coding standards and documentation conventions to make your code more readable and maintainable for both yourself and potential contributors. Below are some common practices for commenting and documenting Python scripts:

1. **Header Comments:**

   At the top of your script, include a header comment that provides essential information about the script. This typically includes:

 - `#!/usr/bin/env python3`: This shebang line specifies the path to the Python 3 interpreter.
 - `# -*- coding: utf-8 -*-`: This line specifies the character encoding for the script.

2. **Module-level Docstring:**

   Immediately after the header comments, include a module-level docstring enclosed in triple quotes (`"""`). This docstring provides an overview of the module and its purpose.

3. **Function and Class Documentation:**

   For each function and class in your script, include docstrings that explain their purpose, input parameters, and return values. Here's an example for a function:

   - Use the `:param` and `:return` tags to document function parameters and return values.
   - Provide clear and concise descriptions.

4. **Comments within Code:**

   Use inline comments sparingly to explain complex or non-obvious code. Make sure your code is self-explanatory whenever possible, but when it isn't, comments can provide clarity.

5. **Consistent Style:**

   Follow a consistent coding style guide such as PEP 8 (Python Enhancement Proposal 8) for naming conventions, indentation, and other code style aspects.

6. **Version Control Information:**

   If you're hosting your code on a version control system like Git, consider including a comment with the repository URL and a brief description of how to contribute.

7. **License Information:**

   Include licensing information in your script. You can add a comment at the top, specifying the license (e.g., MIT, Apache 2.0) you're releasing the code under.

Here's an example of a well-documented Python script:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a sample Python script for demonstration purposes.

It performs a simple task using functions and classes.

Author: Your Name
License: MIT
Repository: https://github.com/yourusername/your-repo

Usage:
    python script.py
"""

# Import statements

def my_function(param1, param2):
    """
    This function performs a specific task.

    :param param1: Description of param1.
    :param param2: Description of param2.
    :return: Description of the return value.
    """
    # Function code goes here

class MyClass:
    """
    This is a sample class.

    It does something useful.
    """

    def __init__(self):
        # Constructor code

    def my_method(self):
        """
        This method does something.

        :return: Description of the return value.
        """
        # Method code goes here

if __name__ == "__main__":
    # Main script logic
```

Remember that good documentation and clean code are essential for open-source projects, as they encourage collaboration and make it easier for others to understand and contribute to your code.