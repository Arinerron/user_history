# what is this

a poorly-written tool that logs other users' command history from an account without root privileges that i made in like 10 mins

# usage

```
sh run.sh
```

then check the `logs/` directory for each user's logs

# why

* pretty useful for shared ssh users. you never know, you might find accidental sudo password (mis)entries in the logs
* sometimes on ctf servers people put their exploit scripts in `/tmp`. often you don't have perms to list the files in `/tmp` so you don't know where to look (besides the obvious: `/tmp/exploit.py`, `/tmp/pwn.py`, etc), but this tool gives you the information you need to find them.
