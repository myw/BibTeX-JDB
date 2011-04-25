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
maintain some database that contains a single entry for the journal and both of
its abbreviations. Natively, BibTeX doesn't have any such system.

What BibTeX does have, however, is an abbreviation system. Abbreviations can be
defined in two places: 
	* `.bst` files (the bibliography styles themselves, generally less useful)
	* `.bib` files (the reference databases themselves: normally what you want)
The two abbreviation syntaxes are not important. Suffice it to say that they let
you define, for example `jcp` as `J. Phys. Chem.`, and t




MIT License
-----------
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

