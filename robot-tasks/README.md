# Robot tasks
This folder contains my codes for automatically generated tasks by the
[kispython robot][robot]. My tasks can be found down below.

## Tasks 1-5
Each of the first five tasks are to implement a mathematical function.
They are pretty easy, but there are some things to remember:

There are floor and ceiling operations in these functions, which may be
new to you. They look like this: ⌊x⌋ - floor, ⌈x⌉ - ceiling.
In Python, they are `math.floor()` and `math.ceil()`.

In the fifth task, the function operates vectors (lists),
and their lengths. In the mathematical notation the indexes start at 1.
In the program, obviously, they start from 0, so you'll have to make
some small adjustments to avoid IndexError exceptions.

Keep in mind you have to follow PEP-8, so keep two lines
between functions, have a newline at end of program,
make sure no lines are longer than 80 characters,
split formulas to several lines if needed.

Links to the tasks: [T1][t01], [T2][t02], [T3][t03], [T4][t04], [T5][t05].

The functions themselves were listed here previously, but they took too much space,
didn't show correctly on dark theme and were of little interest anyway.
You can view this README raw and find the functions as comments below this paragraph if you're curious.
They are in LaTeX format and passed in link to [Codecogs][codecogs].

<!--
**Note:** the formulas may take a short time to render, you might have to refresh the page.
Unfortunately, they don't work well on dark theme, but you can open them in separate tabs and they'll look fine.

<img style="padding:8px; border-radius:8px; background:white" src="https://latex.codecogs.com/svg.image?f(z)&space;=&space;\frac{z^{2}}{45}&space;-&space;70&space;&space;\left(z^{2}&space;-&space;62&space;&space;z^{3}&space;-&space;58\right)^{3}&space;&plus;&space;\frac{41&space;&space;\left\lfloor&space;z&space;\right\rfloor&space;-&space;53&space;&space;\left(74&space;&space;z^{2}&space;-&space;z\right)^{7}}{z^{5}}" title="f(z) = \frac{z^{2}}{45} - 70 \left(z^{2} - 62 z^{3} - 58\right)^{3} + \frac{41 \left\lfloor z \right\rfloor - 53 \left(74 z^{2} - z\right)^{7}}{z^{5}}" />
<img style="padding:8px; border-radius:8px; background:white" src="https://latex.codecogs.com/svg.image?f(x)&space;=&space;\begin{cases}46&space;&space;x^{4}&space;&plus;&space;1,&&space;x&space;<&space;-3\\72&space;&space;x&space;-&space;\left(14&space;&space;x&space;-&space;7\right),&&space;-3&space;\leq&space;x&space;<&space;12\\\left(x^{3}&space;-&space;82&space;&space;x&space;-&space;x^{2}\right)^{6}&space;&plus;&space;81&space;&space;x&space;&plus;&space;77&space;&space;\left(87&space;&space;x^{2}\right)^{7},&&space;12&space;\leq&space;x&space;<&space;36\\\left(66&space;&space;x&space;&plus;&space;x^{3}\right)^{5}&space;&plus;&space;8&space;&space;\,\mathrm{sin}^{4}&space;x,&&space;x&space;\geq&space;36\end{cases}" title="f(x) = \begin{cases}46 x^{4} + 1,& x < -3\\72 x - \left(14 x - 7\right),& -3 \leq x < 12\\\left(x^{3} - 82 x - x^{2}\right)^{6} + 81 x + 77 \left(87 x^{2}\right)^{7},& 12 \leq x < 36\\\left(66 x + x^{3}\right)^{5} + 8 \,\mathrm{sin}^{4} x,& x \geq 36\end{cases}" />
<img style="padding:8px; border-radius:8px; background:white" src="https://latex.codecogs.com/svg.image?f(b,&space;m,&space;n,&space;p)&space;=&space;\sum_{c=1}^{b}\left(82&space;&space;c&space;-&space;\left(\left\lfloor&space;c&space;\right\rfloor\right)^{4}&space;-&space;\left(31&space;&space;c&space;&plus;&space;47&space;&space;c^{2}&space;&plus;&space;c^{3}\right)^{5}\right)&space;&plus;&space;\sum_{j=1}^{n}\prod_{c=1}^{b}\sum_{k=1}^{m}\left(79&space;&space;j^{3}&space;&plus;&space;50&space;&space;k^{5}&space;&plus;&space;\left(\frac{c}{90}&space;-&space;1&space;-&space;p^{3}\right)^{7}\right)" title="f(b, m, n, p) = \sum_{c=1}^{b}\left(82 c - \left(\left\lfloor c \right\rfloor\right)^{4} - \left(31 c + 47 c^{2} + c^{3}\right)^{5}\right) + \sum_{j=1}^{n}\prod_{c=1}^{b}\sum_{k=1}^{m}\left(79 j^{3} + 50 k^{5} + \left(\frac{c}{90} - 1 - p^{3}\right)^{7}\right)" />
<img style="padding:8px; border-radius:8px; background:white" src="https://latex.codecogs.com/svg.image?f_n&space;=\begin{cases}0.28,&space;&&space;n&space;=&space;0;\\\frac{f_{n&space;-&space;1}^{2}}{32}&space;&plus;&space;0.04&space;&plus;&space;f_{n&space;-&space;1},&space;&&space;n&space;\geq&space;1.\end{cases}" title="f_n =\begin{cases}0.28, & n = 0;\\\frac{f_{n - 1}^{2}}{32} + 0.04 + f_{n - 1}, & n \geq 1.\end{cases}" />
<img style="padding:8px; border-radius:8px; background:white" src="https://latex.codecogs.com/svg.image?f(\vec{z})&space;=&space;\sum_{i=1}^{n}\frac{z_{n&space;&plus;&space;1&space;-&space;\left\lceil&space;i&space;/&space;2&space;\right\rceil}^{4}}{67}" title="f(\vec{z}) = \sum_{i=1}^{n}\frac{z_{n + 1 - \left\lceil i / 2 \right\rceil}^{4}}{67}" />
-->

## Task 6
The task is to implement a solution tree function.
Sounds easy, but you need to avoid cyclomatic complexity.
That means the less if-else branches - the better.
Remove the last else statements and just leave the returns.
If there are multiples of the same choice - make it a function.
You can look at my example of code [here][t06].

## Task 7
Now we're onto something interesting. The task is to implement a function for bit field transformation.
Or to put it simply, reordering certain sections of bits in an integer. Sort of an illustration:
```
EE.DD.CCCCCCCCCC.BBBBBBBBBBBBBBBB.AA  # Input
AA.EE.ССССCCCCCC.DD.BBBBBBBBBBBBBBBB  # Output

Examples:
f(0xb163e58f) = 0xe163f963
f(0x29daf9f4) = 0x09dabe7d
```

The way to solve this is:
1. Calculate masks for each section by subtracting powers of two.
2. Isolate the sections with bitwise AND (`&`) and the masks.
3. Shift the sections to their new positions with `<<` / `>>`.
4. Merge the sections together with bitwise OR (`|`).

You can calculate the masks manually - or be a little smarter and write a function for that.
Here's a neat one I wrote - it takes the positions of section borders and returns the masks in hex:
```python
def convert():
    s = [0, 2, 18, 28, 30, 32]   # numbers to the left of each border
    for i in range(len(s) - 1):  # f-string expressions are cool
        print(f"{chr(ord('A') + i)}: 0x{(2 ** s[i + 1] - 2 ** s[i]):08x}")
```

Thanks to that function we now have the masks. All we need now is to use them as shown below. Code [here][t07] btw.
```python
def main(num):
    a = num & 0x00000003  # (2 ** 2  - 2 ** 0)
    b = num & 0x0003fffc  # (2 ** 18 - 2 ** 2)
    c = num & 0x0ffc0000  # (2 ** 28 - 2 ** 18)
    d = num & 0x30000000  # (2 ** 30 - 2 ** 28)
    e = num & 0xc0000000  # (2 ** 32 - 2 ** 30)
    return (a << 30) | (b >> 2) | c | (d >> 12) | (e >> 2)
```

## Task 8
This task is to implement a function for parsing a string with data of a weird format.
The result has to be returned as a dictionary. Example of data format down below (my variant):
```
Input:
<block> <data> declare #1474|> `edce. </data>.<data>declare#-4186
|>`riquer.</data>. <data> declare#3755 |> `diquon_733.</data>.
<data>declare#-4726 |> `bela. </data>. </block>

Output:
{'edce': 1474, 'riquer': -4186, 'diquon_733': 3755, 'bela': -4726}
```

The way to solve this task is by using regular expressions (module `re`).
All we need to do is to parse the data into a list with `re.findall()` and put it into a dictionary.
The difficult part is to actually find a regular expression that works. Regex is not easy - you'll see why.
In this example we have a pattern like: ```#value |> `key.```. We need a regular expression that would
find such patterns - you can find it in the [code][t08] or right below.
```python
def main(s):
    pattern = r"#(.*?) *\|> *`(.*?)\.+"                  # black magic sorcery (regex)
    parsed_s = re.findall(pattern, s.replace('\n', ''))  # parse data into tuple list
    return {key: int(value) for value, key in parsed_s}  # put data into dictionary
```

## Task 9
Implement a Mealy machine as a class.
The starting state is given. Methods return integer values.
If a called method is not implemented for a given state, raise `KeyError`.

This task is very easy: all you need to do is make a class called `main`
(for the robot to parse it properly) with a `state` field.
Add the methods with the names given in the graph.
For every state transition that uses this method,
create an `if` statement that checks the state,
does the transition and returns the integer from graph.
After all the `if` statements, raise the `KeyError` exception.
You can find the code [here][t09].

## Task 10
Implement a function for transforming table data.
Input and output tables are given in row form with lists.
Filled cells have string data, empty ones have `None`.

Do the following transformations:
1. Delete duplicate rows.
2. Delete duplicate columns.
3. Delete empty rows.
4. Transform the data as in examples below.
5. Transpose the table.

### Transform example:

Input table:
| Column 1 | Column 2 | Column 3 | Column 4   |
| -------- | -------- | -------- | ---------- |
| 0.7858   | 0        | 0.7858   | 24-03-2004 |
| 0.0793   | 1        | 0.0793   | 25-11-1999 |
|          |          |          |            |
| 0.5257   | 1        | 0.5257   | 16-04-2004 |
|          |          |          |            |
| 0.5257   | 1        | 0.5257   | 16-04-2004 |
| 0.5257   | 1        | 0.5257   | 16-04-2004 |

Output table:
| Column 1     | Column 2  | Column 3  |
| ------------ | --------- | --------- |
| 79%          | 8%        | 53%       |
| Не выполнено | Выполнено | Выполнено |
| 04.03.24     | 99.11.25  | 04.04.16  |

Rather than deleting duplicate rows/columns, we can just ignore them.
The first and third columns are duplicate so we'll only parse the first.
As for the rows, we can have a `set` where we will add first column values.
The empty rows can be ignored by adding an `is None` check.

To actually transform the data and have the output transposed,
we'll have a list for all three data types (rows).
To format a float to a percentage we can use f-strings: `f'{num:.0%}'`.
To format the date we can use string slices.
As we've parsed all the data, return a list of the rows.
Here's the [code][t10].

## Task 11
Implement parsing of binary data format.
There's a start signature, after which structure A is encoded.
The byte order is from lesser to greater (little-endian).
Addresses are given as offsets from data start.
Using `struct` module is advised.
There are several structures consisting of different data types
and links to other structures.

Parsing all the different types by hand would be a pain.
To aid with that, we can use the function `unpack` from module `struct`,
which is made exactly for parsing mixed data types from byte sequences.
You can read some useful documentation on it [here][struct].
Basically, we can use format strings to define types to parse.
For example, `unpack('hIq', sequence)` will parse a tuple with:
`short` (int16), `unsigned int` (uint32), `long long` (int64).
You can also specify byte order with `<` (little-endian) or
`>` (big-endian) in the beginning of the format string.

Using slices and parsed addresses should let you parse the structures
and arrays. Keep in mind the `unpack` function returns tuples.
To parse strings (`char` arrays), you can use `str(foo[0], 'utf8')`,
where foo is the tuple with a binary string of parsed bytes.
Dictionary comprehensions will also be very useful for parsing structures.
Anyways, you can check the code [here][t11].

[t01]: rt-task01.py
[t02]: rt-task02.py
[t03]: rt-task03.py
[t04]: rt-task04.py
[t05]: rt-task05.py
[t06]: rt-task06.py
[t07]: rt-task07.py
[t08]: rt-task08.py
[t09]: rt-task09.py
[t10]: rt-task10.py
[t11]: rt-task11.py

[robot]: http://kispython.ru
[struct]: https://docs.python.org/3/library/struct.html
[codecogs]: https://latex.codecogs.com