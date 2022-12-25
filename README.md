# Windows-To-Linux
WTL (Beta) allows you to use Linux Functions in Windows Powershell/Command Prompt Terminal

This is still in BETA and will not work (yet). When it is finished, it will be an runable EXE file.

## Version
Currently, this is Version 0.2.1a of WTL. There are no instalations of WTL currently.

Beta Versions:

Version 0.2.1a:
- Mix usage of ```os``` and ```sub``` and removes:
```
"CompletedProcess(args='pwd', returncode =0):"
```
at shell. However, mv does not return proper output. 
```
Version 0.2.1b needs to fix MV subprocess arguments.
```
- Addds Color and Readability to ```README.md``` file.

Version 0.2.0:
 - Replaced "os" package with Subprocess package, migration official.
 ```
 Version 0.2.1 needs to remove: "CompletedProcess(args='pwd', returncode =0):" at shell
 ```

Version 0.1.4:
- Adds ```MV``` (rename) function to commandlist. Very buggy, needs migration to subprocess

Version 0.1.3b:
- Adds Subcommand (```cd -```, ```cd ..```) to CD command. 

Version 0.1.3a:
- Fixes CD Command (Part 1)
```
os.system('cd -l') is not supported in current windows os, thus needed to be replaced with os.chdir('-l')
```

Version 0.1.2a, b:
- Bug Fixes on CD Command and Listening Scripts
- Fixes on README.md

Version 0.1.2:
- CD Command

Version 0.1.1a
- LS Command

Version 0.1.0: 
- Control Loop
- Operating System Win to Linux Converter
