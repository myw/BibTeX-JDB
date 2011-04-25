#!/usr/bin/env python3
#
# reformat_abbrev 
# 
# Copyright Mikhail Wolfson 2011
#
# Take a partially processed database format file (parsed from the HTML in the
# ISI database: http://images.isiknowledge.com/WOK45/help/WOS/A_abrvjt.html)
# Perform the following 'clean-up' actions:
#   * Ensure that the titles all have periods at the end of every word
#   * Uncapitalize short words
#   * Put words not found in the dictionary in All-caps
#   * Assign keys to the file

import sys

_DICT_PATH = "/usr/share/dict/words"
_wordlist = set()
_uncap_words = set([
    'a', 'an', 'the', 'and', 'but', 'or', 'so', 'when', 'amid', 'as', 'at',
    'atop', 'but', 'by', 'down', 'for', 'from', 'in', 'into', 'like', 'mid',
    'near', 'next', 'of', 'off', 'on', 'onto', 'over', 'past', 'plus', 'than',
    'till', 'to', 'up', 'upon', 'via', 'with', 'cum', 'per', 'qua', 'sans',
    'unto', 'ago', 'away'
])
_foriegn_words = set([Zhurnal, Zentralblatt 
    
_used_keys = {}


def reformat_abbrev(file):
    for line in file:
        line = line.strip().replace('&', r'\&')

        title_lables = ('long', 'short')
        titles = {}
        full_words = set()

        # Load the titles in
        for tx, title in enumerate(line.split('|')):
            words = {'regular': title.split()}
            words['lower'] = [w.lower() for w in words['regular']]

            titles[title_lables[tx]] = words

        # Are we a foriegn language entry?
        # Determine this by looking for key words
        foriegn_language = False
        if any(lword in _foriegn_words for lword in titles['long']['regular']):
            foriegn_language = True

        # Uncapitalize short words in long form of title
        # We assume that these short words will not even be in the short title
        if len(titles['long']['regular']) >= 3:
            # Beginning and ending words are always cap'd
            for lwx, lword in enumerate(titles['long']['lower'][1:-1]):
                if lword in _uncap_words:
                    titles['long']['regular'][lwx + 1] = lword

        # Ensure acronyms are capitalized
        # Here, acronyms are heuristically defined as words which 
        # 1. are the same in both forms of the title
        # 2. are not in the dictionary, and 
        # 3. are no more than 5 letters long
        # 4. are not in a foriegn-language entry
        acronym_word_length = 5;
        for llwx, llword in enumerate(titles['long']['lower']):

            # search for a match in the short title
            for slwx, slword in enumerate(titles['short']['lower']):

                # record all short/long matches so that they do not
                # get periods after them in the short title
                if llword == slword:
                    full_words.add(llword)

                    if 1 < len(llword) <= acronym_word_length and \
                       1 < len(slword) <= acronym_word_length and \
                       not foriegn_language and \
                       not test_word(llword):
                        uword = llword.upper()
                        titles['long']['regular'][llwx] = uword
                        titles['short']['regular'][slwx] = uword

        # Make a key (want to use short title without periods for this)
        key = make_key(titles['short']['regular'])

        # Add periods at the end of non-acronym, non-full short words
        for slwx, slword in enumerate(titles['short']['lower']):
            sword = titles['short']['regular'][slwx]
            if len(sword) == 1 or slword not in full_words:
                titles['short']['regular'][slwx] = sword + '.'


        # Show the fully formatted line
        print('|'.join((
            key,
            ' '.join(titles['short']['regular']), 
            ' '.join(titles['long']['regular'])
        )))

def test_word(word):
    """Test a word to see if it is in the wordlist.

    Must already be lowercase. Wordlist must also be loaded."""
    # My wordlist does not contain plurals
    if word[-1] == 's':
        return word[0:-1] in _wordlist or word in _wordlist
    else:
        return word in _wordlist

def make_key(words):
    key_stems = []

    # Create a key from the first letter of every one of the short words
    key_length = 0
    total_letters = 0
    for word in words:
        key_stems.append(word[0])
        key_length += 1
        total_letters += len(word)

    min_key_length = 5 # How long most keys should be
    fuzz_factor = 2    # If a key is this many chars longer, no biggie
    
    # So many letters in the title that we need to really be picky
    # about which ones we include?
    if min_key_length + fuzz_factor < total_letters:

        # Add more data until we have reached the minimum key length
        word_index = 0
        while key_length < min_key_length:
            # If there are still characters to add from this word,
            # add the next one
            if len(key_stems[word_index]) < len(words[word_index]):
                key_stems[word_index] += \
                    words[word_index][len(key_stems[word_index])] 
                key_length += 1

            # Once you've run out of words, go back to the beginning
            # and add another letter from each word, assuming you can
            word_index = (word_index + 1) % len(words)

    else:
        # There are just not that many letters in the entire short title.
        # Use all of them.
        key_stems = words


    key = ''.join(key_stems).lower()

    # Make sure it's unique by adding a counter to the tail
    if key in _used_keys:
        _used_keys[key] += 1
        key += str(_used_keys[key])
    else:
        _used_keys[key] = 1

    return key

def _load_wordlist():
    """Make a set of lowercase versions of every word in the dictionary"""
    with open(_DICT_PATH) as words:
        for word in words:
            _wordlist.add(word.strip().lower());

def _help():
    print("{0} <filename> - clean up a partially processed file" 
            .format(sys.argv[0]))

def _main():
    if len(sys.argv) > 1:
        for fn in sys.argv[1:]:
            with open(fn) as file:
                reformat_abbrev(file)
    else:
        _help()

_load_wordlist();

if __name__ == "__main__":
    _main()

