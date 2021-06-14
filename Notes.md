# Notes.md - Markdown file with notes

## Markdown notes
  https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf  
  Secret pro tip: to force a new line, add two spaces at the end of the line. Otherwise it will wrap.  
  
## Conda Python installation
  Mostly follow steps here: https://github.com/csherwood-usgs/SSF_2021.git This will provide an environment `IOOS` that has most of the packages needed.  
  Some minor changes:
  * After the initial installation of `miniconda`, add support for a basic Unix-like shell command by typing:   
  `conda install m2-base`
  * Download the `environment.yml` file to a local folder. Maybe edit it to add `m2-base` to the package list, and/or change the environment name from `IOOS` to something more personal. 
  * Follow the remaining instructions.  

## Get a good program editor
  * I like Atom https://atom.io/

## Get a Github account
  * https://github.com/

## Install Git on your computer
* https://desktop.github.com/  
* I use the bash window
* Follow the setup instructions here: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

## My git workflow  
* To make a new repo:
  * On the Github site, create a repo and include an README.md file. Put some text in that file. I often put info about where I will store the local copy (e.g. "this repo resides in `\src\reponame` on my laptop").
  * Copy the URL for the repo into the clipboard. Switch to your git bash window, and cd to the parent directory (above where you plan to put the repo...eg. `\src`).
  * `git clone URLforreponame` - Will put a local copy of reponame in `\src\reponame`
  * `cd reponame` - Switch to `reponame`. Maybe copy in versions of a licence.
  * `add somefilename` - Add a filename to be tracked by Git
  * `add *.ipynb` - Will track all of your Jupyter notebooks
  * `commit -a - m "some comment"` - Will stage all of you changed, tracked files for committing, with "some comment" as a memo.
  * `git push` - Will push staged commits to the Github cloud repo. Should do these last two steps often, but for sure at end of an editing session.  
  * `git pull` - First thing you should do when starting to work on a repo.  
  
