# Windows-To-Linux
WTL (Beta) allows you to use Linux Functions in Windows Powershell/Command Prompt Terminal

This is still in BETA and will not work (yet). When it is finished, it will be an runable EXE file.

## Alternative
Read about WSL to use the SUPPORTED Linux Subsystem to Windows here: https://learn.microsoft.com/en-us/windows/wsl/install
This program is offered as an "portable" setup to this while retaining all files and commands and ease of access as an windows commandline.

## Version
Currently, this is Version 0.2.2 of WTL. There is one instalation of WTL, which is the current 0.2.2 Version.

Beta Versions:

ersion 0.2.2:
 (Continuation of Update 0.1.4 with Merging with ```os``` and ```subprocess```)
 - Fixes MV Function with help of:
 https://stackoverflow.com/questions/74908816/subprocess-run-cmd-args-returns-filenotfounderror

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
