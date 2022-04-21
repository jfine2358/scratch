# ISO vs TGZ vs GIT as TeXLive 2022 media

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