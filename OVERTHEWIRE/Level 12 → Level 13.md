

![](Pasted%20image%2020261004174857.png)


![](Pasted%20image%2020261004175101.png)

![](Pasted%20image%2020261004175153.png)

![](Pasted%20image%2020261004175306.png)

![](Pasted%20image%2020261004175507.png)

![](Pasted%20image%2020261004175624.png)

![](Pasted%20image%2020261004175826.png)

![](Pasted%20image%2020261004175952.png)


![](Pasted%20image%2020261004180105.png)
- At this point we know it's `b2z` file  signature
![](Pasted%20image%2020261004180359.png)

- Still not clear data.
- Again we need to reverse the file to see what's file signature using `xxd`.
![](Pasted%20image%2020261004180506.png)
- It holds again: `1f8b` signature means gzip file signature means we need to again change file into .gz and then decompress again.

![](Pasted%20image%2020261004180624.png)
- Ok this time it shows it's `data5 bin`
- Now at this point I can tar the file cause it's bin file.

![](Pasted%20image%2020261004180929.png)

- Now it seems that `data5.bin` is another archieve file called: `data6.bin` so doing same process for this too.
- I will extract the `data5.bin` file again.
![](Pasted%20image%2020261004181151.png)

- Now at this point I know that the file `data6.bin` is bzip2 compress: I got this info when I checked it by using `file` command.
- Now I will be changing the file into `.bz2` extension and `decompress` it again.
![](Pasted%20image%2020261004181758.png)
- So from here I know that there's a file called: `data6.bin.out`
![](Pasted%20image%2020261004182021.png)

- I got `data8.bin` file here.
![](Pasted%20image%2020261004182336.png)
- Another imp file I got here is: `data6.bin.out` file 
![](Pasted%20image%2020261004182423.png)
- So it's tar archived file
![](Pasted%20image%2020261004182550.png)
- Ok after using tar on `data6.bin.out` file I got an `data8.bin` file there.
![](Pasted%20image%2020261004182657.png)
- Checking the `data8.bin` file it's gzip compress now changin it into gzip and decompressd it.

![](Pasted%20image%2020261004183009.png)

- And the password for next level is:
```text
qQYQiHOBPR8zR61qxYqX45quvihF2uzk
```