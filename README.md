# python_seedcracker
Few lines of code that will bruteforce the random lib seed as long as the arguments are reasonable.

# But how?
Bruteforce :)

# Why python?
This was my first ever project and since then I have transitioned to C/C++

# Comparison
Added a archive that you should be able to use for comparison. <br _>
You should also have a enviroment set up with cython and setuptools, if not or you get errors just do a pull req, contact me somehow or try to fix it yourself lol.<br _>
### Usage (linux):
1. download, unzip and go (cd) into the folder <br _>
```
tar -xzf comparison-test.tar.gz
cd seed-op
```
3. you might need to compile the seed_search.pyx natively (if not goto 5)
4. to compile do:
```
python setup.py build_ext --inplace
```
5. run the convenience script 'run.sh'
```
chmod +x run.sh
./run.sh
```
![test](https://github.com/user-attachments/assets/d7825a66-a52e-4556-a7b0-081fa9af47be)
