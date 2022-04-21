#!/bin/bash

set -u
set -v

# This is similar to Alice, Bob and Carol. There we created and sent a
# blob of data, a message. Here we will create and send a tree of
# files.

# Instead of human first names, we'll use the fruit names Apple,
# Banana and Cherry. The new features are (i) using 'git add' and 'git
# write-tree' to create a tree, and (ii) a variant of the 'git
# cat-file' to show us a file in the tree.

# First as before we create the repositories.
git init --bare apple
git init --bare banana
git init --bare cherry


# Now we use 'git add' to store some files.
git --git-dir=apple \
    --work-tree=../texlive2022/texdir \
    add \
    texmf-dist/fonts/source/public/knuth-lib/

# Next we use 'git write-tree' to assemble these files into a tree
# object. The output is the hash of the tree.

# https://stackoverflow.com/questions/58668952/how-to-get-the-tree-hash-of-the-index-in-git
git --git-dir=apple \
    write-tree

HASH="c4c624c6ae60b5b838ba568e94a7a6b4c06c5acd"

# We tag as before.
git --git-dir=apple \
    tag \
    fonts/knuth-lib \
    $HASH

# Let's list the tags to check that it's there.
git --git-dir=apple \
    tag

# As before, Apple pushes the tree to Banana.
git --git-dir=apple \
    push banana \
    fonts/knuth-lib

# As before, Cherry fetches the tree from Banana.
git --git-dir=cherry \
    fetch banana \
    fonts/knuth-lib:fonts/knuth-lib

# Finally, a variant of 'git cat-file' shows us one of the files in
# the tree.
git --git-dir=cherry \
    cat-file -p \
    fonts/knuth-lib:texmf-dist/fonts/source/public/knuth-lib/test.mf
