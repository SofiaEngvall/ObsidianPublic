
The square brackets [ and ] are used in shell scripts to perform test commands (also known as conditional expressions). Here's how they work:
General Syntax:

`[ condition ]`

A space is required after `[` and before `]`.
The `[` command is actually an alias for the test command.
It evaluates the given condition and returns 0 (success) if true, or non-zero (failure) if false.

Common Uses of `[` and `]`:

String Comparison:
`[ -n "$var" ]`: True if $var is not empty.
`[ -z "$var" ]`: True if $var is empty.
`[ "$str1" = "$str2" ]`: True if str1 equals str2.
`[ "$str1" != "$str2" ]`: True if str1 does not equal str2.

Numeric Comparison:
`[ $num1 -eq $num2 ]`: True if num1 equals num2.
`[ $num1 -lt $num2 ]`: True if num1 is less than num2.
`[ $num1 -gt $num2 ]`: True if num1 is greater than num2.

    File Tests:
        [ -f "$file" ]: True if $file is a regular file.
        [ -d "$dir" ]: True if $dir is a directory.
        [ -r "$file" ]: True if $file is readable.
        [ -w "$file" ]: True if $file is writable.
        [ -x "$file" ]: True if $file is executable.

    Logical Operators:
        [ condition1 ] && [ condition2 ]: Logical AND (both must be true).
        [ condition1 ] || [ condition2 ]: Logical OR (one must be true).
        ! [ condition ]: Logical NOT (negates the condition).

Example:

if [ -n "$result" ]; then
    echo "Variable is not empty"
else
    echo "Variable is empty"
fi

Advanced:

Double brackets [[ ... ]] are more flexible and recommended in newer shells (e.g., Bash). They allow regex and logical operators without escaping.
