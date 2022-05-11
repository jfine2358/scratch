# ISO vs TGZ vs GIT as TeXLive 2022 media

### News - Wed 10 May 2022

I've added a script to 
* [convert a folder (directory) into a git pack file](pack_dir.sh).

The rest of this news items is for actual and aspiring git experts. Ordinary users won't see any of this.

#### Call

Here's one way to access files in /git-alt-obj.

```bash
$ GIT_ALTERNATE_OBJECT_DIRECTORIES=/git-alt-obj/texlive/ \
    git --git-dir=empty.git \
    cat-file -p \
    $(cat /git-alt-obj/texlive/pack/texlive-2022*root):tex/plain/knuth-lib/story.tex
```

#### Response

And here's what comes back.

```tex
\hrule
\vskip 1in
\centerline{\bf A SHORT STORY}
\vskip 6pt
\centerline{\sl    by A. U. Thor} % !`?`?! (modified)
\vskip .5cm
Once upon a time, in a distant
  galaxy called \"O\"o\c c,
there lived a computer
named R.~J. Drofnats.

Mr.~Drofnats---or ``R. J.,'' as
he preferred to be called---% error has been fixed!
was happiest when he was at work
typesetting beautiful documents.
\vskip 1in
\hrule
\vfill\eject

```

#### Content of `/git-alt-obj`

```bash
$ ls -sh /git-alt-obj/texlive/pack/ | grep pack
1.3G texlive-2010-texmf-dist-287d05469ee25c2375e22319fc1fb0b9c0fb4051.pack
1.4G texlive-2011-texmf-dist-430f40e5064f41d2eed81cd83f78158735fc3808.pack
1.6G texlive-2012-texmf-dist-cf7f31d632e5adf79472ecafba594816f3997d41.pack
1.8G texlive-2013-texmf-dist-a9451b8debeb824af5024b755c16cdd6f1e73aa0.pack
2.0G texlive-2014-texmf-dist-286fe1dbb6d6fd5b7141172a41458e8be9bb4ec3.pack
2.1G texlive-2015-texmf-dist-b634349587c2787c9f04b600a34f5d030190404b.pack
2.3G texlive-2016-texmf-dist-254d8ec1d2845749a24ea8e485415e451d751723.pack
2.7G texlive-2017-texmf-dist-1e37ca86450504b6876fcf6ab76289f333734980.pack
2.9G texlive-2018-texmf-dist-c22b8033a249f137429673f47e8304261725ca92.pack
3.2G texlive-2019-texmf-dist-8132ba78f614c1eb216af27f65abe597e37346b1.pack
3.6G texlive-2020-texmf-dist-8c9212b5bfaaebcbcfe267858ca0eba6c5391a8b.pack
3.9G texlive-2021-texmf-dist-7493e3369269a9a1657b37428042aa8a2c6ec44d.pack
4.1G texlive-2022-texmf-dist-24827e0e274c48ff25778b5135ac2959f7109a81.pack
```


### News - Thu 21 April 2022

I've added two scripts that show the basics of how I intend to
transfer files between git repositories.

* [Alice send a message to Carol via Bob](alice-bob-carol.sh)
* [Apple sends a tree of files to Cherry via Banana](apple-banana-cherry.sh)

Because git networked file system, there's no problem adapting the
script to transfer the files via the internet.


## A toy problem

One way to install TeXLive is to download an ISO (i.e. a DVD image)
and from there create a TeX installation. Many people for simplicity
choose a full installation. The toy problem is to make this process
quicker (and perhaps also easier).

## Goals and the test environment

The speed of installation depends very much on the speed of the
so-called hard disk. Today the hard disk is very often a solid state
disk (SSD), which is a rectangular non-rotating object.

I've recently rebuilt my computer and now have ample RAM. This allows
me to go even quicker, by placing both the source and target of my
installation on what is called a RAM disk.

Using the RAM disk makes large scale input-output even quicker than a
SSD. It also gives much more consistency regarding results, which is
important when testing.

The download speed depends on the internet connection. This is well
understood, and making a quicker download is a secondary goal of this
project.

## Initial results

### ISO: The standard install

A full standard install takes 9 minutes. Because of the RAM disk, and
the process being mainly single core, the real time is close to the
sum of the user and system CPU times.

The TeXLive 2022 ISO is about 4.3G.

```bash
$ time perl texcol2022/texlive/install-tl -profile texlive2022.profile

real	9m1.196s
user	7m30.872s
sys	1m30.456s

```

### RAM disk: Very high speed install

Copying an existing install is a quick way to create a new
install. This provides something close to an absolute lower bound for
installation time.

When using a RAM disk this lower bound is much lower than 9
minutes. In fact, for me it is just under 3 seconds, which is about
250 times quicker. It would be very hard to get quicker than this.

The full install of TeXLive 2022 is about 7.4G.

```bash
time cp -r texlive2022 tmp

real	0m2.736s
user	0m0.143s
sys	0m2.578s
```

### TGZ: Install from a compressed image

If we install from the ISO (4.3G) to disk (7.4G) and then compress a
tag archive (TGZ) we got back down to (4.4G). So how long does that
take to install?

The answer is almost 29 seconds, just over 10 times slower than the
absolute lower bound.


```bash
$ time tar -xzf texlive2022.tgz -C tmp

real	0m28.973s
user	0m28.284s
sys	0m4.009s
```

### GIT: Install from version control

Instead of using a TGZ, I tried installing from a Git repository.

The answer is almost 17 seconds, just over 6 times slower than the
absolute lower bound.

```bash
tmp$ time git --git-dir=../texlive2022.git/.git checkout -f

real	0m16.733s
user	0m14.645s
sys	0m2.316s
```

## Sizes compared

It turns out that the installation sources ISO, TGZ and GIT all have
close to the same size, namely 4.3 to 4.4G.

I'm surprised that the GIT comes in smaller than the TGZ. This asks
for further investigation, and I suspect there may be an error
somewhere.

If there's not an error perhaps it comes down to this. With Git the
filename paths are stored in 'compressed' form, the timestamp is
discarded, as is the owner, group and permissions.

```bash
$ du -s -h texlive2022.iso texlive2022.tgz texlive2022.git texlive2022

4.3G	texlive2022.iso
4.4G	texlive2022.tgz
4.3G	texlive2022.git
7.4G	texlive2022
```
