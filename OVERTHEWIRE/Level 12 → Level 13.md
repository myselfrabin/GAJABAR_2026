## Bandit Level 12 → Level 13

> **Platform:** OverTheWire **Game:** Bandit **Level:** 12 -> 13 **Topic:** The password for the next level is stored in the file **data.txt**, which contains a hexdump of a file that has been repeatedly compressed. Figure out what kind of file it is, and extract the original file.

## GOAL:
- The file `data.txt` holds a hexdump of some data, not the actual binary. So the plan is: reverse the hexdump back into binary, figure out what compression format it is, decompress it, and repeat this process as many times as needed until I land on the final file with the password.

## ANALYSIS:
- First I copied `data.txt` into a fresh working directory, since this challenge needed a lot of intermediate files and I didn't want to mess up my home folder.

![](Attachments/Pasted%20image%2020261004174857.png)

- Since `data.txt` is just a hexdump and not real binary data, I reversed it back into binary form using `xxd -r`.

![](Attachments/Pasted%20image%2020261004175101.png)

- Checked the resulting file's type to see what I was dealing with.

![](Attachments/Pasted%20image%2020261004175153.png)

- It turned out to be compressed data, so I kept renaming the file with the right extension and decompressing it, checking the type again after each step.

![](Attachments/Pasted%20image%2020261004175306.png)

![](Attachments/Pasted%20image%2020261004175507.png)

![](Attachments/Pasted%20image%2020261004175624.png)

![](Attachments/Pasted%20image%2020261004175826.png)

![](Attachments/Pasted%20image%2020261004175952.png)

![](Attachments/Pasted%20image%2020261004180105.png)

- At this point we know it's a `bz2` file signature.

![](Attachments/Pasted%20image%2020261004180359.png)

- Still not clear data though. So again I reversed the file to check its file signature using `xxd`.

![](Attachments/Pasted%20image%2020261004180506.png)

- It showed `1f8b` signature again — this means gzip. So I needed to change the file extension to `.gz` and decompress it again.

![](Attachments/Pasted%20image%2020261004180624.png)

- This time it showed it's `data5.bin`. Since it's a bin file, I could go ahead and `tar` it.

![](Attachments/Pasted%20image%2020261004180929.png)

- It seems `data5.bin` is actually another archive file called `data6.bin`, so I repeated the same process on this one too — extracting `data5.bin` again.

![](Attachments/Pasted%20image%2020261004181151.png)

- At this point I found out that `data6.bin` is bzip2 compressed, which I confirmed using the `file` command. So I changed the extension to `.bz2` and decompressed it again.

![](Attachments/Pasted%20image%2020261004181758.png)

- From here, I got a file called `data6.bin.out`.

![](Attachments/Pasted%20image%2020261004182021.png)

- I also got a `data8.bin` file at this point.

![](Attachments/Pasted%20image%2020261004182336.png)

- Another important file here was `data6.bin.out`.

![](Attachments/Pasted%20image%2020261004182423.png)

- Turns out it's a tar archived file.

![](Attachments/Pasted%20image%2020261004182550.png)

- After running `tar` on `data6.bin.out`, I got the `data8.bin` file.

![](Attachments/Pasted%20image%2020261004182657.png)

- Checking `data8.bin`, it turned out to be gzip compressed again. So I changed it to `.gz` and decompressed it one more time.

![](Attachments/Pasted%20image%2020261004183009.png)

- And the password for the next level is:

```text
qQYQiHOBPR8zR61qxYqX45quvihF2uzk
```