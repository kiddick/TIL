##Find and remove files by pattern

to find files:
```bash
find . -name "*.ext" -type f
```

to remove:
add `-delete` option
```bash
find . -name "*.bak" -type f -delete
```

[>> source](http://askubuntu.com/a/377442/481836)
