import subprocess


def cat_blob(repos, git_oid):

    args = 'git cat-file -p'.split()
    args.append(git_oid)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, cwd='mybook')
    return proc.stdout


git_oid = "b7ef266514be61ae088f9ba9bfd5d3858078bfaa"


if __name__ == '__main__':

    print('''\
#    # You first need to populate Git repos 'mybook'.
#
#    print(git_oid)
#    fakefile = cat_blob('mybook', git_oid)
#
#    fakefile.read(5)
'''
      )
