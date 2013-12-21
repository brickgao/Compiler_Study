Homework for Compiler Construction
==============

这是编译原理的作业，是一个对 LISP 的部分实现，具体来说是不完全实现了 LISP 的七个基本运算符。

依赖
---

你可以从 [Python.org](http://python.org/) 来获取 Python27

通过`pip`命令来获取`PLY`模块

```bash
pip install ply
```

使用方法
---

运行 `src\main.py`

语法
--------

quote 和 ' 是语法糖，基本形式为`(quote x)`和`'x`，具体来说就是返回本身：

```bash
LISP > 'a
['a']
LISP > (quote a)
['a']
```

atom 的基本形式是`(atom x)`，`x`为列表，在列表非原子的情况下返回空表 `[]`，在原子的情况下返回 `t`：

```bash
LISP > (atom 'a)
['t']
LISP > (atom '(a b c))
[]
```

eq 的基本形式是`(eq x y)`，`x`和`y`均为列表，当x y相同的时候返回`t`，否则返回`[]`：

```bash
LISP > (eq 'a 'a)
['t']
LISP > (eq 'a '(a b))
[]
```

car的基本形式是`(car x)`，`x`为列表，返回`x`中的第一个元素：

```bash
LISP > (car '(a b c))
['a']
```

cdr的基本形式是`(cdr x)`，`x`为列表，返回`x`中的除第一个元素以外的元素：

```bash
LISP > (cdr '(a b c))
['b', 'c']
```

cons的基本形式是`(cons x y)`，`x`和`y`均为列表，返回`x`和`y`的结合（这里与 LISP 不同）：

```bash
LISP > (cons '(a b c) '(d e))
['a', 'b', 'c', 'd', 'e']
```

cons的基本形式是`(cond (p1 e1) ...(pn en))`，`p1`为表达式，`e1`为列表，返回第一个`pi`中存在`t`的`ei`：

```bash
LISP > (cond ((eq 'a 'b) '(a b)) ((atom 'a) '(c d)))
['c', 'd']
```

License
-------

[WTFPL](http://www.wtfpl.net/)

