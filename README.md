Journal Abbrevs
===============

_Trivial journal abbreviation management for BibTeX_

Copyright Mikhail Wolfson 2010-2011.

Summary
-------

Since BibTeX doesn't have a good mechanism for maintaining journal abbreviations,
the following is my attempt at a zero-order abbreviation maintenance system. It
still requires personal curation, (let's be honest, what BibTeX system
doesn't?), but IMHO, it makes the job easier.

### The problem
Different journals and books require journal names in references to follow
different conventions. Of these, there are generally three classes:

1. Full: _The Journal of Physical Chemistry_
2. Abbreviated, with periods: _J. Phys. Chem._
3. Abbreviated, without periods: _J Phys Chem_

Conversion between 2. and 3. is trivial: simply remove the periods from 2. to
get 3. But conversion between 1. and 2. is decidedly not: because of the large
number of exceptions in abbreviations, the only way to do this right is to
maintain some database that contains a single entry for the journal and its
two forms. Natively, BibTeX doesn't have any such system.

What BibTeX does have, however, is a macro system. These macros can be
defined in two places: 
	* `.bst` files (the bibliography styles themselves, generally less useful)
	* `.bib` files (the reference databases themselves: normally what you want)
The two macro syntaxes are not important. Suffice it to say that they let
you define, for example `jcp` as `J. Phys. Chem.`, and then, in your .bib file,
when you have an article, you define its journal as `jcp`, such as below:

    @article{feller1995lpm,
    	Author = {Feller, S.E. and Zhang, Y. and Pastor, R.W. and Brooks, B.R.},
    	Journal = jcp,
    	Keywords = {molecular dynamics; simulation methods},
    	Pages = {4613},
		Title = {Constant pressure molecular dynamics simulation: the {Langevin} piston method},
    	Volume = {103},
    	Year = {1995}}

BibTeX will automatically produce `J. Phys. Chem.` if the macro is defined,
either in the style file or the .bib file itself.

### The solution
BibTeX Macros give us a natural mechanism with which maintain our own database: the
macro name can serve as the key, and the short and long forms can
serve as the entries.

This project is a set of scripts that allows us to do just that. Given a
"database file," which is a plain text file with lines of the form

    macro_name|Shrt. Jrnl. Frm.|Long Journal Form
    acchrs|Acc. Chem. Res|Accounts of Chemical Research

you can use the `make_macros.sh` script (run without arguments to see a help
message) to generate macros either for `.bib` reference databases, or `.bst`
biography styles.

To get a list of the journals you are using, run the `get_journals.sh` script on
your `.bib` database. This should help you begin to generate your own database
file.

### The pitfalls
This scheme lets you maintain all the data (both short and long journal names),
and interconvert freely between the two forms of the data. However, it does
_not_ actually put the macros in your `.bib` or `.bst` files. You still have to
do this by hand. I may add this ability in later, but currently, the potential
for damage if this is done automatically is huge, so I suggest you copy and
paste the lines in by hand for now.

Furthermore, _it does not curate your references for you_.  It is still your
responsibility to make sure that all the papers in your reference database from
the _Journal of Physical Chemistry_ contain the entry `Journal = jcp`, and not
`Journal = {J. Phys. Chem.},`. Once you add a new reference that comes from a
journal that is not in your database, you have to edit the journal database,
re-run `make_macros.sh`, and update the macros in your `.bib` database. This
takes dilligence. But I just don't see a good way around it.

### The ISI abbreviation database
Finally, I've included my current journal abbreviation database in this project,
but I realize that most people do not use the same journals I do. So I took some
time to create a "general" version of the database, using the [ISI journal
abbreviations][0]. The abbreviations seem imperfect, and certainly my conversion
of them is heuristic and imperfect. But it's a start, and should hopefully lower
the barrier to adding new journals to your own database.

I would be keen on improving this list, along with other parts of this project. It's
functional, but has so much room for improvement.


MIT License
-----------
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

