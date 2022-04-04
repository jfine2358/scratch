# LaTeX and Lwarp: specifying header cells in tables

## Introduction

This is a first step towards solving an accessible tables in LaTeX
problem.

Jason White wrote:

> Is there a generally accepted LaTeX convention for specifying which
  cells in a table are header cells (e.g., in tabular, tabularx,
  tabulary, etc., environments)?


He gives the reason for this request:

> The problem is that (at least with the Lwarp package), all of the
  cells, whether header or body, are transformed into HTML TD
  elements. Some browsers (I’ve tested with Chrome and Safari) then
  appear to treat the table as a layout table, and the table structure
  is not exposed to the screen reader at all. Hence I can’t navigate
  it as a table using a screen reader’s table navigation commands.

Jason's initial post is at https://tug.org/pipermail/accessibility/2022q2/000186.html.

## LaTeX input syntax

We have as input

```latex
\begin{center}
  \begin{tabular}{ c c c }
    \headrow{HEAD1 & HEAD2 & HEAD3}\\
    cell1 & cell2 & cell3 \\
    cell4 & cell5 & cell6 \\
    cell7 & cell8 & cell9
  \end{tabular}
\end{center}
```

## PDF output unchanged

For PDF output the following gives the usual output:
```latex
\newcommand\headrow[1]{#1}
```

## Roughly right HTML output

Some hacky macros provide approximately correct HTML output (lightly edited):
```html
<table>

<tr>
<td class="tdc">HEAD1<aaa/td>
<aaatd class="tdc">HEAD2<aaa/td>
<aaatd class="tdc">HEAD3</td>
</tr>

<tr>
<td class="tdc">cell1</td>
<td class="tdc">cell2</td>
<td class="tdc">cell3</td>
</tr>

<tr>
<td class="tdc">cell4</td>
<td class="tdc">cell5</td>
<td class="tdc">cell6</td>
</tr>

<tr>
<td class="tdc">cell7</td>
<td class="tdc">cell8</td>
<td class="tdc">cell9</td>
</tr>

</table>

```

## The hacky macros

Here's the hacky macros:
```latex
\let\Normal@LWR@htmltag\LWR@htmltag
\gdef\jfine@LWR@htmltag #1{\Normal@LWR@htmltag{aaa#1}}

\newcommand\headrow[1]{%
  \global\let\LWR@htmltag\jfine@LWR@htmltag
  #1%
  \global\let\LWR@htmltag\Normal@LWR@htmltag
}
```

You'll find the hacky macros at: https://github.com/jfine2358/scratch/blob/y2022p007/lwarp-jfine2358-headrow.sty

## To contribute

The process for checking this out is a little unusual,
```bash
$ git clone --branch y2022p007 git@github.com:jfine2358/scratch.git y2022p007
$ cd y2022p007/
$ lwarpmk print1
$ lwarpmk html1

```
