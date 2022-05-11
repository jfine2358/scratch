#!/bin/bash

set -e
set -u

DIR="${1}"
NAME="${2}"

# Create a temporary git repository.
GITDIR="tmp-${NAME}.git"
git init --bare "${GITDIR}"

# Add the directory contents to the git repository.
git --git-dir="${GITDIR}" \
    --work-tree="${DIR}" \
    add \
    .

# Convert the contents to a tree.
DIRHASH=$(
    git --git-dir="${GITDIR}" \
	write-tree
	)

# Pack the tree.
PACKHASH=$(
    echo ${DIRHASH} \
	| \
	git --git-dir="${GITDIR}" \
	    pack-objects \
	    --all \
	    "${NAME}"
	)
# Record the hash of the directory.
ROOTFILE="${NAME}-${PACKHASH}.root"
echo ${DIRHASH} > "${ROOTFILE}"
chmod -w "${ROOTFILE}"

# Report result to console.
echo
echo "DIR=${DIR}"
echo "NAME=${NAME}"
echo "DIRHASH=${DIRHASH}"
echo "PACKHASH=${PACKHASH}"

# Remove the temporary working directory.
rm -rf "${GITDIR}"
