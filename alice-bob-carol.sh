#!/bin/bash

set -u
set -v

# We're going to use git's push and fetch commands to send a message
# from Alice to Carol, via Bob.

# Bare repositories store objects, tags and pointers. They can't be
# used for version control. They can be used to store and share the
# objects created by version control.

# Bare repositories are good for sharing objects, and also for
# creating simple objects (such as blobs and trees).

# We create a git repository for Alice, Bob and Carol. Here they're in
# the same folder on the same machine. But all that's really required
# is that the three repositories are accessible via a network service.

# Here goes.
git init --bare alice
git init --bare bob
git init --bare carol

# The three repositories are identical. (The 'diff -r' command
# recursively looks for differences in trees.)
diff -r alice bob
diff -r bob carol
diff -r carol alice

# Here's a low-level git command that adds a blob to a git repository.
echo 'Hi Carol, this is Alice.' \
    | git --git-dir=alice \
	  hash-object \
	  -w \
	  --stdin

# The previous command gaves us a hash. Git stores objects according
# to their hash. Git is a distributed Content Addressable Store (CAS),
# that can be used for version control. But it can also be used just
# as a distributed CAS.

# The same message always gives the same hash, and it's very, very,
# very, ..., very hard to find two different messages that give the
# same hash.

# Here's that HASH, stored for future use.
HASH="da68aeea5eef38061fa8b015c65bfccd0d0c555d"

# Git uses tags as human readable names. To avoid confusion, it's best
# not to change the value (hash) of a tag once it has been created.

# Here we use 'a/msg/1' as an alternative to the unreadable hash.
git --git-dir=alice \
    tag a/msg/1 $HASH

# So far, all action has taken place in Alice's repository. Let's see
# what's changed.
diff -r alice bob

# All set. Alice now pushes her message to Bob.
git --git-dir=alice \
    push bob \
    a/msg/1

# Now, the repositories for Alice and Bob are identical.
diff -r alice bob

# And the repositories for Bob and Carol are different.
diff -r bob carol

# To conclude our story, Carol fetches Alice's message from Bob.
git --git-dir=carol \
    fetch bob \
    a/msg/1:a/msg/1

# And to check our work, let's compare Bob and Carol's
# repositories. (The difference you see is because I need a feature
# that's only available in a more recent version of git than the one I
# have.)
# https://www.spinics.net/lists/git/msg386235.html
diff -r bob carol

# Finally, Carol will want to read the message from Alice.
git --git-dir=carol \
    cat-file -p \
    a/msg/1


# All this will work over the network, and for larger files.
