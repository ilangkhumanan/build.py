Compiled with warnings.

./src/Components/SearchBar/SearchBar.jsx
  Line 12:12:  'errorMessage' is assigned a value but never used  no-unused-vars

./src/Components/AdminBlock/AdminBlock.jsx
  Line 1:17:  'useState' is defined but never used  no-unused-vars

Search for the keywords to learn more about each warning.
To ignore, add // eslint-disable-next-line to the line before.

npm
^C
MacBook-Pro:late-checker tik$ npm run dev
npm ERR! missing script: dev

npm ERR! A complete log of this run can be found in:
npm ERR!     /Users/tik/.npm/_logs/2020-01-12T10_02_24_075Z-debug.log
MacBook-Pro:late-checker tik$ npm run
Lifecycle scripts included in late-checker:
  start
    react-scripts start
  test
    react-scripts test

available via `npm run-script`:
  build
    react-scripts build
  eject
    react-scripts eject
MacBook-Pro:late-checker tik$ npm run-script
Lifecycle scripts included in late-checker:
  start
    react-scripts start
  test
    react-scripts test

available via `npm run-script`:
  build
    react-scripts build
  eject
    react-scripts eject
MacBook-Pro:late-checker tik$ ls
README.md		package-lock.json	public
node_modules		package.json		src
MacBook-Pro:late-checker tik$ cd
MacBook-Pro:~ tik$ cd..
-bash: cd..: command not found
MacBook-Pro:~ tik$ cd ..
MacBook-Pro:Users tik$ ls
Shared	tik
MacBook-Pro:Users tik$ cd tik
MacBook-Pro:~ tik$ ls
Applications			Music
Applications (Parallels)	Parallels
Blend				Pictures
Desktop				Public
Documents			Untitled.ipynb
Downloads			aws
Library				build
Movies				dlib
MacBook-Pro:~ tik$ cd build
MacBook-Pro:build tik$ ls
Websites		flutter			taxikini
amadeus			osxcputemp		xibo-docker-2.2.1
aws			rekognition
MacBook-Pro:build tik$ cd ..
MacBook-Pro:~ tik$ cd ..
MacBook-Pro:Users tik$ cd
MacBook-Pro:~ tik$ cd
MacBook-Pro:~ tik$ cd ..
MacBook-Pro:Users tik$ cd ..
MacBook-Pro:/ tik$ ls
Applications			dev
EFI-Backups			etc
Library				home
Network				installer.failurerequests
System				net
Users				private
Volumes				sbin
aos.build.py			tmp
bin				usr
cores				var
MacBook-Pro:/ tik$ python3 aos.build.py
MacBook-Pro:/ tik$ python3
Python 3.7.5 (default, Nov  1 2019, 02:16:32) 
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
MacBook-Pro:/ tik$ python3
Python 3.7.5 (default, Nov  1 2019, 02:16:32) 
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
MacBook-Pro:/ tik$ python3 aos.build.py
MacBook-Pro:/ tik$ python3 aos.build.py
MacBook-Pro:/ tik$ python3 aos.build.py
MacBook-Pro:/ tik$ python3 aos.build.py
MacBook-Pro:/ tik$ python3 nano aos.build.camera.py
/usr/local/Cellar/python/3.7.5/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python: can't open file 'nano': [Errno 2] No such file or directory
MacBook-Pro:/ tik$ nano aos.build.camera.py

  GNU nano 2.0.6           File: aos.build.camera.py                  Modified  

import opencv as c

c.videocapture(0)

















^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Page ^K Cut Text  ^C Cur Pos
^X Exit      ^J Justify   ^W Where Is  ^V Next Page ^U UnCut Text^T To Spell

import cv2 as class classname(object):
  pass
